import streamlit as st
from handwritten_text_recognition import HandwrittenTextRecognition

def handwritten_to_word(image_path):
    htr_model = HandwrittenTextRecognition()
    recognized_text = htr_model.recognize(image_path)
    return recognized_text

def main():
    st.title("Handwritten Text Recognition")

    uploaded_file = st.file_uploader("Upload handwritten image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Convert handwritten text to Word document on button click
        if st.button("Recognize Text"):
            recognized_text = handwritten_to_word(uploaded_file)
            st.write("Recognized Text:")
            st.write(recognized_text)

if __name__ == "__main__":
    main()
