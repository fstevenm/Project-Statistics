''' UJI Hipotesis Rata-rata 1 Populasi '''
''' n besar / kecil '''
import scipy.stats as st
import math
import matplotlib.pyplot
#import numpy as np

print("Selamat datang di program Uji Hipotesis Rata-rata 1 Populasi",
      "-- by:@fstevenm")
print("Diasumsikan X berdistribusi Normal dan Variansi populasi tidak\n")

n = int(input("Jumlah sampel : "))

if n < 30 :
    print("Karne ukuran sampel kecil, digunakan t-distribution")
    alfa = float((input("Tingkat Signifikansi: ")))

    miu0 = float(input("miu0 = "))
    print("\n")

    a = True
    while a == True :
        H0 = input("H0 (=,>=,<=) : miu ")
        if H0 == "=" :
            print("H1 : miu =/= miu_0")
            alfa = alfa/2
            a = False
        elif H0 == ">=" :
            print("H1 : miu < miu_0")
            a = False
        elif H0 == "<=" :
            print("H1 : miu > miu_0")
            a = False
        else :
            print("Masukkan yang benar\n")
            a = True
        
    data = input("\nApakah ada data-data (Ya/Tidak): ")
    if data == 'Ya' :
        data_list = []
        for i in range (1,n+1):
            data_i = float(input("Data ke {0} : ".format(i)))
            data_list.append(data_i)
        mean = sum(data_list)/len(data_list)
        
        s_2_sum= 0
        for i in range (len(data_list)):
            s_2_sum += (data_list[i]-mean)**2
        s = math.sqrt((s_2_sum)/(n - 1))
        
        print("\nRata-ratanya :",mean)
        print("Standar deviasinya :",s)
        
        t = (mean - miu0)/((s)/(math.sqrt(n)))
        print("t =",round(t,4))
        
    else :
        mean = float(input("Rata-rata nya : "))
        s = float(input("Standar deviasinya : "))
        
        t = (mean - miu0)/((s)/(math.sqrt(n)))
        print("\nt =",round(t,4))
        print("\n")

    #======================= distribusi t  dan KESIMPULAN   =======================
    if H0 == "=" :
        distribusi_t = st.t(n-1)
        t1 = float(distribusi_t.ppf(float(alfa)))
        t2 = -float(t1)
        print("t_({0})_(v={1}) =".format(alfa/2,str(n-1)),t1)
        print("H0 ditolak bila t<-t({0}) atau t>t({1})\n".
              format(alfa/2,alfa/2))
        if t < t1 :
            print("Karena",t,"<",t1,", H0 ditolak")
            print("\nKESIMPULAN : H0 Ditolak")
        elif t > t2 :
            print("Karena",t,">",t2,", H0 ditolak")
            print("\nKESIMPULAN : H0 Ditolak")
        else :
            print("Karena",t1,"<",t,"<",t2,", H0 tidak dapat ditolak")
            print("\nKESIMPULAN : H0 Diterima")
            
    elif H0 == ">=" :
        distribusi_t = st.t(n-1)
        t1 = (float(distribusi_t.ppf(float(alfa))))
        print("t_({0})_(v={1}) =".format(alfa,str(n-1)),t1)
        print("H0 ditolak bila t<-t({0})\n".format(alfa))
        if t < t1 :
            print("Karena",t,"<",t1,", H0 ditolak")
            print("\nKESIMPULAN : H0 Ditolak")
        else :
            print("Karena",t,">",t1,",, H0 tidak dapat ditolak")
            print("\nKESIMPULAN : H0 Diterima")
            
    elif H0 == "<=" :
        distribusi_t = st.t(n-1)
        t1 = -(float(distribusi_t.ppf(float(alfa))))
        print("t_({0})_(v={1}) =".format(alfa,str(n-1)),t1)
        print("H0 ditolak bila t>t({0})\n".format(alfa))
        if t > t1 :
            print("Karena",t,">",t1," ,H0 ditolak")
            print("\nKESIMPULAN : H0 Ditolak")
        else :
            print("Karena",t,"<",t1,", H0 tidak dapat ditolak")
            print("\nKESIMPULAN : H0 Diterima")
            

else :
    print("Karena ukuran sampel besar, berdasar TLP digunakan norm-distribution")
    alfa = float((input("Tingkat Signifikansi: ")))

    miu0 = float(input("miu0 = "))
    print("\n")

    a = True
    while a == True :
        H0 = input("H0 (=,>=,<=) : miu ")
        if H0 == "=" :
            print("H1 : miu =/= miu_0")
            alfa = alfa/2
            a = False
        elif H0 == ">=" :
            print("H1 : miu < miu_0")
            a = False
        elif H0 == "<=" :
            print("H1 : miu > miu_0")
            a = False
        else :
            print("Masukkan yang benar\n")
            a = True
        
    data = input("\nApakah ada data-data (Ya/Tidak): ")
    if data == 'Ya' :
        data_list = []
        for i in range (1,n+1):
            data_i = float(input("Data ke {0} : ".format(i)))
            data_list.append(data_i)
        mean = sum(data_list)/len(data_list)
        
        s_2_sum= 0
        for i in range (len(data_list)):
            s_2_sum += (data_list[i]-mean)**2
        s = math.sqrt((s_2_sum)/(n - 1))
        
        print("\nRata-ratanya :",mean)
        print("Standar deviasinya :",s)
        z = (mean - miu0)/((s)/(math.sqrt(n)))
        print("z =",round(z,4))
        
    else :
        mean = float(input("Rata-rata nya : "))
        s = float(input("Standar deviasinya : "))
        
        z = (mean - miu0)/((s)/(math.sqrt(n)))
        print("\nz =",round(z,4))
        print("\n")

    #======================= distribusi norm  dan KESIMPULAN   =======================
    if H0 == "=" :
        distribusi_n = st.norm
        n1 = float(distribusi_n.ppf(float(alfa)))
        n2 = -float(n1)
        print("z_({0}) = {1}".format(alfa/2,n1))
        print("H0 ditolak bila z<-z({0}) atau z>z({1})\n".
              format(alfa/2,alfa/2))
        if z < n1 :
            print("Karena",z,"<",n1,", H0 ditolak")
            print("\nKESIMPULAN : H0 Ditolak")
        elif z > n2 :
            print("Karena",z,">",n2,", H0 ditolak")
            print("\nKESIMPULAN : H0 Ditolak")
        else :
            print("Karena",n1,"<",z,"<",n2,", H0 tidak dapat ditolak")
            print("\nKESIMPULAN : H0 Diterima")
            
    elif H0 == ">=" :
        distribusi_n = st.norm
        n1 = float(distribusi_n.ppf(float(alfa)))
        print("z_({0}) = {1}".format(alfa,n1))
        print("H0 ditolak bila z<-z({0}\n)".format(alfa))
        if z < n1 :
            print("Karena",z,"<",n1,", H0 ditolak")
            print("\nKESIMPULAN : H0 Ditolak")
        else :
            print("Karena",z,">",n1,", H0 tidak dapat ditolak")
            print("\nKESIMPULAN : H0 Diterima")
            
    elif H0 == "<=" :
        distribusi_n = st.norm
        n1 = -(float(distribusi_n.ppf(float(alfa))))
        print("z_({0}) = {1}".format(alfa,n1))
        print("H0 ditolak bila z>z({0}\n)".format(alfa))
        if z > n1 :
            print("Karena",z,">",n1," ,H0 ditolak")
            print("\nKESIMPULAN : H0 Ditolak")
        else :
            print("Karena",z,"<",n1,", H0 tidak dapat ditolak")
            print("\nKESIMPULAN : H0 Diterima")

enter = input("\nTekan Enter untuk close program -- Terima Kasih")


#print(np.std(data_list,ddof=1)) #Stander deviasi N= n-1