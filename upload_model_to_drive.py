#!/usr/bin/env python3
"""
Script to upload model files to Google Drive for external hosting in deployment.
This allows Vercel to download models at runtime instead of including them in the build.
"""

def upload_models_to_google_drive():
    """
    Instructions for uploading models to Google Drive for external hosting:
    
    1. Go to https://drive.google.com
    2. Upload your model files:
       - balanced_plant_disease_model.pt (18.6MB)
       - best_plant_disease_model_90plus.pt (18.6MB)
    
    3. For each file:
       - Right-click → Share
       - Change to "Anyone with the link can view"
       - Copy the share link
    
    4. Convert share links to direct download links:
       Original: https://drive.google.com/file/d/FILE_ID/view?usp=sharing
       Direct:   https://drive.google.com/uc?export=download&id=FILE_ID
    
    5. Update the URLs in src/model_downloader.py
    
    Example:
    If your share link is:
    https://drive.google.com/file/d/1ABC123XYZ456/view?usp=sharing
    
    Your direct download link is:
    https://drive.google.com/uc?export=download&id=1ABC123XYZ456
    """
    
    print("📋 Instructions for Manual Upload:")
    print("1. Go to https://drive.google.com")
    print("2. Upload these files:")
    print("   - balanced_plant_disease_model.pt")
    print("   - best_plant_disease_model_90plus.pt")
    print("3. Share each file publicly")
    print("4. Get direct download links")
    print("5. Update model_downloader.py with the URLs")
    print("\n🔗 Direct link format:")
    print("https://drive.google.com/uc?export=download&id=YOUR_FILE_ID")

if __name__ == "__main__":
    upload_models_to_google_drive()
