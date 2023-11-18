from google.cloud import vision_v1p2beta1 as vision 
from google.oauth2 import service_account
import streamlit as st
from PIL import Image 
import io
# import os
def detect_logo(image_path):
    # keypath = os.path.join('D:','codes','LogoDetection','logo-detection-system-811c426b1dea.json')
    keypath = 'logo-detection-system.json'
    credentials = service_account.Credentials.from_service_account_file(keypath)
    client = vision.ImageAnnotatorClient(credentials=credentials)
    
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
        
        image = vision.Image(content = content)
        response = client.logo_detection(image=image)
        logos = response.logo_annotations 
        
        if logos:
            st.write("Logos detected: ")
            for logo in logos:
                st.write(f"Logo: {logo.description}, Score: {logo.score}")
        
        else:
            st.write("No logos Detected")

picture = st.camera_input("Take a Photo")
imageWidget = st.image(picture)
if st.button("Capture"):
    # tempImage = imageWidget
    tempImagePath = "captured_image.jpg"
    image_data = picture.getvalue()
    with open(tempImagePath, 'wb') as f:
        f.write(image_data)
    # image = Image.open('tempImagePath')
    # image.save(tempImagePath)
    st.success("Saved Image")
    
if st.button("Detect Logo"):
    detect_logo("captured_image.jpg")
# detect_logo('D:/codes/LogoDetection/McD.jpg')