import streamlit as st

# =========================
# FUNGSI FISIKA
# =========================
def hitung_gaya(m, mu_s, mu_k, F):
    g = 9.8
    fs_max = mu_s * m * g
    fk = mu_k * m * g

    if F < fs_max:
        status = "Benda tidak bergerak (gaya gesek statis)"
    else:
        status = "Benda bergerak (gaya gesek kinetis)"

    return fs_max, fk, status


# =========================
# FUNGSI AI (PLACEHOLDER)
# =========================
def tanya_ai(system_prompt, user_prompt):
    jawaban = (
        "📘 Penjelasan AI:\n\n"
        + system_prompt
        + "\n\nDetail Percobaan:\n"
        + user_prompt
    )
    return jawaban


# =========================
# STREAMLIT UI
# =========================
st.title("Praktikum Online: Gaya Gesek")

m = st.number_input("Massa benda (kg)", min_value=0.0, value=2.0)
mu_s = st.number_input("Koefisien gesek statis (μs)", min_value=0.0, value=0.5)
mu_k = st.number_input("Koefisien gesek kinetis (μk)", min_value=0.0, value=0.3)
F = st.number_input("Gaya tarik (N)", min_value=0.0, value=10.0)

fs_max, fk, status = hitung_gaya(m, mu_s, mu_k, F)

st.subheader("Hasil Perhitungan")
st.write(f"Gaya gesek statis maksimum: {fs_max:.2f} N")
st.write(f"Gaya gesek kinetis: {fk:.2f} N")
st.info(status)

pertanyaan = st.text_input("Tanyakan sesuatu tentang percobaan ini:")

if pertanyaan:
    system_prompt = (
        "Anda adalah asisten fisika yang menjelaskan konsep "
        "gaya gesek statis dan kinetis secara sederhana."
    )

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
