import base64

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
            gif = open('cheers.gif', 'rb')
            contents = gif.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            gif.close()

            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,
            )
        else:
            st.error("Não é um gato 😔")
