# OPERASI KOMPARASI 
# setiap hasil dari operasi komparasi adalah boolean 

a = 10
b = 4

# LEBIH DARI (>)
hasil = a > 5
print(a,'>',5,'=', hasil)
hasil = b > 5
print(b,'>',5,'=', hasil)

# KURANG DARI (<)
hasil = a < 12
print(a,'<',12,'=', hasil)
hasil = b < 12
print(b,'<',12,'=', hasil)

# LEBIH DARI ATAU SAMA DENGAN (>=)
hasil = a >= 10
print(a,'>=', 10,'=', hasil)
hasil = b >= 10
print(b,'>=',10,'=', hasil)

# KURANG DARI ATAU SAMA DENGAN (<=)
hasil = a <= 4
print(a,'<=',4,'=', hasil)
hasil = b <= 4
print(b,'<=',4,'=', hasil)

# SAMA DENGAN (==)
hasil = a == 10
print(a,'==',10,'=', hasil)
hasil = a == 4
print(a,'==',4,'=', hasil)
hasil = b == 4
print(b,'==',4,'=', hasil)
hasil = b == 10
print(b,'==',4,'=', hasil)

# TIDAK SAMA DENGAN (!=)
hasil = a != 10
print(a,'!=',10,'=', hasil)
hasil = a != b
print(a,'!=',b,'=', hasil)

# semua hal di atas dapat bekerja pada sytax literal

# 'IS' sebagai komparasi object identity
# membandingkan memory atau objek
a = 4 # ini adalah assigment membuat object
b = 4
print('nilai a =',a, ',id =',hex(id(a)))
print('nilai b =',b, ',id =',hex(id(b)))
hasil = a is b
print('a is b =', hasil)

x = 5
y = 6
print('nilai x =',x, ',id =',hex(id(x)))
print('nilai y =',y, ',id =',hex(id(y)))
hasil = x is y
print('x is y =', hasil)


# 'IS NOT' adalah kebalikan dari is

a = 4 # ini adalah assigment membuat object
b = 4
print('nilai a =',a, ',id =',hex(id(a)))
print('nilai b =',b, ',id =',hex(id(b)))
hasil = a is not b
print('a is b =', hasil)

x = 5
y = 6
print('nilai x =',x, ',id =',hex(id(x)))
print('nilai y =',y, ',id =',hex(id(y)))
hasil = x is not y
print('x is y =', hasil)