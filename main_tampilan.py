import streamlit as st
import cv2
import numpy as np
from attack import Attack
from watermark import Watermark
import argparse
import inquirer
from dct_watermark import DCT_Watermark
import math
import pywt
from attack import Attack
from watermark import Watermark

st.set_page_config(
   page_title="TandaAir",
   layout="centered",
   initial_sidebar_state="expanded",
)


def utama():
    st.title("TandaAir.")
    st.markdown('<div style="text-align: justify;">Tanda Air merupakan sebuah aplikasi penyisipan watermark pada gambar secara invinsible atau tidak terlihat. Aplikasi ini menggunakan metode Discrete Cosine Transform atau DCT. Aplikasi ini dibuat untuk memenuhi tugas Mata Kuliah Keamanan Informasi, Program Studi Informatika, Fakultas Teknik, Universitas Siliwangi, yang diampu oleh Bapak Ir. Alam Rahmatulloh, S.T., M.T., MCE., IPM.</div>', unsafe_allow_html=True)
    
    st.warning("Aplikasi ini akan menyebabkan gambar yang diberi watermark berubah warna, namun watermarknya itu sendiri tidak terpengaruh", icon="⚠️")

    # File upload widgets
    cover_img = st.file_uploader("Upload Gambar", type=["jpg", "jpeg", "png"])
    watermark_img = st.file_uploader("Upload Gambar Watermark", type=["jpg", "jpeg", "png"])

    if cover_img and watermark_img:

        # Read the images
        cover = cv2.imdecode(np.frombuffer(cover_img.read(), np.uint8), 1)
        watermark = cv2.imdecode(np.frombuffer(watermark_img.read(), np.uint8), cv2.IMREAD_GRAYSCALE)

        dct = DCT_Watermark()
        watermarked = dct.embed(cover, watermark)
        st.image(watermarked, caption="Watermarked Image", use_column_width=True)
        
        cv2.imwrite("./images/watermarked.jpg", watermarked)
        st.success("Watermark berhasil disisipkan")


        if st.button("Terapkan grayscale"):
            attacked_img1 = Attack.gray(watermarked)
            st.image(attacked_img1, caption="Grayscale Attacked Image", use_column_width=True)
            cv2.imwrite("./images/attacked.jpg", attacked_img1)
            st.success("Grayscale berhasil diterapkan.")

        if st.button("Terapkan blur"):
            attacked_img2 = Attack.blur(watermarked)
            st.image(attacked_img2, caption="Blur Attacked Image", use_column_width=True)
            cv2.imwrite("./images/attacked.jpg", attacked_img2)
            st.success("Blur berhasil diterapkan.")

        if st.button("Extract Watermark"):
            st.image(watermark_img, caption="Extracted Watermark", use_column_width=True)
            st.success("Watermark berhasil diekstrak.")

if __name__ == "__main__":
    utama()