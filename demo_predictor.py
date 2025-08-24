"""
Demo predictor for deployment environments where model files can't be loaded.
Returns realistic-looking fake predictions for demonstration purposes.
"""
import random
import time

# Demo predictions for different types of plant images
DEMO_PREDICTIONS = {
    'apple': [
        ('Apple___Apple_scab', 87.5),
        ('Apple___Black_rot', 72.3),
        ('Apple___Cedar_apple_rust', 68.9),
        ('Apple___healthy', 95.2)
    ],
    'tomato': [
        ('Tomato_Early_blight', 89.1),
        ('Tomato_Bacterial_spot', 76.8),
        ('Tomato_Late_blight', 84.2),
        ('Tomato_Leaf_Mold', 79.3),
        ('Tomato_Septoria_leaf_spot', 73.1),
        ('Tomato__Target_Spot', 71.4),
        ('Tomato__Tomato_YellowLeaf__Curl_Virus', 68.7),
        ('Tomato__Tomato_mosaic_virus', 74.9),
        ('Tomato_Spider_mites_Two_spotted_spider_mite', 67.2),
        ('Tomato_healthy', 92.4)
    ],
    'potato': [
        ('Potato___Early_blight', 81.3),
        ('Potato___Late_blight', 77.9),
        ('Potato___healthy', 88.7)
    ],
    'corn': [
        ('Corn_(maize)___Common_rust_', 79.4),
        ('Corn_(maize)___Northern_Leaf_Blight', 73.2),
        ('Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 75.6),
        ('Corn_(maize)___healthy', 91.8)
    ],
    'pepper': [
        ('Pepper__bell___Bacterial_spot', 78.3),
        ('Pepper__bell___healthy', 89.1)
    ],
    'default': [
        ('Tomato_Early_blight', 83.2),
        ('Apple___Apple_scab', 79.8),
        ('Potato___Early_blight', 76.4),
        ('Corn_(maize)___Common_rust_', 74.1),
        ('Tomato_Bacterial_spot', 81.7),
        ('Apple___Black_rot', 69.3),
        ('Tomato_healthy', 88.5),
        ('Apple___healthy', 85.3),
        ('Potato___healthy', 87.9),
        ('Corn_(maize)___healthy', 90.2)
    ]
}

def demo_predict_disease(image_filename):
    """
    Generate demo prediction based on filename or random selection.
    Returns (predicted_class, confidence, top3_predictions) like real model.
    """
    # Add slight delay to simulate model processing
    time.sleep(random.uniform(0.3, 1.0))
    
    # Try to guess plant type from filename
    filename_lower = image_filename.lower() if image_filename else ""
    
    # More aggressive filename detection
    plant_type = 'default'
    if any(word in filename_lower for word in ['apple', 'appl']):
        plant_type = 'apple'
    elif any(word in filename_lower for word in ['tomato', 'tomat', 'tom']):
        plant_type = 'tomato'
    elif any(word in filename_lower for word in ['potato', 'potat', 'pot']):
        plant_type = 'potato'
    elif any(word in filename_lower for word in ['corn', 'maize', 'mai']):
        plant_type = 'corn'
    elif any(word in filename_lower for word in ['pepper', 'bell', 'pep']):
        plant_type = 'pepper'
    else:
        # If no filename clues, randomly pick a plant type for variety
        plant_types = ['apple', 'tomato', 'potato', 'corn']
        plant_type = random.choice(plant_types)
    
    # Get predictions for this plant type
    available_predictions = DEMO_PREDICTIONS.get(plant_type, DEMO_PREDICTIONS['default'])
    
    # Weighted selection - prefer diseases over healthy (more interesting for demo)
    weighted_predictions = []
    for pred in available_predictions:
        if 'healthy' in pred[0].lower():
            # Add healthy predictions once
            weighted_predictions.append(pred)
        else:
            # Add disease predictions multiple times for higher chance
            weighted_predictions.extend([pred] * 3)
    
    # Randomly select primary prediction
    primary_pred = random.choice(weighted_predictions)
    predicted_class = primary_pred[0]
    base_confidence = primary_pred[1]
    
    # Add random variation to confidence
    confidence_variation = random.uniform(-8, 8)
    confidence = max(65, min(95, base_confidence + confidence_variation))
    
    # Generate top 3 predictions
    top3_predictions = []
    used_classes = set()
    
    # Primary prediction
    top3_predictions.append({
        'class': predicted_class,
        'confidence': round(confidence, 2)
    })
    used_classes.add(predicted_class)
    
    # Get all possible predictions for variety
    all_preds = []
    for pred_list in DEMO_PREDICTIONS.values():
        all_preds.extend(pred_list)
    
    # Remove duplicates and used classes
    remaining_preds = [p for p in all_preds if p[0] not in used_classes]
    
    # Add 2 more random predictions with decreasing confidence
    for i in range(min(2, len(remaining_preds))):
        pred = random.choice(remaining_preds)
        remaining_preds.remove(pred)
        
        # Make confidence significantly lower than primary
        confidence_drop = random.uniform(15, 30) + (i * 10)
        demo_confidence = max(8, confidence - confidence_drop)
        
        top3_predictions.append({
            'class': pred[0],
            'confidence': round(demo_confidence, 2)
        })
    
    return predicted_class, confidence, top3_predictions

def is_demo_mode():
    """Check if we're in demo mode (no real model available)"""
    return True  # Always return True for deployment demo
