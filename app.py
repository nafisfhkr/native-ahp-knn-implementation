import streamlit as st
import numpy as np
import model as mn 


st.set_page_config(page_title="Sistem SPK Kredit Petani", page_icon="🌾")

# --- JUDUL & HEADER ---
st.title("🌾Prediksi Kredit Petani")
st.markdown("Sistem Pendukung Keputusan menggunakan **Hybrid AHP-KNN (Native)**")
st.markdown("---")


st.sidebar.header("📝 Masukkan Data Petani")

input_panen = st.sidebar.number_input("Rata-rata Pendapatan Panen (Rp)", min_value=0, value=5000)

input_sampingan = st.sidebar.number_input("Pendapatan Sampingan (Rp)", min_value=0, value=0)

input_pinjaman = st.sidebar.number_input("Pengajuan Jumlah Pinjaman (Ribuan)", min_value=0, value=100)

input_durasi = st.sidebar.selectbox("Durasi Pinjaman (Hari)", [360, 180, 120, 60, 30])

st.sidebar.subheader("⭐ (Bobot Tertinggi)")
input_riwayat = st.sidebar.radio("Riwayat Kredit Digital (Skor Reputasi)", [1.0, 0.0], 
                                 format_func=lambda x: "Baik (1.0)" if x == 1.0 else "Buruk (0.0)")


input_lokasi = st.sidebar.selectbox("Lokasi Lahan", ["Pedesaan (Rural)", "Semi-Kota (Semiurban)", "Perkotaan (Urban)"])
map_lokasi = {"Pedesaan (Rural)": 0, "Semi-Kota (Semiurban)": 1, "Perkotaan (Urban)": 2}
val_lokasi = map_lokasi[input_lokasi]

@st.cache_resource
def get_model():
    return mn.load_and_train_model()

model, data_min, data_max = get_model()

if st.button("🔍 Analisis Kelayakan"):
    user_data = [input_panen, input_sampingan, input_pinjaman, input_durasi, input_riwayat, val_lokasi]
    

    user_data_norm = (np.array(user_data) - data_min) / (data_max - data_min)
    
    hasil = model.predict_single(user_data_norm)
    
    st.markdown("### Hasil Keputusan Sistem:")
    
    if hasil == "Y": 
        st.success(f"✅ **LAYAK DIBERIKAN MODAL**")
        st.balloons()
        st.write("Profil risiko petani ini dinilai aman berdasarkan algoritma AHP-KNN.")
    else:
        st.error(f"❌ **TIDAK LAYAK / BERISIKO TINGGI**")
        st.write("Mohon maaf, profil risiko petani ini belum memenuhi standar kelayakan.")


st.markdown("---")
st.caption("Dikembangkan oleh M Nafis F | Metode: Hybrid AHP-KNN (Native Python) | Dataset: Loan Prediction Dataset")