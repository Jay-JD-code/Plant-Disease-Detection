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
        ('Apple___healthy', 95.2),
        ('Apple___Cedar_apple_rust', 68.9)
    ],
    'tomato': [
        ('Tomato_Early_blight', 89.1),
        ('Tomato_Bacterial_spot', 76.8),
        ('Tomato_healthy', 92.4),
        ('Tomato_Late_blight', 84.2)
    ],
    'potato': [
        ('Potato___Early_blight', 81.3),
        ('Potato___Late_blight', 77.9),
        ('Potato___healthy', 88.7)
    ],
    'corn': [
        ('Corn_(maize)___Common_rust_', 79.4),
        ('Corn_(maize)___Northern_Leaf_Blight', 73.2),
        ('Corn_(maize)___healthy', 91.8)
    ],
    'default': [
        ('Apple___healthy', 85.3),
        ('Tomato_healthy', 82.1),
        ('Potato___healthy', 87.9)
    ]
}

def demo_predict_disease(image_filename):
    """
    Generate demo prediction based on filename or random selection.
    Returns (predicted_class, confidence, top3_predictions) like real model.
    """
    # Add slight delay to simulate model processing
    time.sleep(random.uniform(0.5, 1.5))
    
    # Try to guess plant type from filename
    filename_lower = image_filename.lower() if image_filename else ""
    
    if 'apple' in filename_lower:
        plant_type = 'apple'
    elif 'tomato' in filename_lower:
        plant_type = 'tomato'
    elif 'potato' in filename_lower:
        plant_type = 'potato'
    elif 'corn' in filename_lower or 'maize' in filename_lower:
        plant_type = 'corn'
    else:
        plant_type = 'default'
    
    # Get predictions for this plant type
    available_predictions = DEMO_PREDICTIONS[plant_type]
    
    # Randomly select primary prediction and add some noise
    primary_pred = random.choice(available_predictions)
    predicted_class = primary_pred[0]
    base_confidence = primary_pred[1]
    
    # Add random variation to confidence
    confidence_variation = random.uniform(-5, 5)
    confidence = max(60, min(98, base_confidence + confidence_variation))
    
    # Generate top 3 predictions
    top3_predictions = []
    used_classes = set()
    
    # Primary prediction
    top3_predictions.append({
        'class': predicted_class,
        'confidence': round(confidence, 2)
    })
    used_classes.add(predicted_class)
    
    # Add 2 more random predictions with lower confidence
    remaining_preds = [p for p in available_predictions if p[0] not in used_classes]
    if len(remaining_preds) < 2:
        # Add from other categories if needed
        all_preds = [p for pred_list in DEMO_PREDICTIONS.values() for p in pred_list]
        remaining_preds.extend([p for p in all_preds if p[0] not in used_classes])
    
    for i in range(2):
        if remaining_preds:
            pred = random.choice(remaining_preds)
            remaining_preds.remove(pred)
            
            # Make confidence lower than primary
            demo_confidence = max(10, min(confidence - 10 - i*5, pred[1] + random.uniform(-10, 5)))
            
            top3_predictions.append({
                'class': pred[0],
                'confidence': round(demo_confidence, 2)
            })
    
    return predicted_class, confidence, top3_predictions

def is_demo_mode():
    """Check if we're in demo mode (no real model available)"""
    return True  # Always return True for deployment demo
