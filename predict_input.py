import pandas as pd
import pickle

def predict_asesmen_rekomendasi(input_data):
    """
    Fungsi untuk memprediksi kategori_asesmen dan rekomendasi_bantuan berdasarkan input pengguna.

    Parameters:
        input_data (dict): Data input dari pengguna dalam bentuk dictionary.

    Returns:
        dict: Prediksi kategori_asesmen dan rekomendasi_bantuan.
    """
    # Konversi input pengguna ke DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Memuat model kategori asesmen dengan pickle
    with open('model_kategori_asesmen.pkl', 'rb') as file:
        model_kategori_asesmen = pickle.load(file)
    
    # Memuat model rekomendasi bantuan dengan pickle
    with open('model_rekomendasi_bantuan.pkl', 'rb') as file:
        model_rekomendasi_bantuan = pickle.load(file)
    
    # Prediksi kategori_asesmen
    pred_kategori_asesmen = model_kategori_asesmen.predict(input_df)[0]
    
    # Prediksi rekomendasi_bantuan
    pred_rekomendasi_bantuan = model_rekomendasi_bantuan.predict(input_df)[0]
    
    # Memuat LabelEncoder dengan pickle
    with open('label_encoder.pkl', 'rb') as file:
        encoders = pickle.load(file)
    
    return {
        'kategori_asesmen': encoders['kategori_asesmen'].inverse_transform([pred_kategori_asesmen])[0],
        'rekomendasi_bantuan': encoders['rekomendasi_bantuan'].inverse_transform([pred_rekomendasi_bantuan])[0]
    }

user_input = {
    'anggota_kk': 4,
    'pendapatan': 1,
    'kondisi_rumah': 1,
    'sumber_air_minum': 1,
    'akses_listrik': 2,
    'kepemilikan_aset': 1,
    'pekerjaan': 3,
    'status_kepemilikan_rumah': 0,
    'penghasilan_dibawah_ump': 0,
    'aset_produktif': 1,
    'akses_pendidikan': 0,
    'akses_kesehatan': 0,
    'akses_sanitasi': 1,
    'akses_listrik_ump': 1,
    'rumah_tidak_layak_huni': 1,
}

# Prediksi hasil
hasil_prediksi = predict_asesmen_rekomendasi(user_input)
print("Hasil Prediksi:")
print("Kategori Asesmen:", hasil_prediksi['kategori_asesmen'])
print("Rekomendasi Bantuan:", hasil_prediksi['rekomendasi_bantuan'])