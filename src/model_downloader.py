"""
Model downloader for deployment environments.
Downloads model from external storage (Google Drive, Dropbox, etc.) if not present locally.
"""
import os
import urllib.request
import ssl

def download_model_from_url(url, local_path):
    """Download model from external URL"""
    try:
        # Create SSL context that doesn't verify certificates (for some cloud services)
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        
        print(f"Downloading model from {url[:50]}...")
        urllib.request.urlretrieve(url, local_path)
        print(f"✅ Model downloaded to {local_path}")
        return True
    except Exception as e:
        print(f"❌ Failed to download model: {e}")
        return False

def ensure_model_exists():
    """Ensure model file exists, download if necessary"""
    model_files = [
        'balanced_plant_disease_model.pt',
        'best_plant_disease_model_90plus.pt'
    ]
    
    # Check if any model exists locally
    for model_file in model_files:
        if os.path.exists(model_file):
            print(f"✅ Found local model: {model_file}")
            return True
    
    # If no local model, try to download
    # YOU NEED TO UPLOAD YOUR MODEL TO A PUBLIC URL AND REPLACE THIS
    model_urls = {
        'balanced_plant_disease_model.pt': 'YOUR_GOOGLE_DRIVE_OR_DROPBOX_DIRECT_LINK_HERE',
        # Example: 'https://drive.google.com/uc?export=download&id=YOUR_FILE_ID'
        # Or use GitHub Releases, Dropbox, etc.
    }
    
    for model_file, url in model_urls.items():
        if url != 'YOUR_GOOGLE_DRIVE_OR_DROPBOX_DIRECT_LINK_HERE':
            if download_model_from_url(url, model_file):
                return True
    
    print("⚠️ No model found locally and no valid download URL configured")
    return False
