import streamlit as st
import numpy as np
import pandas as pd

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
pada sebuah benda yang ditarik di atas permukaan datar,
lengkap dengan **visualisasi arah gaya dan balok**.
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
# GRAFIK NUMERIK
# =========================
st.subheader("Grafik Hubungan Gaya Tarik dan Gaya Gesek")

F_range = np.linspace(0, fs_max * 1.5, 100)
gaya_gesek_range = []

for F_i in F_range:
    if F_i < fs_max:
        gaya_gesek_range.append(F_i)
    else:
        gaya_gesek_range.append(fk)

st.line_chart({
    "Gaya Tarik (N)": F_range,
    "Gaya Gesek (N)": gaya_gesek_range
})

# =========================
# VISUALISASI SIMULASI BALOK & GAYA
# =========================
st.subheader("Visualisasi Simulasi Gaya")

# Skala visual (agar panah tidak terlalu panjang)
skala = max(F, gaya_gesek, 1)
Ft_visual = F / skala
Fg_visual = gaya_gesek / skala

data = pd.DataFrame({
    "x": [0, 0],
    "y": [0, 0],
    "dx": [Ft_visual, -Fg_visual],
    "dy": [0, 0],
    "jenis": ["Gaya Tarik", "Gaya Gesek"]
})

st.vega_lite_chart(
    data,
    {
        "width": 500,
        "height": 200,
        "layer": [
            # Balok
            {
                "mark": {"type": "rect", "width": 60, "height": 40},
                "encoding": {
                    "x": {"value": 250},
                    "y": {"value": 100},
                    "color": {"value": "steelblue"}
                }
            },
            # Panah gaya
            {
                "mark": {"type": "rule", "strokeWidth": 4},
                "encoding": {
                    "x": {"value": 250},
                    "y": {"value": 100},
                    "x2": {
                        "field": "dx",
                        "type": "quantitative",
                        "scale": {"domain": [-1, 1], "range": [100, 400]}
                    },
                    "y2": {"value": 100},
                    "color": {
                        "field": "jenis",
                        "type": "nominal",
                        "scale": {
                            "domain": ["Gaya Tarik", "Gaya Gesek"],
                            "range": ["green", "red"]
                        }
                    }
                }
            }
        ]
    }
)

st.caption("Panah hijau: gaya tarik | Panah merah: gaya gesek")

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
