# Requirements:
# pip install streamlit pillow pytesseract
# Also install Tesseract OCR separately (Windows: UB-Mannheim installer)

import streamlit as st
from PIL import Image
import pytesseract
import os
import time

st.set_page_config(page_title = "Screenshot --> Text", page_icon = "📷", layout = "wide")
st.title("Automatic Screenshot-to-Text convertor📝")

image_files = [f for f in os.listdir() if f.lower().endswith(('.png', '.jpg','.jpeg'))]

if not image_files:
    st.warning("No image files were found!")
else:
    st.success(f"Found {len(image_files)} images. Processing the images...⚙️")
    with st.spinner('Loading data...'): 
        time.sleep(2)
    for img_file in image_files:
        st.subheader(f"Image: {img_file}")
        img = Image.open(img_file)
        st.image(img, width = 400)
        text = pytesseract.image_to_string(img).strip()
        st.subheader("Extracted text: ")
        if text == "" or text == "\x0c":   # \x0c = form feed (Tesseract empty output)
            st.info("No readable text/no text present in the image.")
        else:
            st.text_area("", text, height = 200)
        st.markdown("---")
