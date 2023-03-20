def luas_segitiga(alas,tinggi):
    luas = (alas * tinggi) / 2
    print("-------------------")
    print("luas segitiga: %f" %luas)

alas = int(input("inputkan nilai alas:"))
tinggi = int(input("inputkan nilai tinggi:"))
luas_segitiga(alas, tinggi)