import streamlit as st
import numpy as np

# =========================
# FUNGSI FISIKA
# =========================
def hitung_gaya(m, mu_s, mu_k, F):
    g = 9.8
    fs_max = mu_s * m * g
    fk = mu_k * m * g

    if F < fs_max:
        status = "Benda tidak bergerak (gaya gesek statis)"
        gaya_gesek = F
    else:
        status = "Benda bergerak (gaya gesek kinetis)"
        gaya_gesek = fk

    return fs_max, fk, gaya_gesek, status


# =========================
# STREAMLIT UI
# =========================
st.title("Praktikum Online: Gaya Gesek Statis dan Kinetis")

st.markdown("""
Aplikasi ini mensimulasikan **gaya gesek statis dan kinetis**
pada sebuah benda yang ditarik di atas permukaan datar.
""")

# Input parameter
m = st.number_input("Massa benda (kg)", min_value=0.1, value=2.0)
mu_s = st.number_input("Koefisien gesek statis (μs)", min_value=0.0, value=0.5)
mu_k = st.number_input("Koefisien gesek kinetis (μk)", min_value=0.0, value=0.3)
F = st.number_input("Gaya tarik (N)", min_value=0.0, value=10.0)

# Perhitungan
fs_max, fk, gaya_gesek, status = hitung_gaya(m, mu_s, mu_k, F)

# =========================
# OUTPUT TEKS
# =========================
st.subheader("Hasil Perhitungan")
st.write(f"Gaya gesek statis maksimum (Fs max): **{fs_max:.2f} N**")
st.write(f"Gaya gesek kinetis (Fk): **{fk:.2f} N**")
st.write(f"Gaya gesek yang bekerja: **{gaya_gesek:.2f} N**")
st.info(status)

# =========================
# GRAFIK (TANPA MATPLOTLIB)
# =========================
st.subheader("Grafik Hubungan Gaya Tarik dan Gaya Gesek")

F_range = np.linspace(0, fs_max * 1.5, 100)
gaya_gesek_range = []

for F_i in F_range:
    if F_i < fs_max:
        gaya_gesek_range.append(F_i)
    else:
        gaya_gesek_range.append(fk)

grafik_data = {
    "Gaya Tarik (N)": F_range,
    "Gaya Gesek (N)": gaya_gesek_range
}

st.line_chart(grafik_data)

# =========================
# KESIMPULAN
# =========================
st.subheader("Kesimpulan")

if F < fs_max:
    st.write(
        "Gaya tarik belum cukup untuk mengatasi gaya gesek statis maksimum, "
        "sehingga benda masih dalam keadaan diam."
    )
else:
    st.write(
        "Gaya tarik telah melebihi gaya gesek statis maksimum, "
        "sehingga benda bergerak dan gaya gesek yang bekerja adalah gaya gesek kinetis."
    )
