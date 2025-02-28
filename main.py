import RumusMtk
    
def main():
    print("Hello from project1!")
    print("Hasil Penjumlahan: ", RumusMtk.tambah(10,5))
    print("Hasil Penjumlahan: ", RumusMtk.kurang(10,5))
    print("Hasil Penjumlahan: ", RumusMtk.kali(10,5))
    print("Hasil Penjumlahan: ", RumusMtk.bagi(10,5))
    
    hasil = RumusMtk.luasPersegi(5)
    print("Hasil Luas Persegi: ", hasil)


if __name__ == "__main__":
    main()
