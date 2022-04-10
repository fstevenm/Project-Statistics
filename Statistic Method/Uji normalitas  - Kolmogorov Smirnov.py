#class Hero():
#    def __init__(self,pertama,kedua):
#        self.pertama = darah
#        self.kedua = armor
#    def serang(self,tahan):
#        self.tahan = self.tahan*2

from itertools import accumulate
import collections
import scipy.stats as st

kumpulan_data=[]

jumlah_data =input("Berapa jumlah data : ")
for i in range (int(jumlah_data)):
    print("data ke",i+1)
    data_i=input("\t")
    kumpulan_data.append(float(data_i))

#--------- Urutin data dan frekuensi kumulatif----------------
for i in range (len(kumpulan_data)):
    for j in range (i+1, len(kumpulan_data)):
        if kumpulan_data[i] > kumpulan_data[j]:
            kumpulan_data[i], kumpulan_data[j] = kumpulan_data[j], kumpulan_data[i]

print(kumpulan_data)
print("\n")

''' untuk frekuensi '''
from itertools import groupby
frek=[len(list(group)) for key, group in groupby(kumpulan_data)]

''' untuk tabel angka yang muncul sekali aja '''
counter = collections.Counter(kumpulan_data)
kumpulan_data2 = list(counter.keys())
print("Dataya adalah ",kumpulan_data2)
print("Frekuensi data",frek)

''' untuk frekuensi kumulatif '''
def accumu(lis):
    total = 0
    for x in lis :
        total += x
        yield total

frek_kum = list(accumu(frek))
print("Frekuensi kumulatifnya :",frek_kum)
#print(kumpulan_data[0])


#------------- Rata-rata & Standar Dev ----------------------
rata_rata = (sum(kumpulan_data))/(len(kumpulan_data))
print("\n")
print("Rata-ratanya :", rata_rata)

data_total = []
for i in range (len(kumpulan_data)):
    #print((kumpulan_data[i]-rata_rata)**2)
    data_total.append(((kumpulan_data[i]-rata_rata)**2))
standar_dev = (sum(data_total)/(len(kumpulan_data)-1))**0.5

print("\n")
print("Standar deviasinya :",standar_dev)
print("\n")


#------- Z_i
Z = []
for i in range (len(kumpulan_data2)):
    if standar_dev==0:
        print("standar deviasi 0, tidak bisa jadi pembagi")
        break
    Z.append((kumpulan_data2[i]-(rata_rata))/standar_dev)
print("Z_i berturut-turut adalah",Z,"\n")    


F_o=[]
for i in range (len(Z)):
    #st.norm.ppf(0.95)
    F_o.append(st.norm.cdf(Z[i]))
print("F_0 nya adalah :", F_o)

#============= F_n (x) ============
F_n=[]
for i in range (len(kumpulan_data2)):
    F_n.append(frek_kum[i]/len(kumpulan_data))
print("F_n nya adalah :",F_n)


#======= Menghitung D nya ============
perbedaan = []
for i in range (len(kumpulan_data2)):
    perbedaan.append(abs(F_o[i]-F_n[i]))

print("\n Selisih antara F_0 dan F_n adalah",perbedaan)
print("Selisih yang paling besar adalah",max(perbedaan))