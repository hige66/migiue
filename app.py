import streamlit as st
from PIL import Image

st.title("画像右上4分の1切り取りアプリ")

uploaded_file = st.file_uploader("画像をアップロードしてください", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="アップロードされた画像", use_column_width=True)

    # 画像サイズ取得
    width, height = image.size
    left = width // 2
    upper = 0
    right = width
    lower = height // 2

    # 右上4分の1を切り取り
    cropped_image = image.crop((left, upper, right, lower))
    st.image(cropped_image, caption="右上4分の1の切り取り結果", use_column_width=True)

    # ダウンロードリンク
    st.download_button("切り取った画像をダウンロード", cropped_image.tobytes(), "cropped_image.png", "image/png")
