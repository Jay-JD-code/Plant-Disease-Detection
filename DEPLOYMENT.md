# Plant Disease Detection - Deployment Guide

This guide helps you deploy the Plant Disease Detection application to various cloud platforms.

## 🚨 Important Note About Model Files

The trained model files (`balanced_plant_disease_model.pt` and `best_plant_disease_model_90plus.pt`) are **18.6 MB each** and may exceed size limits on some free deployment platforms.

### Current Status
- **Model files are too large** for some deployment platforms
- **Demo mode is enabled** as fallback when models can't be loaded
- Demo mode provides realistic predictions based on filename patterns

## 🎯 Quick Deployment Solutions

### Option 1: Vercel Deployment (Recommended)

1. **Fork the repository** on GitHub
2. **Sign up for Vercel** at https://vercel.com
3. **Import the project** from GitHub
4. **Use the included `vercel.json` configuration**

The app will automatically run in demo mode if model files can't be loaded.

### Option 2: Railway Deployment

1. Sign up at https://railway.app
2. Connect your GitHub repository
3. Railway will auto-detect the Flask app
4. Use the `wsgi.py` entry point

### Option 3: Render Deployment

1. Sign up at https://render.com
2. Create a new Web Service from GitHub
3. Use Python runtime
4. Build command: `pip install -r requirements-deploy.txt`
5. Start command: `python wsgi.py`

## 📁 Deployment Files Included

- `vercel.json` - Vercel configuration
- `wsgi.py` - WSGI entry point
- `Procfile` - Heroku configuration
- `runtime.txt` - Python version specification
- `requirements-deploy.txt` - Optimized dependencies

## 🎭 Demo Mode

When model files cannot be loaded (due to size limitations), the app automatically falls back to **demo mode**:

- ✅ Provides realistic-looking predictions
- ✅ Uses filename patterns to guess plant types
- ✅ Includes all disease information and treatments
- ✅ Maintains the same user interface
- ✅ Shows confidence scores and top-3 predictions

**Demo predictions are for demonstration purposes only and not real AI analysis.**

## 🔧 For Production with Real Models

To deploy with actual model functionality:

### Option A: Use Model Hosting Service

1. Upload your `.pt` files to:
   - Google Drive (get public download link)
   - Dropbox (get direct link)
   - GitHub Releases
   - AWS S3 with public access

2. Update `src/model_downloader.py` with your download URLs

3. The app will automatically download models on startup

### Option B: Use Larger Deployment Platform

Deploy to platforms with higher size limits:
- **AWS EC2** - No size limits
- **Google Cloud Run** - Up to 10GB
- **Azure Container Instances** - Flexible sizing
- **DigitalOcean App Platform** - Up to 10GB

## 🚀 Local Testing Before Deployment

```bash
# Test the deployment configuration locally
python wsgi.py

# Test with demo mode
# (Models won't load, but app should run)
```

## 🌐 Environment Variables

Set these on your deployment platform:

```bash
FLASK_ENV=production
PORT=5000  # Will be set automatically by most platforms
```

## 📱 Live Demo

Once deployed, your app will have:
- Upload interface at `/`
- Classes list at `/classes`
- API endpoint at `/api/predict`

## 🆘 Troubleshooting Deployment

### 404 Error (NOT_FOUND)
- Check if `vercel.json` is configured correctly
- Verify the entry point in deployment settings
- Ensure `wsgi.py` is in the root directory

### App Crashes on Startup
- Check the deployment logs
- Verify all dependencies in `requirements-deploy.txt`
- Ensure Python version matches `runtime.txt`

### Model Loading Issues
- App will automatically fall back to demo mode
- Check logs for model loading messages
- Verify model files are accessible if using external hosting

## 📞 Support

If you encounter issues:
1. Check the deployment platform's logs
2. Verify all files are uploaded correctly
3. Test locally using `python wsgi.py`
4. The app should work in demo mode even without models

## 🎉 Success Checklist

- [ ] Repository is public and accessible
- [ ] Deployment configuration files are included
- [ ] App starts without errors (check logs)
- [ ] Homepage loads at deployed URL
- [ ] Upload functionality works (demo predictions)
- [ ] All templates and static files load correctly

Your Plant Disease Detection app should now be live and accessible! 🌱
