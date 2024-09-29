import streamlit as st
from PIL import Image
import pytesseract
import cv2
import numpy as np

# Set the path to Tesseract (required for Windows users)
#pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'  # Update this path if necessary

# Function to preprocess the image (grayscale and thresholding)
def preprocess_image(image):
    # Convert PIL image to OpenCV format
    open_cv_image = np.array(image.convert('RGB'))
    img = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to improve OCR
    _, threshold_img = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    # Convert back to PIL image
    processed_image = Image.fromarray(threshold_img)
    
    return processed_image

# Function to perform OCR on the image
def extract_text(image):
    # Preprocess the image
    processed_image = preprocess_image(image)
    
    # Extract text using Tesseract
    extracted_text = pytesseract.image_to_string(processed_image, config='--psm 6', lang='eng+hin')
    
    return extracted_text

# Streamlit Web App
st.title("OCR for Hindi and English Text with Keyword Search")

# Image uploader widget
uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Open and display the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Perform OCR on the uploaded image
    with st.spinner("Extracting text..."):
        extracted_text = extract_text(image)
    
    # Display extracted text
    if extracted_text:
        st.subheader("Extracted Text")
        st.text_area("Text", value=extracted_text, height=250)
    
    # Keyword search input
    keyword = st.text_input("Enter keyword to search in the text:")
    
    # Perform keyword search and highlight matching sections
    if keyword:
        highlighted_text = extracted_text.replace(keyword, f"**{keyword}**")
        st.subheader(f"Search Results for '{keyword}'")
        st.markdown(highlighted_text)
