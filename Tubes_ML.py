from tabulate import tabulate
import math
import numpy as np
import pandas as pd

#Bila tidak bisa di run dengan "py" run dengan "python3"
d = np.genfromtxt(r"C:\Users\Doremie\Documents\Workspace\Tubes\training2.csv",delimiter=',') 
data_input = d[:,0:5] 
data_target = np.zeros([np.size(data_input,0),1]) #bikin matrix target
data_target[:,0] = d[:,4]  #assign dengan kolom sebagai target

data_value = pd.read_csv(r"C:\Users\Doremie\Documents\Workspace\Tubes\training22.csv")

#input nama pegawai
nama = data_value['name'].tolist()

#input masa kerja
kerja = d[:,1:2]

#input usia
usia = d[:,2:3]

#input nilai pelatihan
pelatihan = d[:,3:4]

#input nilai kinerja
kinerja = d[:,4:5]

#input hasil evaluasi
hasil = data_value['Evaluasi']

#inisialisasi tabel normalisasi
n_kerja = []
n_usia =[]
n_pelatihan = []
n_kinerja = []

#normalisasi
for i in range(0,100):
    #rumus normalisasi
    n_kerja.append((kerja[i]-min(kerja))/(max(kerja)-min(kerja)))
    n_usia.append((usia[i]-min(usia))/(max(usia)-min(usia)))
    n_pelatihan.append((pelatihan[i]-min(pelatihan))/(max(pelatihan)-min(pelatihan)))
    n_kinerja.append((kinerja[i]-min(kinerja))/(max(kinerja)-min(kinerja)))

k = input("Masukan nilai k: ")
nama_i = input("Masukan nama: ")
kerja_i = input("Masukan lama masa kerja: ")
usia_i = input("Masukan usia: ")
pelatihan_i = input("Masukan nilai pelatihan: ")
kinerja_i = input("Masukan nilai kinerja: ")

euclidian = []

#menghitung jarak euclidian
for i in range(0,100):
    #rumus euclidian
    euclidian.append(math.sqrt((n_kerja[i]-float(kerja_i))**2+(n_usia[i]-float(usia_i))**2+(n_pelatihan[i]-float(pelatihan_i))**2+(n_kinerja[i]-float(kinerja_i))**2))

#(n_kerja[i]-float(kerja_i))**2+(n_usia[i]-float(usia_i))**2+(n_pelatihan[i]-float(pelatihan_i))**2+(n_kinerja[i]-float(kinerja_i))**2
# table = [["No","nama","masa kerja","usia","pelatihan","kinerja","hasil"]]
# m = 1
# for i in range (0,1):
#     table.append([m,nama[i],kerja[i],usia[i],pelatihan[i],kinerja[i],hasil[i]])
#     m = m + 1
# print(tabulate(table, headers="firstrow", tablefmt='grid'))

# table = [["No","nama","masa kerja","usia","pelatihan","kinerja","hasil"]]
# m = 1
# for i in range (0,33):
#     table.append([m,nama[i],n_kerja[i],n_usia[i],n_pelatihan[i],n_kinerja[i],hasil[i]])
#     m = m + 1
# print(tabulate(table, headers="firstrow", tablefmt='grid'))

zipped_list = zip(euclidian, hasil)
sorted_pairs = sorted(zipped_list)

tuples = zip(*sorted_pairs)
euclidian, hasil = [ list(tuple) for tuple in  tuples]

mut = 0
phk = 0
pro = 0

table = [["euclidian","evaluasi"]]
for i in range (0,int(k)):
    table.append([euclidian[i],hasil[i]])
    if hasil[i] == "MUTASI":
        mut = mut + 1
    elif hasil[i] == "PROMOSI":
        pro = pro + 1
    elif hasil[i] == "PHK":
        phk = phk + 1

# if mut == phk or mut == pro or pro == phk:
#     pro = pro * 0
#     mut = mut * 0
#     phk = phk * 0
#     for i in range (0,int(k)-1):
#         if hasil[i] == "MUTASI":
#             mut = mut + 1
#         elif hasil[i] == "PROMOSI":
#             pro = pro + 1
#         elif hasil[i] == "PHK":
#             phk = phk + 1

if mut > phk and mut > pro:
    evaluasi = "MUTASI"

if phk > mut and phk > pro:
    evaluasi = "PHK"

if pro > mut and pro > phk:
    evaluasi = "PROMOSI"   

print(tabulate(table, headers="firstrow", tablefmt='grid'))
print("hasil  promosi : ",pro)
print("hasil  phk : ",phk)
print("hasil  mutasi : ",mut) 

# if mut == phk or mut == pro or pro == phk:
#     print("mohon kurangi nilai k dan coba lagi")
# else:
print("Maka hasil evaluasi yang didapat ",nama_i," adalah ",evaluasi)