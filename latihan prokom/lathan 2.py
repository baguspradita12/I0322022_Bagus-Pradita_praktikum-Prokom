#program matrik 3x3

#input
matriksA=[[1,2,3],
          [4,5,6],
          [7,8,9]]

matriksB=[[9,8,7],
          [6,5,4],
          [3,2,1]]

HasilJumlah=[[0,0,0],
             [0,0,0],
             [0,0,0]] 

#proses

#output



#proses penjumlahan matriks 1 dan 2

for x in range(0, len(matriksA)):
   #print()
   for y in range(0,len(matriksA[0])):
      
      HasilJumlah[x][y] = matriksA[x][y] + matriksB[x][y]
      print(HasilJumlah[x][y], end=" ")

   print()   

print("==================================")
