import pandas as pd
import numpy as np
import joblib
from flask import Flask, request, render_template
from pgmpy.inference import VariableElimination

# --- INITIALIZE & MODEL TOO ---

# FLASK INITIALIZE
app = Flask(__name__)

# LOAD MODEL AND PREPROCESS OBJECT
print("Memuat model dari 'model.joblib'...")
try:
    model_package = joblib.load('model.joblib')
    model = model_package['model']
    encoders = model_package['encoders']
    discretizer_bins = model_package['discretizer_bins']
    ALL_FEATURES = model_package['all_features']
    
    # INTERFACE Engine
    inference = VariableElimination(model)
    print("Model berhasil dimuat.")
except FileNotFoundError:
    print("ERROR: 'model.joblib' not found.")
    print("Harap jalankan 'train.py' terlebih dahulu untuk membuat file model.")
    exit()

# HELPER FUNCTION FOR PREDICT
def preprocess_input(form_data):
    """Mengubah input dari form HTML menjadi format yang bisa diterima model."""
    
    # 1. Buat dictionary untuk evidence
    evidence_dict = {}
    # 2. Buat daftar "alasan" risiko
    reasons = []

    # --- Proses Fitur Numerik (Diskretisasi) ---
    numeric_inputs = {
        'Age': int(form_data['Age']),
        'RestingBP': int(form_data['RestingBP']),
        'Cholesterol': int(form_data['Cholesterol']),
        'MaxHR': int(form_data['MaxHR']),
        'Oldpeak': float(form_data['Oldpeak']),
    }
    
    for col, value in numeric_inputs.items():
        bins, labels = discretizer_bins[col]
        # Bin yang sesuai untuk nilai input
        bin_index = pd.cut([value], bins=bins, labels=labels, right=False)[0]
        
        # Simpan sebagai string label (e.g., '>60')
        evidence_dict[col] = str(bin_index)
        
        # Logika sederhana untuk "alasan"
        if col == 'Age' and bin_index == '>60':
            reasons.append(f"Usia Lanjut ({value} tahun)")
        if col == 'Cholesterol' and bin_index in ['Borderline', 'High']:
            reasons.append(f"Kolesterol Tinggi ({value} mg/dl)")
        if col == 'RestingBP' and bin_index in ['High S1', 'High S2']:
            reasons.append(f"Tekanan Darah Tinggi ({value} mmHg)")
        if col == 'Oldpeak' and bin_index in ['Medium', 'High']:
            reasons.append(f"Depresi ST Tinggi ({value}) saat olahraga")

    # PROSES FITUR KATEGORIKAL DARI FORM
    categorical_inputs = {
        'Sex': form_data['Sex'],
        'ChestPainType': form_data['ChestPainType'],
        'FastingBS': str(form_data['FastingBS']), # sudah 0 atau 1
        'RestingECG': form_data['RestingECG'],
        'ExerciseAngina': form_data['ExerciseAngina'],
        'ST_Slope': form_data['ST_Slope'],
    }
    
    for col, value in categorical_inputs.items():
        evidence_dict[col] = value
        
        # Logika sederhana untuk "alasan"
        if col == 'ChestPainType' and value not in ['ATA', 'NAP']:
            reasons.append(f"Tipe Nyeri Dada ({value})")
        if col == 'ExerciseAngina' and value == 'Y':
            reasons.append("Angina saat Olahraga")
        if col == 'ST_Slope' and value == 'Flat':
            reasons.append("ST Slope 'Flat'")

    # --- ENCODER STRING TO NUMBER !!!!! ---
    # Ubah semua nilai string (e.g., '>60', 'ATA') menjadi angka (e.g., 2, 1)
    # Sesuai dengan yang dipelajari model saat training
    encoded_evidence = {}
    for col in ALL_FEATURES:
        try:
            # Ambil nilai string (e.g., '>60')
            raw_val = evidence_dict[col]
            # Ambil encoder yang sesuai
            le = encoders[col]
            # Ubah string tsb (e.g., '>60') menjadi angka (e.g., 2)
            # le.transform() butuh array
            encoded_val = le.transform([raw_val])[0]
            encoded_evidence[col] = encoded_val
        except Exception as e:
            print(f"Error encoding {col} dengan nilai {evidence_dict.get(col)}: {e}")
            # Jika ada nilai yang tidak dikenal, lewati
            pass
            
    return encoded_evidence, reasons


# --- APP ROUTE ---

@app.route('/')
def home():
    """Menampilkan halaman utama (index.html)."""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Menerima data form, memproses, dan mengembalikan prediksi."""
    try:
        # Ambil data dari form
        form_data = request.form

        # 1. Ubah input form menjadi evidence
        evidence, reasons = preprocess_input(form_data)
        
        # 2. Lakukan inference
        # Kita ingin tahu probabilitas HeartDisease=1 (Sakit)
        target_encoder = encoders['HeartDisease']
        target_value_index = int(target_encoder.transform(['1'])[0]) # Biasanya '1'

        print(f"Melakukan query dengan evidence: {evidence}")
        
        # Lakukan query ke Bayesian Network
        result_phi = inference.query(
            variables=['HeartDisease'],
            evidence=evidence
        )
        
        # Ambil nilai probabilitas untuk HeartDisease=1
        risk_probability = result_phi.values[target_value_index]
        risk_percentage = round(risk_probability * 100, 2)
        
        print(f"Hasil Probabilitas: {risk_probability} ({risk_percentage}%)")
        
        # Tentukan warna berdasarkan risiko
        if risk_percentage > 70:
            risk_color = "text-red-500"
        elif risk_percentage > 40:
            risk_color = "text-yellow-500"
        else:
            risk_color = "text-green-500"

        # Jika tidak ada alasan spesifik, beri pesan default
        if not reasons:
            reasons = ["Faktor risiko Anda terlihat terkendali."]

        # Kembalikan hasil ke halaman HTML
        return render_template('index.html',
                               risk=risk_percentage,
                               reasons=reasons,
                               risk_color=risk_color,
                               scroll_to='result') # Untuk auto-scroll

    except Exception as e:
        print(f"Terjadi error saat prediksi: {e}")
        # Jika error, kirim pesan error ke halaman
        return render_template('index.html',
                               error=f"Terjadi kesalahan: {e}. Pastikan semua input terisi.",
                               scroll_to='result')

# --- APP STARTTT !!! ---
if __name__ == '__main__':
    app.run(debug=True)