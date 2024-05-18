import streamlit as st
import easyocr
from PIL import Image
import numpy as np

# Initialize the OCR reader
reader = easyocr.Reader(['en'])

def ocr_image(image):
    # Convert PIL image to numpy array
    image_np = np.array(image)
    # Perform OCR
    results = reader.readtext(image_np)
    # Extract and concatenate recognized text
    recognized_text = ' '.join([result[1] for result in results])
    return recognized_text

def main():
    st.title("Handwritten Text Recognition with EasyOCR")

    uploaded_file = st.file_uploader("Upload handwritten image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Recognize Text"):
            recognized_text = ocr_image(image)
            st.write("Recognized Text:")
            st.write(recognized_text)

if __name__ == "__main__":
    main()
