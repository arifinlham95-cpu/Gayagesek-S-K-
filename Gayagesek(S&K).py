import sys
import os

sys.path.append(os.path.dirname(__file__))

import streamlit as st
def hitung_gaya(massa, percepatan):
    return massa * percepatan

from utils.ai_engine import tanya_ai

st.title("Praktikum Online: Gaya Gesek")

m = st.slider("Massa (kg)", 0.5, 10.0, 2.0)
mu_s = st.slider("μs", 0.1, 1.0, 0.5)
mu_k = st.slider("μk", 0.1, mu_s, 0.3)
F = st.slider("Gaya Tarik (N)", 0.0, 100.0, 10.0)

fs_max, fk, status = hitung_gaya(m, mu_s, mu_k, F)

st.subheader("Status Benda")
st.info(status)

pertanyaan = st.text_input("Tanyakan sesuatu tentang percobaan ini:")

if pertanyaan:
    system_prompt = open("prompt/system.txt").read()
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


