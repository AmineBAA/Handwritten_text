import streamlit as st
from PIL import Image
import pytesseract
import numpy as np

# Path to the tesseract executable
# Uncomment and set the path if tesseract is not in your PATH environment variable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# For Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# For macOS/Linux, if necessary, specify the path:
# pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'


def ocr_image(image):
    # Convert the image to a numpy array
    image_np = np.array(image)
    # Perform OCR using Tesseract
    recognized_text = pytesseract.image_to_string(image_np)
    return recognized_text

def main():
    st.title("Handwritten Text Recognition with Tesseract OCR")

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
