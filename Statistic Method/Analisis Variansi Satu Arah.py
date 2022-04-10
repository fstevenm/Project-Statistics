'''PROGRAM ANALISIS VARIANSI (Rata-Rata n Populasi -- Kalo Variansi sama dari uji
Levene test)'''

import scipy.stats as st
print(" H0 : miu sampe n sama semua")
print(" H1 : Ada miu yang tidak sama\n")

alfa = input("Tingkat Signifikansi : ")

jumlah_populasi = int(input("Jumlah Populasi : "))
data_populasi = [[17.5,16.9,15.8,18.6],[16.4,19.2,17.7,15.4],
                 [20.3,15.7,17.8,18.9],[14.6,16.7,20.8,18.9],
                 [17.5,19.2,16.5,20.5],[18.3,16.2,17.5,20.1]]
#data_populasi = [[1.06,0.79,0.82,0.89,1.05,0.95,0.65,1.15,1.12],
#                 [1.58,1.45,0.57,1.16,1.12,0.91,0.83,0.43],
#                 [0.29,0.06,0.44,0.55,0.61,0.43,0.51,0.10,0.53,
#                  0.34,0.06,0.09,0.17,0.17,0.60]]
#data_populasi = [[42.5,39.3,39.6,39.9,42.9,43.6],
#                 [39.8,40.1,40.5,42.3,42.5,43.1],
#                 [40.2,40.5,41.3,43.4,44.9,45.1],
#                 [41.3,42.2,43.5,44.2,45.9,42.3]]

#data_populasi = []

ukuran_sampel = input("Ukuran sampel sama (Ya/Tidak) : ")

#for i in range(1,jumlah_populasi+1):
#    populasi_i = []
#    jumlah_data_i = int(input("Jumlah data populasi ke {0} : ".format(i)))
#    for j in range(1,jumlah_data_i+1):
#        data_j = float(input("Data ke {0} : ".format(j)))
#        populasi_i.append(data_j)
#    print("\n")
#    data_populasi.append(populasi_i)



#JKT, JKK, JKG untuk menentukan f 
#=============================================
x_kuadrat = 0
jumlah_nilai_T = []
k = jumlah_populasi
nilai_T_masing_kuadrat = []
N = 0

if ukuran_sampel == "Ya" :
    n = len(data_populasi[0])
    for i in range (0,jumlah_populasi):
        for j in range (0,len(data_populasi[i])):
            x_kuadrat += (data_populasi[i][j])**2
#            print(x_kuadrat)
        jumlah_nilai_i = sum (data_populasi[i])
        jumlah_nilai_T.append(jumlah_nilai_i)
        nilai_T_masing_kuadrat.append((jumlah_nilai_i)**2)
    
    print("Jumlah nilai Ti. =",jumlah_nilai_T)
    
    jumlah_nilai_T_kuadrat = (sum(jumlah_nilai_T))**2
    JKT = x_kuadrat-((jumlah_nilai_T_kuadrat)/(n*k))
    print("JKT = :",round(JKT,4))
    
    JKK = (sum(nilai_T_masing_kuadrat)/n) - ((jumlah_nilai_T_kuadrat)/(n*k))
    print("JKK = :",round(JKK,4))
    
    print("JKT - JKK = :",round(JKT-JKK,4))

    s1_2 = JKK/(k-1)
    s2_2 = (JKT-JKK)/(k*(n-1))
    print("\nRata-rata jumlah Kuadrat")
    print("s1^2 = {0}       s^2 = {1}".format(round(s1_2,4),round(s2_2,4)))

    F = s1_2 / s2_2
    print("F hitung =",round(F,4))
    
    distribusi_f = st.f(k-1,k*(n-1))
    x = distribusi_f.ppf(1-float(alfa))
    print("F dengan alfa =",str(alfa),",dfn =",str(k-1),",dan dfd =",str(k*(n-1)),"adalah"
          ,str(round(x,4)))
    
    print("\n")
    print(" {0}               {1}              {2}             {3}           {4}"
          .format("Sumber Variansi","Derajat Bebas",
                  "Jumlah Kuadrat", "RJK", "Statistik F"))
    print("{0}                   {1}                       {2}                   {3}           {4}"
          .format("AntarMesin(Kolom)",k-1,round(JKK,4),
                  round(s1_2,4),round(F,4)))
    print("      {0}                        {1}                       {2}                   {3}"
          .format("Galat",k*(n-1),round(JKT-JKK,4),
                  round(s2_2,4)))
    print("      {0}                        {1}                       {2}"
          .format("Total",k*(n-1)+k-1,round(JKT,4)))
    
    
    
elif ukuran_sampel == "Tidak" :
    for i in range (0,jumlah_populasi):
        for j in range (0,len(data_populasi[i])):
            x_kuadrat += (data_populasi[i][j])**2
#            print(x_kuadrat)
        jumlah_nilai_i = sum (data_populasi[i])
        jumlah_nilai_T.append(jumlah_nilai_i)
        nilai_T_masing_kuadrat.append(((jumlah_nilai_i)**2)/len(data_populasi[i]))
        
        N_jumlah = len(data_populasi[i])
        N += N_jumlah
    
    print("Jumlah nilai Ti. =",jumlah_nilai_T)
    
    jumlah_nilai_T_kuadrat = (sum(jumlah_nilai_T))**2
    JKT = x_kuadrat-((jumlah_nilai_T_kuadrat)/(N))
    print("JKT = :",round(JKT,4))
    
    JKK = sum(nilai_T_masing_kuadrat) - ((jumlah_nilai_T_kuadrat)/(N))
    print("JKK = :",round(JKK,4))
    
    print("JKT - JKK = :",round(JKT-JKK,4))

    s1_2 = JKK/(k-1)
    s2_2 = (JKT-JKK)/(N-k)
    print("\nRata-rata jumlah Kuadrat")
    print("s1^2 = {0}       s^2 = {1}".format(round(s1_2,4),round(s2_2,4)))

    F = s1_2 / s2_2
    print("F hitung =",round(F,4))
    
    distribusi_f = st.f(k-1,N-k)
    x = distribusi_f.ppf(1-float(alfa))
    print("F dengan alfa =",str(alfa),",dfn =",str(k-1),",dan dfd =",str(N-k),"adalah"
          ,str(round(x,4)))


    print("\n")
    print(" {0}               {1}              {2}             {3}           {4}"
          .format("Sumber Variansi","Derajat Bebas",
                  "Jumlah Kuadrat", "RJK", "Statistik F"))
    print("{0}                   {1}                       {2}                   {3}           {4}"
          .format("AntarMesin(Kolom)",k-1,round(JKK,4),
                  round(s1_2,4),round(F,4)))
    print("      {0}                        {1}                       {2}                   {3}"
          .format("Galat",N-k,round(JKT-JKK,4),
                  round(s2_2,4)))
    print("      {0}                        {1}                       {2}"
          .format("Total",N-1,round(JKT,4)))


#print(st.f.sf(2,2,12)) #p_value langsung ini bisa
print("\n")
if F > float(round(x,4)) :
    print("Karena F hitung > F tabel, H0 ditolak")
else :
    print("Karena F hitung < F tabel, H0 tidak dapat ditolak")


'''RUMUS CEPAT'''
#print(st.f_oneway(data_populasi[0],data_populasi[1],data_populasi[2]))