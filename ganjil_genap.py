while True:
    print("\n=== PROGRAM CEK GANJIL / GENAP ===")
    teks = input("Masukkan angka (ketik 0 untuk keluar): ")
    
    angka = int(teks)
    
    if angka == 0:
        print("Program selesai.")
        break
    elif angka % 2 == 0:
        print("Angka", angka, "adalah Bilangan GENAP")
    else:
        print("Angka", angka, "adalah Bilangan GANJIL")
