import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from preprocess import text_proses

# Inisialiasi App
app = Flask(__name__)

# Mengunggah Model
model_predict = load_model('fake_news_model')

# Route untuk mengecek apakah backend jalan atau tidak
@app.route('/')
def home():
    return '<h1> Backend Berjalan! </h1>'

# Route untuk melakukan prediksi
@app.route('/predict', methods=['POST'])
def news_predict():
    args = request.json

    # Memasukan parameter data inference
    data_inf = {
        'title': args.get('title'),
        'text': args.get('text')
    }

    # Melakukan printing jika data inference berhasil diambil dari frontend
    print('[DEBUG] Data Inference : ', data_inf)
    
    # Transformasi data inference
    data_inf = pd.DataFrame([data_inf])
    data_inf['feature'] = data_inf['title'] + ' ' + data_inf['text']
    data_inf.drop('title', axis=1, inplace=True)
    data_inf.drop('text', axis=1, inplace=True)
    data_inf_pro = data_inf['feature'].apply(lambda x: text_proses(x))
    y_pred_inf = model_predict.predict(data_inf_pro)
    y_pred_inf = np.where(y_pred_inf >= 0.5, 1, 0)

    # Membuat fungsi if untuk respon, 0 = customer tidak meninggalkan jasa
    # 1 = customer meninggalkan jasa

    if y_pred_inf == 0:
        label = 'The news is most likely fake'
    else:
        label = 'The news is most likely true'

    # Untuk melihat apakah inference berhasil di prediksi atau tidak
    print('[DEBUG] Result : ', y_pred_inf, label)
    print('')

    # Membuat fungsi untuk respon dari backend yang akan menampilkan hasil prediksi
    response = jsonify(
        result = str(y_pred_inf),
        label_names = label
    )

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)