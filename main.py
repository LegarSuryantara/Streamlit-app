import streamlit as st
from streamlit_option_menu import option_menu


with st.sidebar:
    selected = option_menu("Menu", ["Kalkulator", "Konversi suhu", "Fibonacci"],
    default_index=0)
    selected


if selected == "Kalkulator":
    st.title("Kalkulator Sederhana")
    angka1 = st.number_input("Masukkan angka pertama:")
    angka2 = st.number_input("Masukkan angka kedua:")
    operasi = st.selectbox("Pilih operasi:", ["Tambah", "Kurang", "Kali", "Bagi"])
    hitung = st.button("Hitung")

    if hitung:
        if operasi == "Tambah":
            hasil = angka1 + angka2
        elif operasi == "Kurang":
            hasil = angka1 - angka2
        elif operasi == "Kali":
            hasil = angka1 * angka2
        elif operasi == "Bagi":
            if angka2 != 0:
                hasil = angka1 / angka2
            else:
                hasil = "Error: Pembagian dengan nol"
        st.write(f"Hasil: {hasil}")
        st.success("Perhitungan selesai!")

elif selected == "Konversi suhu":
    st.title("Konversi Suhu")
    suhu = st.number_input("Masukkan suhu:")
    satuan_asal = st.selectbox("Pilih satuan asal:", ["Celsius", "Fahrenheit", "Reamur"])
    satuan_tujuan = st.selectbox("Pilih satuan tujuan:", ["Celsius", "Fahrenheit", "Reamur"])
    konvert = st.button("Konversi")

    if konvert:
        hasil = 0
        if satuan_asal == "Celsius":
            if satuan_tujuan == "Fahrenheit":
                hasil = (suhu * 9/5) + 32
                st.write(f"Hasil: {hasil} °F")
            elif satuan_tujuan == "Reamur":
                hasil = suhu * 4/5
                st.write(f"Hasil: {hasil} °R")
            else:
                st.write(f"Hasil: {suhu} °C")
        elif satuan_asal == "Fahrenheit":
            if satuan_tujuan == "Celsius":
                hasil = (suhu - 32) * 5/9
                st.write(f"Hasil: {hasil} °C")
            elif satuan_tujuan == "Reamur":
                hasil = (suhu - 32) * 4/9
                st.write(f"Hasil: {hasil} °R")
            else:
                st.write(f"Hasil: {suhu} °F") 
        elif satuan_asal == "Reamur":
            if satuan_tujuan == "Celsius":
                hasil = suhu * 5/4
                st.write(f"Hasil: {hasil} °C")
            elif satuan_tujuan == "Fahrenheit":
                hasil = (suhu * 9/4) + 32
                st.write(f"Hasil: {hasil} °F")
            else:
                st.write(f"Hasil: {suhu} °R")
        st.success("Konversi selesai!")

elif selected == "Fibonacci":
    st.title("Deret Fibonacci")
    n = st.number_input("Masukkan jumlah bilangan Fibonacci yang diinginkan:", min_value=1, step=1)
    generate = st.button("Generate")

    if generate:
        fib_sequence = []
        a, b = 0, 1
        for _ in range(n):
            fib_sequence.append(a)
            a, b = b, a + b
        st.write(f"Deret Fibonacci: {fib_sequence}")
        st.success("Deret selesai!")