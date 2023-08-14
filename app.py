import streamlit as st
from rembg import remove
from PIL import Image
from streamlit_image_comparison import image_comparison
import easyocr as ocr   # OCR
import numpy as np

# set page config
st.set_page_config(page_title="My_first_Image_App", layout="centered")
st.subheader('[미니프로젝트] 이미지 배경제거 + 글자추출 웹서비스')
st.markdown('### :sunglasses: Remove Background - `rembg`')      # : : 사이에 이모지 적어주면 됨  # 이모지 참고) https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.markdown("#### sample result")

uploaded_file = st.file_uploader("이미지를 업로드하세요", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    input = Image.open(uploaded_file)
    st.image(input, caption='원본 이미지', use_column_width=True)
    output = remove(input)
    st.image(output, caption='배경 제거 이미지', use_column_width=True)


image_comparison(
    img1="image1.jpg",
    img2="image2.jpg",
    label1="text1",
    label2="text1",
    width=700,
    starting_position=50,
    show_labels=True,
    make_responsive=True,
    in_memory=True,
)
