import timeit as tm
from matplotlib import pyplot as plt

#fungsi iterasi
def Ajaib1(n):
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
    return a

#fungsi rekursif
def Ajaib2(n):  
    if n <= 1:
        return n
    else:
        return Ajaib2(n-1) + Ajaib2(n-2)
        
#catatan waktu dari kedua fungsi
r = range(1,101)
time_data = []
for i in r:
    mulai = tm.default_timer()

    x = Ajaib1(i)

    w = "{:.10f}" .format(tm.default_timer() - mulai)
    time_data.append(w)
    # print("Input {}, waktu {:.10f} detik" .format(i, time.default_timer() - mulai))

# print(time_data)
plt.plot(r, time_data)
plt.ylabel("Waktu .sec")
plt.show()