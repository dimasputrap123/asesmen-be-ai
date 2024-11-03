import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
# from sklearn.metrics import accuracy_score,classification_report
import pickle

file_path = 'dataset.csv'
data = pd.read_csv(file_path)
data.columns = data.columns.str.strip()

column_encoder=['kondisi_rumah','sumber_air_minum','akses_listrik','kepemilikan_aset','pekerjaan','status_kepemilikan_rumah','kategori_asesmen','rekomendasi_bantuan']
encoders = {}

for col in data.columns:
    if col in column_encoder:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])
        encoders[col] = le

with open("label_encoder.pkl", "wb") as filehandler:
    pickle.dump(encoders, filehandler)
    

x = data.drop(['rekomendasi_bantuan'], axis=1)
y = data['rekomendasi_bantuan']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

modelnb = BernoulliNB(alpha=1.0)
nbtrain = modelnb.fit(x_train, y_train)

with open("model.pkl", "wb") as filehandler:
    pickle.dump(modelnb, filehandler)

# y_pred = nbtrain.predict(x_test)
# accuracy = accuracy_score(y_test, y_pred)
# classification_rep = classification_report(y_test, y_pred)

# print(accuracy)