import streamlit as st

import recognition as rg

uploaded_file = st.file_uploader("Escolha uma foto", ["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = uploaded_file

    with st.spinner('Verificando...'):
        response = rg.recognize(image)
        if(response):
            st.balloons()
            st.success("É um gato 🐱")
        else:
            st.error("Não é um gato 😔")
