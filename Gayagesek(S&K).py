import sys
import os

def tanya_ai(system_prompt, user_prompt):
    """
    Fungsi AI sederhana (placeholder).
    Untuk sementara hanya menggabungkan prompt.
    """

    jawaban = (
        "📘 Penjelasan AI:\n\n"
        + system_prompt
        + "\n\nPertanyaan:\n"
        + user_prompt
    )

    return jawaban

sys.path.append(os.path.dirname(__file__))

import streamlit as st
def hitung_gaya(massa, percepatan):
    return massa * percepatan
def hitung_gaya(m, mu_s, mu_k, F):
    g = 9.8
    
    fs_max = mu_s * m * g
    fk = mu_k * m * g

    if F < fs_max:
        status = "Benda tidak bergerak (gaya gesek statis)"
    else:
        status = "Benda bergerak (gaya gesek kinetis)"

    return fs_max, fk, status

def tanya_ai(pertanyaan):
    return "Fitur AI belum diaktifkan."

st.title("Praktikum Online: Gaya Gesek")

m = st.slider("Massa (kg)", 0.5, 10.0, 2.0)
mu_s = st.slider("μs", 0.1, 1.0, 0.5)
mu_k = st.slider("μk", 0.1, mu_s, 0.3)
F = st.slider("Gaya Tarik (N)", 0.0, 100.0, 10.0)

fs_max, fk, status = hitung_gaya(m, mu_s, mu_k, F)
m = st.number_input("Massa benda (kg)", min_value=0.0)
mu_s = st.number_input("Koefisien gesek statis", min_value=0.0)
mu_k = st.number_input("Koefisien gesek kinetis", min_value=0.0)
F = st.number_input("Gaya tarik (N)", min_value=0.0)

st.subheader("Status Benda")
st.info(status)

pertanyaan = st.text_input("Tanyakan sesuatu tentang percobaan ini:")

if pertanyaan:
    system_prompt = """
Anda adalah asisten fisika yang membantu menjelaskan konsep gaya gesek
statis dan kinetis secara sederhana dan mudah dipahami.
"""
    user_prompt = f"""
    Massa: {m} kg
    μs: {mu_s}
    μk: {mu_k}
    Gaya: {F} N
    Status: {status}

    Pertanyaan siswa:
    {pertanyaan}
    """
    jawaban = tanya_ai(system_prompt, user_prompt)
    st.success(jawaban)






