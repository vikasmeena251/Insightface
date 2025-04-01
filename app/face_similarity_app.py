# face_similarity_app.py

import streamlit as st
import cv2
import numpy as np
from insightface.app import FaceAnalysis
from PIL import Image
from numpy.linalg import norm

# Set Streamlit page config
st.set_page_config(page_title="Face Similarity Checker", layout="centered")
st.title("🧠 Face Similarity Checker using InsightFace")

# Load InsightFace model
@st.cache_resource
def load_model():
    app = FaceAnalysis(name='buffalo_l')
    app.prepare(ctx_id=-1)  # -1 to run on CPU
    return app

face_app = load_model()

# Main app logic
def main():
    st.markdown("Upload two face images below to calculate similarity score:")

    # Upload columns
    col1, col2 = st.columns(2)
    with col1:
        uploaded_file1 = st.file_uploader("Upload First Face Image", type=["jpg", "jpeg", "png"])
    with col2:
        uploaded_file2 = st.file_uploader("Upload Second Face Image", type=["jpg", "jpeg", "png"])

    if uploaded_file1 and uploaded_file2:
        try:
            img1 = np.array(Image.open(uploaded_file1).convert("RGB"))
            img2 = np.array(Image.open(uploaded_file2).convert("RGB"))

            faces1 = face_app.get(img1)
            faces2 = face_app.get(img2)

            if len(faces1) == 0 or len(faces2) == 0:
                st.error("No faces detected in one or both images.")
                return

            emb1 = faces1[0].embedding
            emb2 = faces2[0].embedding

            cos_sim = np.dot(emb1, emb2) / (norm(emb1) * norm(emb2))
            similarity_percent = round(cos_sim * 100, 2)

            st.success(f"✅ Face similarity score: **{similarity_percent}%**")
            st.image([img1, img2], caption=["Face 1", "Face 2"], width=300)

        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")

if __name__ == "__main__":
    main()
