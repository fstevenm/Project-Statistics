'''PROGRAM ANALISIS VARIANSI (Rata-Rata n Populasi -- Kalo Variansi sama dari uji
Levene test)'''

import scipy.stats as st
print(" H01 : miu sampe n sama semua (tidak ada pengaruh baris)")
print(" H11 : Tidak semua miu sama (ada pengaruh baris)\n")
print(" H02 : miu sampe n sama semua (tidak ada pengaruh kolom)")
print(" H11 : Ada miu yang tidak sama (ada pengaruh kolom)\n")

alfa = input("Tingkat Signifikansi : ")

jumlah_populasi = int(input("Jumlah Populasi : "))
#data_populasi = [[1.06,0.79,0.82,0.89,1.05,0.95,0.65,1.15,1.12],
#                 [1.58,1.45,0.57,1.16,1.12,0.91,0.83,0.43],
#                 [0.29,0.06,0.44,0.55,0.61,0.43,0.51,0.1,0.53
#                  ,0.34,0.06,0.09,0.17,0.17,0.6]]
data_populasi = [[60,65,67],[50,56,54],[75,76,78],
                 [67,70,75],[78,75,80],[45,40,65],
                 [53,52,67],[55,56,66]]


#JKT, JKK, JKG untuk menentukan f 
#=============================================
''' k = jumlah baris, n = jumlah kolom'''
x_kuadrat = 0
jumlah_nilai_T = []
jumlah_nilai_Tj = []
k = jumlah_populasi
nilai_T_masing_kuadrat = []
nilai_T_j_masing_kuadrat = []
nilai_T_j = []
N = 0

#if ukuran_sampel == "Ya" :
if True :
    n = len(data_populasi[0])
    for i in range (0,jumlah_populasi):
        for j in range (0,len(data_populasi[i])):
            x_kuadrat += (data_populasi[i][j])**2
#            print(x_kuadrat)
        jumlah_nilai_i = sum (data_populasi[i])
        jumlah_nilai_T.append(jumlah_nilai_i)
        nilai_T_masing_kuadrat.append((jumlah_nilai_i)**2)

    
    for i in range (0,len(data_populasi[i])):
        a = []
        for j in range (jumlah_populasi):
            a.append(data_populasi[j][i])
        nilai_T_j.append(a)
        jumlah_nilai_j = sum (nilai_T_j[i])
        jumlah_nilai_Tj.append(jumlah_nilai_j )
        nilai_T_j_masing_kuadrat.append((jumlah_nilai_j)**2)        
        
    
    print("Jumlah nilai Ti. =",jumlah_nilai_T)
    print("Jumlah nilai T.j =",jumlah_nilai_Tj)
    print("\n")
    
    jumlah_nilai_T_kuadrat = (sum(jumlah_nilai_T))**2
    JKT = x_kuadrat-((jumlah_nilai_T_kuadrat)/(n*k))
    print("JKT = :",round(JKT,4)
          ,", dengan derajat bebas",k-1+n-1+((k-1)*(n-1)))
    
    JKB = (sum(nilai_T_masing_kuadrat)/n) - ((jumlah_nilai_T_kuadrat)/(n*k))
    print("JKB = :",round(JKB,4),", dengan derajat bebas",k-1)
    
    JKK = (sum(nilai_T_j_masing_kuadrat)/k) - ((jumlah_nilai_T_kuadrat)/(n*k))
    print("JKK = :",round(JKK,4),", dengan derajat bebas",n-1)
    
    print("JKG = JKT-JKB-JKK = :",round(JKT-JKB-JKK,4)
          ,", dengan derajat bebas",(k-1)*(n-1))
    
    
    s1_2 = JKB/(k-1)
    s2_2 = JKK/(n-1)
    s3_2 = (JKT-JKB-JKK)/((k-1)*(n-1))
    print("\nRata-rata jumlah Kuadrat")
    print("s1^2 = {0}       s^2 = {1}      s^3 = {2} "
          .format(round(s1_2,4),round(s2_2,4),round(s3_2,4)))

    F1 = s1_2 / s3_2
    F2 = s2_2 / s3_2
    print("F1 hitung =",round(F1,4))
    print("F2 hitung =",round(F2,4))
    
    distribusi_f = st.f(k-1,(k-1)*(n-1))
    x1 = distribusi_f.ppf(1-float(alfa))
    print("F1 dengan alfa =",str(alfa),",dfn =",str(k-1),",dan dfd =",str((k-1)*(n-1)),"adalah"
          ,str(round(x1,4)))
    
    distribusi_f = st.f(n-1,(k-1)*(n-1))
    x2 = distribusi_f.ppf(1-float(alfa))
    print("F2 dengan alfa =",str(alfa),",dfn =",str(n-1),",dan dfd =",str((k-1)*(n-1)),"adalah"
          ,str(round(x2,4)))
    
#elif ukuran_sampel == "Tidak" :
#    for i in range (0,jumlah_populasi):
#        for j in range (0,len(data_populasi[i])):
#            x_kuadrat += (data_populasi[i][j])**2
##            print(x_kuadrat)
#        jumlah_nilai_i = sum (data_populasi[i])
#        jumlah_nilai_T.append(jumlah_nilai_i)
#        nilai_T_masing_kuadrat.append(((jumlah_nilai_i)**2)/len(data_populasi[i]))
#        
#        N_jumlah = len(data_populasi[i])
#        N += N_jumlah
#    
#    print("Jumlah nilai Ti. =",jumlah_nilai_T)
#    
#    jumlah_nilai_T_kuadrat = (sum(jumlah_nilai_T))**2
#    JKT = x_kuadrat-((jumlah_nilai_T_kuadrat)/(N))
#    print("JKT = :",round(JKT,4))
#    
#    JKK = sum(nilai_T_masing_kuadrat) - ((jumlah_nilai_T_kuadrat)/(N))
#    print("JKK = :",round(JKK,4))
#    
#    print("JKT - JKK = :",round(JKT-JKK,4))
#
#    s1_2 = JKK/(k-1)
#    s2_2 = (JKT-JKK)/(N-k)
#    print("\nRata-rata jumlah Kuadrat")
#    print("s1^2 = {0}       s^2 = {1}".format(round(s1_2,4),round(s2_2,4)))
#
#    F = s1_2 / s2_2
#    print("F hitung =",round(F,4))
#    
#    distribusi_f = st.f(k-1,N-k)
#    x = distribusi_f.ppf(1-float(alfa))
#    print("F dengan alfa =",str(alfa),",dfn =",str(k-1),",dan dfd =",str(N-k),"adalah"
#          ,str(round(x,4)))

#print(st.f.sf(2,2,12)) #p_value langsung ini bisa
print("\n")
print("{0}    {1}    {2}    {3}    {4}"
      .format("Sumber Variansi","Derajat Bebas",
              "Jumlah Kuadrat","Kuadrat Rata-rata",
              "Statistik f"))
print("     {0}               {1}              {2}             {3}           {4}"
      .format("Baris",k-1,round(JKB,4),round(s1_2,4),round(F1,4)))
print("     {0}               {1}              {2}             {3}           {4}"
      .format("Kolom",n-1,round(JKK,4),round(s2_2,4),round(F2,4)))
print("     {0}               {1}              {2}             {3}"
      .format("Galat",(k-1)*(n-1),
              round(JKT-JKB-JKK,4),round(s3_2,4)))
print("     {0}               {1}             {2}"
      .format("Total",k-1+n-1+((k-1)*(n-1)),round(JKT,4)))


print("\n")
if F1 > float(round(x1,4)) :
    print("Karena F1 hitung > F1 tabel, H01 ditolak")
else :
    print("Karena F1 hitung < F1 tabel, H01 tidak dapat ditolak")
    
if F2 > float(round(x2,4)) :
    print("Karena F2 hitung > F2 tabel, H02 ditolak")
else :
    print("Karena F2 hitung < F2 tabel, H02 tidak dapat ditolak")

