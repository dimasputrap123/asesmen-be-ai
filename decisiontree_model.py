import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

# import dataset
file_path = 'dataset.csv'
data = pd.read_csv(file_path)
data.columns = data.columns.str.strip()

# ubah kolom pendapatan ke string
tmp = []
for item in data['pendapatan']:
  if item < 1000000:
    txt = 'dibawah 1jt'
  elif item >= 1000000 and item < 5000000:
    txt = 'antara 1jt dan dibawah 5jt'
  elif item >= 5000000 and item < 10000000:
    txt = 'antara 5jt dan dibawah 10jt'
  else:
    txt = 'minimal 10jt'
  tmp.append(txt)

data['pendapatan'] = tmp 

# encode kolom yang mengandung string ke numerik
column_encoder=['kondisi_rumah','pendapatan','sumber_air_minum','akses_listrik','kepemilikan_aset','pekerjaan','status_kepemilikan_rumah','kategori_asesmen','rekomendasi_bantuan']
encoders = {}

for col in data.columns:
    if col in column_encoder:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])
        encoders[col] = le

with open("label_encoder.pkl", "wb") as filehandler:
    pickle.dump(encoders, filehandler)
    
# pisahkan kolom fitur dan label kategori_asesmen & rekomendasi_bantuan
x = data.drop(columns=['kategori_asesmen','rekomendasi_bantuan','skor_kemiskinan'])
y_kategori_asesmen = data['kategori_asesmen']
y_rekomendasi_bantuan = data['rekomendasi_bantuan']

# pisahkan data training dan data testing untuk label kategori_asesmen
X_train_ka, X_test_ka, y_train_ka, y_test_ka = train_test_split(x, y_kategori_asesmen, test_size=0.2, random_state=42)
model_kategori_asesmen = DecisionTreeClassifier(random_state=42)
model_kategori_asesmen.fit(X_train_ka, y_train_ka)

with open("model_kategori_asesmen.pkl", "wb") as filehandler:
    pickle.dump(model_kategori_asesmen, filehandler)

# pisahkan data training dan data testing untuk label kategori_asesmen
X_train_rb, X_test_rb, y_train_rb, y_test_rb = train_test_split(x, y_rekomendasi_bantuan, test_size=0.2, random_state=42)
model_rekomendasi_bantuan = DecisionTreeClassifier(random_state=42)
model_rekomendasi_bantuan.fit(X_train_rb, y_train_rb)

with open("model_rekomendasi_bantuan.pkl", "wb") as filehandler:
    pickle.dump(model_rekomendasi_bantuan, filehandler)

# hitung prediksi
y_pred_ka = model_kategori_asesmen.predict(X_test_ka)
y_pred_rb = model_rekomendasi_bantuan.predict(X_test_rb)

# metrik penilaian
accuracy_ka = accuracy_score(y_test_ka, y_pred_ka)
accuracy_rb = accuracy_score(y_test_rb, y_pred_rb)
classification_ka = classification_report(y_test_ka,y_pred_ka)
classification_rb = classification_report(y_test_rb,y_pred_rb)
confusion_matrix_ka = confusion_matrix(y_test_ka,y_pred_ka)
confusion_matrix_rb = confusion_matrix(y_test_rb,y_pred_rb)

print("Akurasi label kategori_asesmen:", accuracy_ka)
print("Akurasi label rekomendasi_bantuan:", accuracy_rb)
print("classification report label kategori_asesmen:", classification_ka)
print("classification report label rekomendasi_bantuan:", classification_rb)
print("confusion matrix label kategori_asesmen:", confusion_matrix_ka)
print("confusion matrix label rekomendasi_bantuan:", confusion_matrix_rb)

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
    
    # Prediksi kategori_asesmen
    pred_kategori_asesmen = model_kategori_asesmen.predict(input_df)[0]
    
    # Prediksi rekomendasi_bantuan
    pred_rekomendasi_bantuan = model_rekomendasi_bantuan.predict(input_df)[0]
    
    return {
        'kategori_asesmen': encoders['kategori_asesmen'].inverse_transform([pred_kategori_asesmen])[0],
        'rekomendasi_bantuan': encoders['rekomendasi_bantuan'].inverse_transform([pred_rekomendasi_bantuan])[0]
    }

user_input = {
    'anggota_kk': 1,
    'pendapatan': 1,
    'kondisi_rumah': 2,
    'sumber_air_minum': 1,
    'akses_listrik': 2,
    'kepemilikan_aset': 1,
    'pekerjaan': 2,
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