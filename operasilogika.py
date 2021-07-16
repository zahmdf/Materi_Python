# OPERASI LOGIKA ATAU BOOLEAN

# ada NOT, OR, AND, XOR

# NOT
print('====NOT====')
a = False
c = not a
print('Data a =',a)
print("NOT")
print('Data c =',c)

# OR (|) (jika salah satu nilai terpenuhi atau true, maka hasilnya = true)
print('====OR====')
a = False
b = False
c = a | b
print(a,'OR',b,'=',c)
a = False
b = True
c = a | b
print(a,'OR',b,'=',c)
a = True
b = False
c = a | b
print(a,'OR',b,'=',c)
a = True
b = True
c = a | b
print(a,'OR',b,'=',c)

# AND (&) (jika hanya satu yang terpenuhi atau true, maka hasilnya = false)
print('====AND====')
a = False
b = False
c = a & b
print(a,'AND',b,'=',c)
a = False
b = True
c = a & b
print(a,'AND',b,'=',c)
a = True
b = False
c = a & b
print(a,'AND',b,'=',c)
a = True
b = True
c = a & b
print(a,'AND',b,'=',c)

# XOR (^) (akan true jika salah satu true, sisanya false)
print('====XOR====')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

