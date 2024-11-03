import random
import string
from faker import Faker
from datetime import datetime
import pandas as pd

# Inisialisasi Faker untuk data acak
fake = Faker('id_ID')  # Menggunakan bahasa Indonesia untuk data lokal

def generate_nik():
    # Format NIK: 16 digit angka
    return ''.join(random.choices(string.digits, k=16))

def generate_nokk():
    # Format No. KK: 16 digit angka
    return ''.join(random.choices(string.digits, k=16))

def generate_data(num_records=10):
    data = []
    for i in range(1, num_records + 1):
        nik = generate_nik()
        nokk = generate_nokk()
        nama = fake.name()
        alamat = fake.address()
        status = 0  # Nilai default untuk kolom status
        created_at = updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        data.append({
            "id": i,
            "nik": nik,
            "nokk": nokk,
            "nama": nama,
            "alamat": alamat,
            "status": status,
        })
    return data

# Generate data dan tampilkan hasilnya
data = generate_data()
for record in data:
    print(record)

df = pd.DataFrame(data)
df.to_csv('bnba.csv')