# print (f"{var/string : < 20}")
# menulis 20 karakter dari kiri ke kanan

# print (f"{var/string : > 20}")
# menulis 20 karakter dari kiri ke kanan

# print (f"{var/string : ^ 20}")
# menulis 20 karakter dengan rata kiri kanan

#membuat tabel database
pelanggan = []
alamat = []
nohandphone = []

# sub program masukan pelanggan dibuat oleh budi
def masukpelanggan():
    pelangganBaru = input("masukan nama pelanggan")
    pelanggan.append(pelangganBaru)
    alamatBaru = input("masukan alamat pelanggan")
    alamat.append (alamatBaru)
    nohpbaru = input ("masulan nomor hp = ")
    nohandphone.append(nohpbaru)

#sub program masukan pelanggan dibuat oleh fani
tampilkandata2 = """
    nama pelanggan      \t: {0}
    alamat pelanggan    \t: {1}
    no. telepon         \t: {2}"""

def tampilkandata(): 
    for i in range(0, len(pelanggan))
    print(tampilkandata2.format(pelanggan[i], alamat[i], nohandphone[i]))

#program utama dibuat oleh ali

jawaban = input("apakah anda ingin memasukan data pelanggan (ya/tidak) ? ")

while jawaban in ("Ya" , "Ya")
    masukpelanggan()
    jawaban = input ("apakah anda ingin memasukan data pelanggan(ya/tidak) ? ")
