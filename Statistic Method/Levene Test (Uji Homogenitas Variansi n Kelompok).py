'''PROGRAM LEVENE TEST'''

import scipy.stats as st

print(" H0 : Variansi sama")
print(" H1 : Variansi tidak sama \n")
alfa = input("Tingkat Signifikansi : ")

jumlah_populasi = int(input("Jumlah Populasi : "))
'''Nomer 13.1'''
data_populasi = [[60,50,75,67,78,45,53,55],
                 [65,56,76,70,75,40,52,56],
                 [67,54,78,75,80,65,67,66]]
#'''Nomer 13.2'''
#data_populasi = [[5.2,4.7,8.1,6.2,3.0],[9.1,7.1,8.2,6.0,9.1],
#                 [3.2,5.8,2.2,3.1,7.2],[2.4,3.4,4.1,1.0,4.0],
#                 [7.1,6.6,9.3,4.2,7.6]]
#'''Nomer 13.6'''
#data_populasi = [[1.06,0.79,0.82,0.89,1.05,0.95,0.65,1.15,1.12],
#                 [1.58,1.45,0.57,1.16,1.12,0.91,0.83,0.43],
#                 [0.29,0.06,0.44,0.55,0.61,0.43,0.51,0.1,0.53
#                  ,0.34,0.06,0.09,0.17,0.17,0.6]]



#for i in range(1,jumlah_populasi+1):
#    populasi_i = []
#    jumlah_data_i = int(input("Jumlah data populasi ke {0} : ".format(i)))
#    for j in range(1,jumlah_data_i+1):
#        data_j = float(input("Data ke {0} : ".format(j)))
#        populasi_i.append(data_j)
#    print("\n")
#    data_populasi.append(populasi_i)

N = 0
for i in range (0,jumlah_populasi):
    N_jumlah = len(data_populasi[i])
    N += N_jumlah  
print("Jumlah total ukuran sampel n = ",N)


#================================== Median =================================
for i in range (0,jumlah_populasi):
    for j in range (0,len(data_populasi[i])):
        for k in range (0,len(data_populasi[i])) :
            if data_populasi[i][k] > data_populasi[i][j]:
                data_populasi[i][k], data_populasi[i][j] = data_populasi[i][j],data_populasi[i][k]

median = []
for i in range (0,jumlah_populasi):
    jumlah_data_i = len(data_populasi[i])
    
    modulus_2 = len(data_populasi[i]) % 2
    if modulus_2 == 0 :
        j = int((jumlah_data_i)/2) - 1
        k = int((jumlah_data_i)/2)
        median_1 = (data_populasi[i][j] + data_populasi[i][k])/2
        median.append(median_1)
    else :
        j = int(((jumlah_data_i)+1)/2) - 1
        median_1 = data_populasi[i][j]
        median.append(median_1)      


'''balikin ke data awal'''
data_populasi = [[60,50,75,67,78,45,53,55],
                 [65,56,76,70,75,40,52,56],
                 [67,54,78,75,80,65,67,66]]
#data_populasi = [[17.5,16.9,15.8,18.6],[16.4,19.2,17.7,15.4],
#                 [20.3,15.7,17.8,18.9],[14.6,16.7,20.8,18.9],
#                 [17.5,19.2,16.5,20.5],[18.3,16.2,17.5,20.1]]
#data_populasi = [[1.06,0.79,0.82,0.89,1.05,0.95,0.65,1.15,1.12],
#                 [1.58,1.45,0.57,1.16,1.12,0.91,0.83,0.43],
#                 [0.29,0.06,0.44,0.55,0.61,0.43,0.51,0.1,0.53
#                  ,0.34,0.06,0.09,0.17,0.17,0.6]]
print("Data =",data_populasi)
print("Median tiap kelompok =",median)

#========================== y bar, y_ij ================================
y_dikurangi = [] #y_ij
for i in range (0, jumlah_populasi) :
    y_i = []
    for j in range(len(data_populasi[i])):
        y_ij = abs(data_populasi[i][j] - median[i])
        y_i.append(y_ij)
    y_dikurangi.append(y_i)
print("\ny_ij kelompok =",y_dikurangi)


y_bar = [] #y_bar masing kelompok
for i in range (0, jumlah_populasi) :
    y_i_bar = sum(y_dikurangi[i])/(len(y_dikurangi[i]))
    y_bar.append(y_i_bar)
print("\nRata-rata y_bar kelompok =",y_bar)

#===============================
#y bar total (Rata-rata yi_bar)
#y_bar_keseluruhan = 0
#jumlah_data_y_bar_keseluruhan = []
#for i in range (0, jumlah_populasi) :
#    y_bar_keseluruhan += sum(y_dikurangi[i])
#    jumlah_data_y_bar_keseluruhan.append(len(y_dikurangi[i]))
#jumlah_data_y_bar_keseluruhan = sum(jumlah_data_y_bar_keseluruhan)
#
#print("Jumlah data y_bar =",jumlah_data_y_bar_keseluruhan)
#print("Rata-rata y_bar keseluruhan =",y_bar_keseluruhan / jumlah_data_y_bar_keseluruhan)
#================================

rata_data_y_bar_keseluruhan = sum(y_bar)/jumlah_populasi
print("Rata-rata y_bar keseluruhan =",rata_data_y_bar_keseluruhan)

#=================== PRINT DATA ==================================
#for i in range (len(data_populasi)):
#    print("Populasi ke {0}".format(i+1))
#    for j in range (0,len(data_populasi[i])):
#        print("{:0.4f}".
#              format(data_populasi[i][j]))

#================== Perhitungan F Levene =======================
k = int(jumlah_populasi)
pembilang = 0
penyebut = []

sigma_pembilang = 0
sigma_penyebut = 0
for i in range (0,len(data_populasi)):
    sigma_pembilang += len(data_populasi[i])*(y_bar[i]-(rata_data_y_bar_keseluruhan))**2
    for j in range (0,len(data_populasi[i])):
        sigma_penyebut += (y_dikurangi[i][j] - y_bar[i])**2
#for i in range (jumlah_populasi):
#    pembilang += ((N - k)*(len(data_populasi[i])*(y_bar[i]-(y_bar_keseluruhan / jumlah_data_y_bar_keseluruhan))**2))
#    for j in range (len(data_populasi[i])) :
#        penyebut.append((k - 1)*((y_dikurangi[i][j]-y_bar[i])**2))

pembilang = (N-k)*sigma_pembilang
penyebut = (k-1)*sigma_penyebut
F_levene = pembilang / penyebut
print("\nF Levene = pembilang/penyebut",pembilang,"/",penyebut,"=",round(F_levene,4))

distribusi_f = st.f(k-1,N-k)
x = distribusi_f.ppf(1-float(alfa))
print("F dengan alfa =",str(alfa),",dfn =",str(k-1),",dan dfd =",str(N-k),"adalah"
      ,str(round(x,4)))



print("\n")
if F_levene > float(round(x,4)) :
    print("Karena F Levene > F tabel, H0 ditolak \nKesimpulan : Variansi tidak sama")
else :
    print("Karena F Levene < F tabel, H0 tidak dapat ditolak\nKesimpulan : Variansi sama")

