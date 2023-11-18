from google.cloud import vision_v1p2beta1 as vision 
from google.oauth2 import service_account
# import os
def detect_logo(file_path):
    # keypath = os.path.join('D:','codes','LogoDetection','logo-detection-system-811c426b1dea.json')
    keypath = 'logo-detection-system.json'
    credentials = service_account.Credentials.from_service_account_file(keypath)
    client = vision.ImageAnnotatorClient(credentials=credentials)
    
    with open(file_path, 'rb') as image_file:
        content = image_file.read()
        
        image = vision.Image(content = content)
        response = client.logo_detection(image=image)
        logos = response.logo_annotations 
        
        if logos:
            print("Logos detected: ")
            for logo in logos:
                print(f"Logo: {logo.description}, Score: {logo.score}")
        
        else:
            print("No logos Detected")
            
# My_api_key = "AIzaSyAu0whNgg3KE0ifp4nT4jfPe3Cd7Ui9D54"
detect_logo('kfc.png')
# detect_logo('D:/codes/LogoDetection/McD.jpg')