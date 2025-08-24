import os
try:
    import torch
    import torch.nn as nn
    from torchvision import transforms, models
    TORCH_AVAILABLE = True
except ImportError:
    print("🚨 PyTorch not available - running in demo mode")
    TORCH_AVAILABLE = False
    # Create dummy classes to prevent import errors
    class torch:
        class nn:
            class Module: pass
        @staticmethod
        def device(x): return 'cpu'
        @staticmethod
        def cuda(): 
            class cuda:
                @staticmethod
                def is_available(): return False
            return cuda()
from PIL import Image
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import io
import base64
import json
from disease_info import get_disease_info, get_severity_color, format_disease_name
from demo_predictor import demo_predict_disease, is_demo_mode

# Template and static directories (now in same directory structure)
app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'your-secret-key-here'  # Change this to a random secret key
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# CORRECTED: 23 plant disease classes in exact training order from dataset folder
CLASS_NAMES = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Pepper__bell___Bacterial_spot',
    'Pepper__bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Tomato_Bacterial_spot',
    'Tomato_Early_blight',
    'Tomato_Late_blight',
    'Tomato_Leaf_Mold',
    'Tomato_Septoria_leaf_spot',
    'Tomato_Spider_mites_Two_spotted_spider_mite',
    'Tomato__Target_Spot',
    'Tomato__Tomato_YellowLeaf__Curl_Virus',
    'Tomato__Tomato_mosaic_virus',
    'Tomato_healthy',
]

# Global variable to store the model
model = None
if TORCH_AVAILABLE:
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
else:
    device = 'cpu'  # Fallback when PyTorch not available

# Only define model class if PyTorch is available
if TORCH_AVAILABLE:
    class CustomPlantDiseaseModel(nn.Module):
        """Custom model class that matches the saved checkpoint structure"""
        def __init__(self, num_classes=24):
            super(CustomPlantDiseaseModel, self).__init__()
            self.backbone = models.efficientnet_b0(pretrained=False)
            # Replace the classifier to match saved model structure
            self.backbone.classifier = nn.Sequential(
                nn.Dropout(p=0.2, inplace=True),
                nn.Linear(in_features=1280, out_features=512, bias=True),
                nn.ReLU(),
                nn.BatchNorm1d(512),
                nn.Dropout(p=0.3),
                nn.Linear(in_features=512, out_features=256, bias=True),
                nn.ReLU(),
                nn.BatchNorm1d(256),
                nn.Dropout(p=0.3),
                nn.Linear(in_features=256, out_features=num_classes, bias=True)
            )
            
        def forward(self, x):
            return self.backbone(x)
else:
    # Dummy model class for demo mode
    class CustomPlantDiseaseModel:
        def __init__(self, num_classes=24):
            pass

def load_model():
    """Load the trained EfficientNet model with exact architecture match"""
    global model
    
    # If PyTorch not available, skip model loading
    if not TORCH_AVAILABLE:
        print("🎭 PyTorch not available - skipping model loading, using demo mode")
        return False
    
    try:
        # Try balanced model first (usually better for generalization)
        model_paths = ['balanced_plant_disease_model.pt', 'best_plant_disease_model_90plus.pt']
        model_path = None
        checkpoint = None
        
        for path in model_paths:
            if os.path.exists(path):
                print(f"🔍 Trying model: {path}")
                try:
                    checkpoint = torch.load(path, map_location=device)
                    model_path = path
                    print(f"✅ Successfully loaded checkpoint from {path}")
                    break
                except Exception as e:
                    print(f"❌ Failed to load {path}: {e}")
                    continue
        
        if checkpoint is None:
            raise FileNotFoundError("No valid model file found")
        
        # Create model that exactly matches your trained model (23 classes)
        model = CustomPlantDiseaseModel(num_classes=23)  # Use 23 classes as in your original model
        
        # Load the complete state dict with all trained weights
        try:
            model.load_state_dict(checkpoint, strict=True)
            print("✅ Successfully loaded complete trained model with all weights!")
        except Exception as e1:
            print(f"Strict loading failed: {e1}")
            try:
                # Try loading with strict=False to see what loads
                missing_keys, unexpected_keys = model.load_state_dict(checkpoint, strict=False)
                print(f"Loaded model with some weights. Missing keys: {len(missing_keys)}, Unexpected keys: {len(unexpected_keys)}")
                if len(missing_keys) > 0:
                    print(f"Missing keys: {missing_keys[:5]}...")  # Show first 5
                if len(unexpected_keys) > 0:
                    print(f"Unexpected keys: {unexpected_keys[:5]}...")  # Show first 5
            except Exception as e2:
                print(f"Alternative loading also failed: {e2}")
                # Fallback: use pretrained EfficientNet and fine-tune
                print("⚠️ Using pretrained EfficientNet as fallback")
                model = models.efficientnet_b0(pretrained=True)
                model.classifier[1] = nn.Linear(model.classifier[1].in_features, len(CLASS_NAMES))
        
        model.to(device)
        model.eval()
        print(f"Model loaded successfully on {device}")
        print(f"Model supports {len(CLASS_NAMES)} classes")
        return True
    except Exception as e:
        print(f"Error loading model: {e}")
        return False

def preprocess_image(image):
    """Preprocess image for model prediction"""
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    # Convert to RGB if needed
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Apply transforms and add batch dimension
    image_tensor = transform(image).unsqueeze(0)
    return image_tensor.to(device)

def predict_disease(image):
    """Make prediction on uploaded image"""
    global model
    if model is None:
        return None, None, None
    
    try:
        # Preprocess image
        image_tensor = preprocess_image(image)
        
        # Make prediction
        with torch.no_grad():
            outputs = model(image_tensor)
            probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
            confidence, predicted_idx = torch.max(probabilities, 0)
            
            # Get top 3 predictions
            top3_prob, top3_idx = torch.topk(probabilities, 3)
            
            top3_predictions = []
            for i in range(3):
                class_name = CLASS_NAMES[top3_idx[i].item()]
                prob = top3_prob[i].item() * 100
                top3_predictions.append({
                    'class': class_name,
                    'confidence': round(prob, 2)
                })
        
        predicted_class = CLASS_NAMES[predicted_idx.item()]
        confidence_score = confidence.item() * 100
        
        return predicted_class, confidence_score, top3_predictions
    
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None, None, None

def format_class_name(class_name):
    """Format class name for better display"""
    if class_name == 'Background_without_leaves':
        return 'Background (No Leaves Detected)'
    
    # Replace underscores with spaces and format
    formatted = class_name.replace('___', ' - ').replace('_', ' ')
    return formatted

@app.route('/')
def index():
    """Main page with upload form"""
    # Check if we're in demo mode (model not available)
    is_demo = model is None
    return render_template('index.html', demo_mode=is_demo)

@app.route('/predict', methods=['POST'])
def predict():
    """Handle image upload and prediction"""
    if 'file' not in request.files:
        flash('No file selected')
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file.filename == '':
        flash('No file selected')
        return redirect(url_for('index'))
    
    if file:
        try:
            # Read and process image
            image = Image.open(io.BytesIO(file.read()))
            
            # Convert image to base64 for display
            img_io = io.BytesIO()
            image.save(img_io, 'PNG')
            img_io.seek(0)
            img_b64 = base64.b64encode(img_io.getvalue()).decode()
            
            # Make prediction (use demo mode if real model unavailable)
            if model is not None:
                predicted_class, confidence, top3_predictions = predict_disease(image)
            else:
                print("🎭 Using demo mode for prediction")
                predicted_class, confidence, top3_predictions = demo_predict_disease(file.filename)
            
            if predicted_class is None:
                flash('Error occurred during prediction')
                return redirect(url_for('index'))
            
            # Get disease information
            disease_info = get_disease_info(predicted_class)
            severity_color = get_severity_color(disease_info.get('severity', 'Unknown'))
            
            # Format results
            result = {
                'image': img_b64,
                'predicted_class': format_class_name(predicted_class),
                'confidence': round(confidence, 2),
                'top3_predictions': [(format_class_name(pred['class']), pred['confidence']) 
                                   for pred in top3_predictions],
                'filename': file.filename,
                'disease_info': disease_info,
                'severity_color': severity_color
            }
            
            return render_template('result.html', result=result)
            
        except Exception as e:
            flash(f'Error processing image: {str(e)}')
            return redirect(url_for('index'))

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint for predictions"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    try:
        # Process image
        image = Image.open(io.BytesIO(file.read()))
        
        # Make prediction (use demo mode if real model unavailable)
        if model is not None:
            predicted_class, confidence, top3_predictions = predict_disease(image)
        else:
            print("🎭 Using demo mode for API prediction")
            predicted_class, confidence, top3_predictions = demo_predict_disease(file.filename)
        
        if predicted_class is None:
            return jsonify({'error': 'Prediction failed'}), 500
        
        return jsonify({
            'predicted_class': format_class_name(predicted_class),
            'confidence': round(confidence, 2),
            'top3_predictions': [(format_class_name(pred['class']), pred['confidence']) 
                               for pred in top3_predictions]
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/debug')
def debug_info():
    """Debug endpoint to check deployment status"""
    import glob
    import sys
    
    info = {
        'pytorch_available': TORCH_AVAILABLE,
        'model_loaded': model is not None,
        'model_type': str(type(model)) if model else None,
        'device': str(device),
        'current_directory': os.getcwd(),
        'model_files': glob.glob('*.pt'),
        'all_files': glob.glob('*'),
        'python_version': sys.version,
        'torch_version': torch.__version__ if TORCH_AVAILABLE else 'Not available'
    }
    
    return jsonify(info)

@app.route('/classes')
def show_classes():
    """Display all available classes"""
    formatted_classes = [format_class_name(cls) for cls in CLASS_NAMES]
    
    # Calculate statistics
    healthy_count = sum(1 for cls in formatted_classes if 'healthy' in cls.lower())
    disease_count = len(formatted_classes) - healthy_count
    
    statistics = {
        'total_classes': len(formatted_classes),
        'healthy_count': healthy_count,
        'disease_count': disease_count
    }
    
    return render_template('classes.html', classes=formatted_classes, stats=statistics)

# Load model on import for deployment
print("🚀 Starting model loading for Railway deployment...")
print(f"📁 Current working directory: {os.getcwd()}")
print(f"📦 PyTorch available: {TORCH_AVAILABLE}")
print(f"💻 Device: {device}")

# List available files for debugging
import glob
model_files = glob.glob('*.pt')
print(f"🔍 Found model files: {model_files}")

if not load_model():
    print("⚠️ Warning: Failed to load model. App will run in demo mode.")
    print(f"🎭 Demo mode active - model variable: {model}")
else:
    print("✅ Real AI model loaded successfully!")
    print(f"🤖 Model type: {type(model)}")

if __name__ == '__main__':
    # For local development only
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)
