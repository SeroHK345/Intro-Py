from RumusMtk import RumusMatematika
    
def main():
    print("Hello from project1!")
    print("Hasil Penjumlahan: ", RumusMatematika.tambah(10,5))
    print("Hasil Penjumlahan: ", RumusMatematika.kurang(10,5))
    print("Hasil Penjumlahan: ", RumusMatematika.kali(10,5))
    print("Hasil Penjumlahan: ", RumusMatematika.bagi(10,5))
    
    hasil = RumusMatematika.luasPersegi(5)
    print("Hasil Luas Persegi: ", hasil)


if __name__ == "__main__":
    main()
