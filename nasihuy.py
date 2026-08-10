for i in range(100):
    angka = int(input("Masukkan angka: "))

    if angka % 2 == 0:
        print("Genap")
    else:
        print("Ganjil")

    lanjut = input("Masukkan lagi? (y/n): ")

    if lanjut == "n":
        break