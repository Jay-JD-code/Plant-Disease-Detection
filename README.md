# 🌱 Plant Disease Detection System

A comprehensive AI-powered web application for detecting plant diseases using deep learning. Built with Flask, PyTorch, and EfficientNet, this system can identify 23 different plant conditions across 5 species.

![Plant Disease Detection](https://img.shields.io/badge/AI-Plant%20Disease%20Detection-green) ![Python](https://img.shields.io/badge/Python-3.8+-blue) ![PyTorch](https://img.shields.io/badge/PyTorch-1.9+-red) ![Flask](https://img.shields.io/badge/Flask-Web%20App-lightgrey)

## 🌱 Features

- **AI-Powered Detection**: EfficientNet-B0 model trained for high accuracy plant disease classification
- **37 Plant Conditions**: Supports 23 disease classes, 13 healthy plant classes, and 1 background class
- **Modern Web Interface**: Responsive Flask web application with Bootstrap UI
- **Real-time Predictions**: Instant analysis with confidence scores and top-3 alternative predictions
- **Background Detection**: Special class for images without visible plant leaves
- **Comprehensive Analysis**: Jupyter notebook for confusion matrix and performance evaluation
- **Easy Deployment**: Simple setup and deployment process

## 🎯 Supported Plant Classes

### Plants Covered:
- **Apple**: Scab, Black rot, Cedar apple rust, Healthy
- **Blueberry**: Healthy
- **Cherry**: Powdery mildew, Healthy
- **Corn (Maize)**: Leaf spot, Common rust, Northern blight, Healthy
- **Grape**: Black rot, Esca, Leaf blight, Healthy
- **Orange**: Citrus greening
- **Peach**: Bacterial spot, Healthy
- **Pepper (Bell)**: Bacterial spot, Healthy
- **Potato**: Early blight, Late blight, Healthy
- **Squash**: Powdery mildew
- **Strawberry**: Leaf scorch, Healthy
- **Tomato**: Multiple diseases and healthy state
- **Background**: No leaves detected

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- (Optional) CUDA-compatible GPU for faster inference

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Plant-Disease-Detection-main
   ```

2. **Create virtual environment**
   ```bash
   python -m venv plant_disease_env
   
   # On Windows
   plant_disease_env\Scripts\activate
   
   # On Linux/Mac
   source plant_disease_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify model file**
   Ensure `best_plant_disease_model_90plus.pt` is in the project root directory.

### Running the Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Access the web interface**
   Open your browser and navigate to: `http://localhost:5000`

3. **Upload and analyze**
   - Upload a plant image (JPG, PNG, GIF, BMP)
   - View instant AI predictions with confidence scores
   - Get top-3 alternative predictions

## 📊 Model Evaluation

### Confusion Matrix Analysis

Run the Jupyter notebook for comprehensive model evaluation:

```bash
jupyter notebook confusion_matrix_analysis.ipynb
```

The notebook provides:
- Detailed confusion matrix visualization
- Per-class performance metrics
- Precision, recall, and F1-score analysis
- Background class performance evaluation
- Exportable results in CSV format

### Performance Metrics

- **Model Architecture**: EfficientNet-B0
- **Total Classes**: 37 (23 diseases + 13 healthy + 1 background)
- **Input Resolution**: 224x224 pixels
- **Model Size**: Optimized for deployment
- **Inference Time**: Real-time prediction capability

## 🏗️ Project Structure

```
Plant-Disease-Detection-main/
│
├── app.py                           # Main Flask application
├── best_plant_disease_model_90plus.pt # Trained EfficientNet model
├── requirements.txt                 # Python dependencies
├── README.md                       # Project documentation
├── confusion_matrix_analysis.ipynb # Model evaluation notebook
│
├── templates/                      # HTML templates
│   ├── base.html                  # Base template with navigation
│   ├── index.html                 # Upload page
│   ├── result.html                # Results display page
│   └── classes.html               # Classes information page
│
├── static/                        # Static files
│   ├── css/
│   │   └── style.css             # Custom CSS styling
│   └── js/
│       └── main.js               # JavaScript functionality
│
└── outputs/ (generated)           # Analysis outputs
    ├── plant_disease_performance_metrics.csv
    ├── confusion_matrix.csv
    ├── confusion_matrix_normalized.csv
    └── class_names.txt
```

## 🎨 Web Interface Features

### Upload Page
- Drag-and-drop file upload
- File validation (type and size)
- Image preview before analysis
- Loading animation during processing

### Results Page
- High-resolution image display
- Primary prediction with confidence score
- Visual confidence indicator (progress bar)
- Top-3 alternative predictions
- Disease information and recommendations
- Background detection alerts

### Classes Page
- Complete list of detectable conditions
- Search functionality
- Visual categorization (healthy/diseased/background)
- Performance statistics

## 🔧 API Endpoints

### Web Interface
- `GET /` - Main upload page
- `POST /predict` - Image upload and prediction
- `GET /classes` - View all supported classes

### API Endpoints
- `POST /api/predict` - JSON API for predictions

**Example API Usage:**
```python
import requests

with open('plant_image.jpg', 'rb') as f:
    response = requests.post(
        'http://localhost:5000/api/predict',
        files={'file': f}
    )
    
result = response.json()
print(f"Predicted: {result['predicted_class']}")
print(f"Confidence: {result['confidence']}%")
```

## 🔬 Model Details

### Architecture
- **Base Model**: EfficientNet-B0
- **Input Size**: 224 × 224 × 3
- **Output Classes**: 37
- **Activation**: Softmax for probability distribution

### Preprocessing
- Resize to 224×224 pixels
- Normalization: ImageNet statistics
- RGB color space

### Training Features
- Data augmentation for better generalization
- Transfer learning from ImageNet
- Custom classification head for plant diseases
- Background class for non-leaf images

## 🚀 Deployment Options

### Local Deployment
Use the provided Flask development server for testing and local use.

### Production Deployment
For production use, consider:

1. **Gunicorn WSGI Server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

2. **Docker Container**
   ```dockerfile
   FROM python:3.9-slim
   COPY . /app
   WORKDIR /app
   RUN pip install -r requirements.txt
   EXPOSE 5000
   CMD ["python", "app.py"]
   ```

3. **Cloud Platforms**
   - AWS EC2/Elastic Beanstalk
   - Google Cloud Run
   - Azure App Service
   - Heroku

## 📈 Model Performance

### Expected Performance Metrics
- **Overall Accuracy**: 90%+ (model name suggests 90+ accuracy)
- **Background Detection**: High precision for non-leaf images
- **Disease Classification**: Robust across multiple plant species
- **False Positive Rate**: Low for critical disease detection

### Evaluation Metrics
- Precision, Recall, F1-Score per class
- Confusion matrix analysis
- ROC curves and AUC scores
- Cross-validation performance

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/improvement`)
5. Create Pull Request

### Development Setup
```bash
# Install development dependencies
pip install -r requirements.txt
pip install pytest black flake8

# Run tests
pytest

# Format code
black .

# Lint code
flake8 .
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- EfficientNet architecture by Google Research
- PyTorch deep learning framework
- Flask web framework
- Bootstrap for responsive UI design
- Plant disease datasets used for training

## 📞 Support

For questions, issues, or contributions:

1. **Issues**: Use GitHub Issues for bug reports and feature requests
2. **Documentation**: Check this README and code comments
3. **Community**: Join discussions in the repository

## 🔄 Version History

- **v1.0.0** - Initial release with 37-class detection
- **v1.1.0** - Added background class detection
- **v1.2.0** - Enhanced web interface and API endpoints
- **v1.3.0** - Comprehensive evaluation notebook and metrics

---

**Made with ❤️ for sustainable agriculture and plant health monitoring**
