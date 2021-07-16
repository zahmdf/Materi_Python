# OPERATOR ASSIGNMENT
# operasi yang dapat dilakukkan dengan penyingkatan
# operasi ditambah dengan assignment 

a = 5 # ini adalah assignment
print('Nilai a =', a)

a += 3 # artinya sama aja kayak a = a + 3
print('Nilai a menjadi =',a)

a -= 3 # artinya sama aja kayak a = a - 3
print('Nilai a menjadi =', a)

a *= 2 # artinya sama aja kayak a = a * 2
print('Nilai a menjadi =', a)

a /= 2 # artinya sama aja kayak a = a / 2
a = int(a) # diubah ke integer
print('Nilai a menjadi =', a)

a **= 2 # artinya sama aja kayak a = a pangkat 2
print('Nilai a menjadi =', a)

a //= 3 # artinya sama jaja kayak a = a floor division 3
print('Nilai a menjadi =', a)

a %= 3 # artinya sama aja kayak a = a % 3
print('Nilai a menjadi =', a)

# OPERATOR BITWISE
# OR (|)
b = True
print('\nNilai b =', b)
b |= False
print('Nilai b |= False\nNilai b menjadi =',b)

# AND (&)
b = False
print('Nilai b =', b)
b &= True
print('Nilai b &= True\nNilai b menjadi =', b)

# XOR (^)
b = False
print('Nilai b =', b)
b ^= True
print('Nilai b ^= True\nNilai b menjadi =', b)

# SHIFTING
c = 0b0100
print('\nNilai c =',c, 'Binary = ', format(c,'04b'))

# Shift Right (>>)
c >>= 2
print('Nilai c >>= 2\nNilai c menjadi =', format(c,'04b'))

# Shift Left (<<)
c <<= 3
print('Nilai c <<= 3\nNilai c menjadi =', format(c,'04b'))

