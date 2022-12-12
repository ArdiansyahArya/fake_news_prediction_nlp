import streamlit as st
import pandas as pd
import requests
from PIL import Image


st.set_page_config(
    page_title="Fake News Prediction Model",
    layout='wide',
    initial_sidebar_state='expanded'
)

# Membuat fungsi untuk melakukan prediksi
def run():

    # Menggunakan Kolom untuk menengahkan text
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        # Membuat judul
        st.title('Fake News Prediction Model')
    
    with col3:
        st.write(' ')

    col4, col5, col6 = st.columns(3)

    with col4:
        st.write(' ')

    with col5:
        image = Image.open('Fake_News.jpg')
        st.image(image, caption='Fake News')
    
    with col6:
        st.write(' ')

    # Membuat form parameter
    with st.form(key='form_parameters'):
        title = st.text_input('News Title', max_chars=150, value='', help='Diiskan judul berita')
        text = st.text_area('News Text', height=30, max_chars=10000, value='', help='Di isikan teks dari berita')

        submitted = st.form_submit_button('Predict')
    
    # Membuat data baru
    data_inf = {
        'title': title,
        'text': text, 
    }
    
    # Membuat fungsi if untuk melakukan respon apabila tombol submit diklik
    if submitted:
        # Memperlihatkan dataframe inference
        st.dataframe(pd.DataFrame([data_inf]))
        print('[DEBUG] Data Inference : \n', data_inf)
        
        # Melakukan prediksi (URL tempat backend di deploy)
        URL = "http://125.164.17.106:8080/predict"
        r = requests.post(URL, json=data_inf)
        
        if r.status_code == 200:
            res = r.json()
            st.write('## Prediction : ', res['label_names'])
            print('[DEBUG] Result : ', res)
            print('')
        else:
            st.write('Error with status code ', str(r.status_code))
        

if __name__ == '__main__':
    run()