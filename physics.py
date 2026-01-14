def hitung_gaya(m, mu_s, mu_k, F):
    g = 9.8
    N = m * g
    fs_max = mu_s * N
    fk = mu_k * N

    if F < fs_max:
        status = "Diam (Gesek Statis)"
    else:
        status = "Bergerak (Gesek Kinetis)"

    return fs_max, fk, status
