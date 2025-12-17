# 🌾 Micro-Farmer Credit Scoring System (Native Hybrid AHP-KNN)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

<p align="center">
  <a href="#english">🇺🇸 English</a> | <a href="#bahasa-indonesia">🇮🇩 Bahasa Indonesia</a>
</p>

---

<div id="english"></div>

## 🇺🇸 English

### Project Description
This repository contains the source code for a **Creditworthiness Decision Support System (DSS)** designed for micro-farmers. The system implements a **Hybrid AHP-KNN** method built entirely using **Native Python (From Scratch)** without relying on instant machine learning libraries (like Scikit-Learn) for its core algorithms. This project demonstrates a fundamental understanding of computational logic.

### 🚀 Key Features
* **🧠 Hybrid Algorithm:** Combines **AHP** (Analytic Hierarchy Process) for feature weighting and **KNN** (K-Nearest Neighbors) for classification.
* **🐍 100% Native Python:** Core logic (Euclidean Distance, Sorting, Slicing, Voting, and Data Splitting) is written manually using pure NumPy.
* **⚖️ Weighted Distance Logic:** Implements *Weighted Euclidean Distance* where **Digital Credit History** has the highest influence (Weight: 0.45).
* **📊 Manual Evaluation:** Performance metrics (Accuracy, Precision, Recall, Specificity) are calculated using manual mathematical formulas.
* **🖥️ Interactive GUI:** User-friendly web interface powered by **Streamlit**.

### 📂 Repository Structure
```text
📂 MODEL_KLASIFIKASI_DEBT/
│
├── 📄 app.py                     
├── 📄 model.py           
├── 📄 requirements.txt           
├── 📄 README.md                  
│
├── 📂 data/                      
│   └── loan_data.csv
│
└── 📂 notebooks/                
    └── eksperimen_tuning.ipynb   

```

### 🔬 Technical Logic

1. **AHP Weighting:** Features are prioritized based on expert logic:
* *Digital Credit History:* 45.08% (Dominant)
* *Harvest Income:* 21.29%
* *Others:* Location, Loan Duration, etc.


2. **Native KNN Workflow:**
* Calculate distance using formula: \sqrt{\sum w_i (x_i - y_i)^2}
* Sort training data by distance (ascending).
* Slice top **K=11** neighbors.
* Vote for the majority class ("Eligible" vs "Not Eligible").



### 📈 Performance Results

Based on Hyperparameter Tuning (available in `notebooks/`), the optimal parameter is **K=11**.

| Metric | Score | Analysis |
| --- | --- | --- |
| **Accuracy** | **81.97%** | Global prediction success rate. |
| **Recall** | **98.84%** | Highly sensitive in detecting eligible farmers (Minimizing False Negatives). |
| **Precision** | **80.19%** | High confidence when predicting "Eligible". 

---

---

<div id="bahasa-indonesia"></div>

## 🇮🇩 Bahasa Indonesia

### Deskripsi Proyek

Repositori ini berisi *source code* implementasi **Sistem Pendukung Keputusan (SPK)** untuk menilai kelayakan kredit petani. Sistem ini dibangun menggunakan metode **Hybrid AHP-KNN** yang ditulis secara **Native (From Scratch)** tanpa bergantung pada *library* algoritma instan (seperti Scikit-Learn) untuk menjaga orisinalitas logika komputasi.

### 🚀 Fitur Utama

* **🧠 Algoritma Hybrid:** Menggabungkan **AHP** (*Analytic Hierarchy Process*) untuk pembobotan fitur risiko dan **KNN** (*K-Nearest Neighbors*) untuk klasifikasi.
* **🐍 Implementasi Native Python:** Seluruh logika inti (Rumus Jarak Euclidean, Sorting, Voting, hingga Splitting Data) ditulis manual menggunakan Python/NumPy murni.
* **⚖️ Logika Jarak Berbobot:** Menerapkan *Weighted Euclidean Distance* di mana fitur **Riwayat Kredit Digital** memiliki bobot pengaruh terbesar (0.45).
* **📊 Evaluasi Manual:** Perhitungan metrik evaluasi (Akurasi, Presisi, Recall, Spesifisitas) dilakukan menggunakan rumus matematika manual.
* **🖥️ GUI Interaktif:** Antarmuka pengguna berbasis web menggunakan **Streamlit**.

### 📂 Struktur Repositori

```text
📂 MODEL_KALSIFIKASI_DEBT/
│
├── 📄 app.py                     
├── 📄 model_native.py            
├── 📄 requirements.txt          
├── 📄 README.md                  
│
├── 📂 data/                      
│   └── data_petani.csv
│
└── 📂 notebooks/                 
    └── eksperimen_tuning.ipynb   

```



### 🔬 Penjelasan Teknis

1. **Pembobotan (AHP):** Sistem memprioritaskan kriteria penilaian berdasarkan bobot pakar:
* *Riwayat Kredit Digital:* 45.08% (Prioritas Utama)
* *Pendapatan Panen:* 21.29%
* *Lainnya:* Lokasi, Durasi Pinjaman, dll.


2. **Logika Native KNN:**
* **Hitung Jarak:** Menggunakan rumus $\sqrt{\sum w_i (x_i - y_i)^2}$.
* **Sorting:** Mengurutkan data latih dari jarak terdekat (*ascending*).
* **Slicing:** Mengambil **K=11** tetangga teratas.
* **Voting:** Menentukan status "Layak/Tidak" berdasarkan suara terbanyak.



### 📈 Hasil Evaluasi & Performa

Berdasarkan pengujian *Hyperparameter Tuning* (tersedia di folder `notebooks`), parameter optimal ditemukan pada **K=11**.

| Metrik Evaluasi | Skor | Analisis |
| --- | --- | --- |
| **Akurasi** | **81.97%** | Tingkat keberhasilan prediksi global. |
| **Recall** | **98.84%** | Sistem sangat sensitif mendeteksi petani layak (Minim *False Negative*). |
| **Presisi** | **80.19%** | Tingkat kepercayaan saat sistem memprediksi "Layak". |

---

### 🤝 Developer / Pengembang

* ** Nafis Fakhru **


```

```