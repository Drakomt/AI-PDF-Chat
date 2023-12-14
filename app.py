import streamlit as st

st.set_page_config(layout="wide")

st.title("AI-PDF-Chat")

uploaded_pdf = st.file_uploader("Upload your PDF file", type=['pdf'])

if uploaded_pdf is not None:
    col1, col2 , col3 = st.columns([2,1,1])

    with col1:
        pass