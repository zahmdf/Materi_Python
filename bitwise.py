# OPERATOR BITWISE, OPERASI BINER, BINARY

a = 9
b = 5 

# Bitwise OR (|)
c = a | b
print('\n====OR====\n')
print('Nilai =',a,', binary =',format(a,'08b'))
print('Nilai =',b,', binary =',format(b,'08b'))
print('------------------------------(|)')
print('Nilai =',c,', binary =',format(c,'08b'))

# Bitwise AND (&)
c = a & b
print('\n====AND====\n')
print('Nilai =',a,', binary =',format(a,'08b'))
print('Nilai =',b,', binary =',format(b,'08b'))
print('------------------------------(&)')
print('Nilai =',c,', binary =',format(c,'08b'))

# Bitwise XOR (^)
c = a ^ b
print('\n====XOR====\n')
print('Nilai =',a,', binary =',format(a,'08b'))
print('Nilai =',b,', binary =',format(b,'08b'))
print('------------------------------(^)')
print('Nilai =',c,', binary =',format(c,'08b'))

# Bitwise NOT (~)
c = ~a
print('\n====NOT====\n')
print('Nilai =',a,', binary =',format(a,'08b'))
print('------------------------------(~)')
print('Nilai =',c,', binary =',format(c,'08b'))
print('-------------------------------(^)')
d = 0b00001001
e = 0b11111111
print('Nilai =',e^d,', binary =',format(e^d,'08b'))

# Shifting

# Shift right (>>)
c = a >> 2
print('\n====SHIFT=RIGHT====\n')
print('Nilai =',a,', binary =',format(a,'08b'))
print('------------------------------(>>)')
print('Nilai =',c,', binary =',format(c,'08b'))

# Shift left (<<)
c = a << 2
print('\n====SHIFT=LEFT====\n')
print('Nilai =',a,', binary =',format(a,'08b'))
print('------------------------------(<<)')
print('Nilai =',c,', binary =',format(c,'08b'))
