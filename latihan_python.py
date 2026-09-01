from kalkulator_bangun import *
from logika_bilangan import *

while True:
    print("\n========================================")
    print("   MODUL MATEMATIKA & LOGIKA PYTHON    ")
    print("========================================")
    print("1. Hitung Luas Persegi")
    print("2. Hitung Keliling Persegi")
    print("3. Cek Bilangan Prima")
    print("4. Cek Bilangan Genap / Ganjil")
    print("5. Hitung Luas Lingkaran")
    print("6. Hitung Luas Segitiga")
    print("7. Keluar")
    print("========================================")
    
    pilihan = input("Pilih menu (1-7): ")
    
    if pilihan == "1":
        print("\n--- MODUL 1: LUAS PERSEGI ---")
        sisi = float(input("Masukkan sisi: "))
        print(f" -> Hasil Luas Persegi: {hitung_luas_bujursangkar(sisi)}")
        
    elif pilihan == "2":
        print("\n--- MODUL 2: KELILING PERSEGI ---")
        sisi = float(input("Masukkan sisi: "))
        print(f" -> Hasil Keliling Persegi: {hitung_keliling_bujursangkar(sisi)}")
        
    elif pilihan == "3":
        print("\n--- MODUL 3: BILANGAN PRIMA ---")
        angka = int(input("Masukkan angka: "))
        if cek_prima(angka):
            print(f" -> {angka} adalah Bilangan Prima.")
        else:
            print(f" -> {angka} bukan Bilangan Prima.")
            
    elif pilihan == "4":
        print("\n--- MODUL 4: GENAP / GANJIL ---")
        x = int(input("Masukkan angka: "))
        print(f" -> {x} adalah {cek_paritas(x)}.")
            
    elif pilihan == "5":
        print("\n--- MODUL 5: LUAS LINGKARAN ---")
        r = float(input("Masukkan jari-jari: "))
        print(f" -> Hasil Luas Lingkaran: {luas_lingkaran_custom(r)}")

    elif pilihan == "6":
        print("\n--- MODUL 6: LUAS SEGITIGA ---")
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        print(f" -> Hasil Luas Segitiga: {luas_segitiga_custom(alas, tinggi)}")
        
    elif pilihan == "7":
        print("\nProgram selesai, terima kasih!")
        break
    else:
        print("\nPilihan salah, masukkan angka 1 sampai 7.")
