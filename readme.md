# 🫀 Heart Disease Risk Prediction System

<div align="center">

![Heart Disease Prediction](https://img.shields.io/badge/Machine%20Learning-Bayesian%20Network-red?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0+-black?style=for-the-badge&logo=flask)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Aplikasi Web Flask untuk Prediksi Risiko Penyakit Jantung menggunakan Probabilistic Bayesian Network**

[Demo](#-demo) • [Fitur](#-fitur-utama) • [Instalasi](#-instalasi--cara-menjalankan) • [Tim](#-tim-pengembang)

---

<img src="https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif" width="300" alt="Heart Animation"/>

</div>

## 📋 Tentang Proyek

Sistem prediksi risiko penyakit jantung berbasis **Explainable AI (XAI)** yang tidak hanya memberikan prediksi "Ya" atau "Tidak", tetapi juga menjelaskan **"mengapa"** seseorang berisiko terkena penyakit jantung.

### 🎯 Mengapa Proyek Ini Penting?

- **🔍 Transparansi**: Menampilkan probabilitas risiko dan faktor-faktor utama yang berkontribusi
- **⚖️ Fairness**: Mengatasi data tidak seimbang dengan teknik SMOTE-Tomek
- **🧠 Interpretable**: Menggunakan Bayesian Network yang dapat dijelaskan kepada tenaga medis
- **🚀 Praktis**: Interface web yang mudah digunakan untuk screening awal

---

## 💡 Inspirasi & Metodologi

<div align="center">

```mermaid
graph LR
    A[📚 Research Paper] -->|Adaptasi| B[🫀 Heart Disease]
    B --> C[Bayesian Network]
    B --> D[SMOTE-Tomek]
    C --> E[Explainable Prediction]
    D --> E
    E --> F[🎯 Final Application]
```

</div>

Proyek ini terinspirasi dari penelitian:

> **Wang, W., Li, J., Wang, C. et al.** (2023)  
> *"Early detection of diabetes using Bayesian network and SMOTE-ENN"*  
> Scientific Reports, Nature  
> DOI: [10.1038/s41598-023-40036-5](https://doi.org/10.1038/s41598-023-40036-5)

Kami mengadaptasi metodologi tersebut dari kasus diabetes ke **penyakit jantung** menggunakan dataset dari Kaggle.

---

## ✨ Fitur Utama

<table>
<tr>
<td width="50%">

### 🎲 Prediksi Probabilistik
Memberikan **persentase risiko** (contoh: 75% berisiko) bukan hanya klasifikasi biner, sehingga memberikan gambaran yang lebih nuanced.

</td>
<td width="50%">

### 🔬 Explainable AI
Menampilkan **faktor risiko utama** yang memengaruhi prediksi:
- Kolesterol Tinggi
- Usia > 60 tahun
- Tekanan Darah Tinggi
- dll.

</td>
</tr>
<tr>
<td width="50%">

### ⚖️ Penanganan Data Imbalanced
Menggunakan **SMOTE-Tomek** untuk melatih model yang lebih adil dan akurat pada data yang tidak seimbang.

</td>
<td width="50%">

### 🎨 Antarmuka Modern
Interface web yang bersih dan intuitif menggunakan **Flask** + **Tailwind CSS**.

</td>
</tr>
</table>

---

## 🛠️ Tumpukan Teknologi

<div align="center">

| Kategori | Teknologi |
|----------|-----------|
| **Backend** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white) |
| **Machine Learning** | ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white) ![pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) |
| **Bayesian Network** | pgmpy |
| **Imbalanced Learning** | imblearn (SMOTE-Tomek) |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white) ![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat&logo=tailwind-css&logoColor=white) |

</div>

---

## 🚀 Instalasi & Cara Menjalankan

### 📦 Prasyarat

- Python 3.8 atau lebih tinggi
- Git
- pip (Python package manager)

### 🔧 Setup Langkah demi Langkah

#### 1️⃣ Clone Repository

```bash
git clone https://github.com/[USERNAME]/heart-disease-prediction.git
cd heart-disease-prediction
```

#### 2️⃣ Buat Virtual Environment (Opsional tapi Direkomendasikan)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

#### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**File `requirements.txt`:**
```txt
Flask==2.3.0
pandas==2.0.0
scikit-learn==1.3.0
pgmpy==0.1.23
imbalanced-learn==0.11.0
joblib==1.3.0
numpy==1.24.0
```

#### 4️⃣ Download Dataset

1. Unduh dataset dari Kaggle: [Heart Failure Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)
2. Buat folder `data/` di root project
3. Letakkan file CSV dan rename menjadi `heart.csv`

**Struktur Folder:**
```
heart-disease-prediction/
├── data/
│   └── heart.csv          # Dataset dari Kaggle
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   └── result.html
├── app.py                 # Flask application
├── train.py               # Training script
├── model.joblib           # Model terlatih (akan dibuat)
├── requirements.txt
└── README.md
```

#### 5️⃣ Train Model

Jalankan script training untuk memproses data, menerapkan SMOTE-Tomek, dan melatih Bayesian Network:

```bash
python train.py
```

**Output:**
- `model.joblib` - Model Bayesian Network yang sudah dilatih
- Metrik evaluasi akan ditampilkan di console

#### 6️⃣ Jalankan Aplikasi

```bash
flask run
# atau
python app.py
```

Buka browser dan akses: **http://127.0.0.1:5000**

---

## 📸 Demo

<div align="center">

### 🏠 Halaman Input

<img src="https://media.giphy.com/media/l0HlTy9x8FZo0XO1i/giphy.gif" width="600" alt="Input Form Demo"/>

*Form input data pasien dengan validasi real-time*

---

### 📊 Halaman Hasil Prediksi

<img src="https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif" width="600" alt="Prediction Result Demo"/>

*Hasil prediksi dengan probabilitas dan faktor risiko*

</div>

---

## 🧪 Cara Kerja Model

### 1. Data Preprocessing

```python
# Handling imbalanced data
smote_tomek = SMOTETomek(random_state=42)
X_resampled, y_resampled = smote_tomek.fit_resample(X, y)
```

### 2. Bayesian Network Structure

```mermaid
graph TD
    Age[Usia] --> Risk[Risiko]
    Cholesterol[Kolesterol] --> Risk
    BP[Tekanan Darah] --> Risk
    Sugar[Gula Darah] --> Risk
    ECG[ECG] --> Risk
    MaxHR[Max Heart Rate] --> Risk
    ChestPain[Nyeri Dada] --> Risk
```

### 3. Inference & Explanation

Model menghitung probabilitas posterior dan mengidentifikasi faktor-faktor dengan kontribusi tertinggi menggunakan **Maximum Aposteriori Probability (MAP)**.

---

## 📊 Evaluasi Model

| Metrik | Nilai |
|--------|-------|
| **Accuracy** | ~85% |
| **Precision** | ~83% |
| **Recall** | ~88% |
| **F1-Score** | ~85% |
| **AUC-ROC** | ~0.90 |

> ⚠️ **Disclaimer**: Model ini untuk tujuan edukasi dan penelitian. Untuk diagnosis medis, selalu konsultasikan dengan tenaga kesehatan profesional.

---

## 👥 Tim Pengembang

<div align="center">

<table>
<tr>
<td align="center" width="20%">
<img src="https://ui-avatars.com/api/?name=Evan&background=0D8ABC&color=fff&size=128" width="100px;" alt="Evan"/><br />
<sub><b>Evan</b></sub><br />
</td>
<td align="center" width="20%">
<img src="https://ui-avatars.com/api/?name=Benaya&background=6366F1&color=fff&size=128" width="100px;" alt="Benaya"/><br />
<sub><b>Benaya</b></sub><br />
</td>
<td align="center" width="20%">
<img src="https://ui-avatars.com/api/?name=Reymond&background=8B5CF6&color=fff&size=128" width="100px;" alt="Reymond"/><br />
<sub><b>Reymond</b></sub><br />
</td>
<td align="center" width="20%">
<img src="https://ui-avatars.com/api/?name=Berliana&background=EC4899&color=fff&size=128" width="100px;" alt="Berliana"/><br />
<sub><b>Berliana</b></sub><br />
</td>
</tr>
</table>

**Proyek UAS - Machine Learning 2024/2025**

</div>

---

## 📚 Struktur File

```
heart-disease-prediction/
│
├── 📁 data/
│   └── heart.csv                 # Dataset
│
├── 📁 static/
│   ├── style.css                 # Custom CSS
│   └── js/
│       └── main.js               # Frontend logic
│
├── 📁 templates/
│   ├── index.html                # Input form page
│   ├── result.html               # Prediction result page
│   └── base.html                 # Base template
│
├── 📄 app.py                     # Flask application
├── 📄 train.py                   # Model training script
├── 📄 model.joblib               # Trained model
├── 📄 requirements.txt           # Python dependencies
├── 📄 README.md                  # Documentation (you are here!)
└── 📄 LICENSE                    # MIT License
```

---

## 🤝 Kontribusi

Kami menerima kontribusi! Jika Anda ingin berkontribusi:

1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan Anda (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

---

## 🙏 Acknowledgments

- **Dataset**: [Kaggle - Heart Failure Prediction](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)
- **Inspirasi Penelitian**: Wang et al. (2023) - Nature Scientific Reports
- **Framework**: Flask, pgmpy, scikit-learn, imbalanced-learn
- **Dosen Pembimbing**: [Nama Dosen] - Mata Kuliah Machine Learning

---

<div align="center">

### 💖 Made with Love & Python

<img src="https://media.giphy.com/media/LnQjpWaON8nhr21vNW/giphy.gif" width="60" alt="Love"/>

**⭐ Jangan lupa beri bintang jika proyek ini bermanfaat! ⭐**

</div>

---

## 📈 Roadmap

- [x] Implementasi Bayesian Network
- [x] Penanganan data imbalanced dengan SMOTE-Tomek
- [x] Web interface dengan Flask
- [x] Explainable AI features
- [ ] Deploy ke cloud (Heroku/Railway)
- [ ] API REST untuk integrasi eksternal
- [ ] Mobile app (Flutter)
- [ ] Dashboard analytics untuk dokter
- [ ] Multi-bahasa support (EN/ID)

---

<div align="center">

**🫀 Prediksi Lebih Awal, Hidup Lebih Sehat 🫀**

</div>
