# Operasi dan Manipulasi string

# 1. Menyambung string (concatenate)
nama_depan = "Zaki"
nama_tengah = "Ahmad"
nama_akhir = "Fitriawan"

nama_lengkap = nama_depan +" "+ nama_tengah +" "+ nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang_str = len(nama_lengkap)
print("Panjang dari " + nama_lengkap + " = " + str(panjang_str))

# 3. Operator untuk string

# mengecek apakah ada komponen char atau string pada string

karakter = "i"
status = karakter in nama_lengkap
print(karakter + ' ada di ' + nama_lengkap + ' = ' + str(status))

karakter = "I"
status = karakter in nama_lengkap
print(karakter + " ada di " + nama_lengkap + " = " + str(status))

karakter = "I"
status = karakter not in nama_lengkap
print(karakter + " tidak ada di " + nama_lengkap + " = " + str(status))

# Mengulang string
print("="*40)

# Indexing
print("index ke 19 =" + nama_lengkap[19])
print("index ke 0 =" + nama_lengkap[0])
print("index ke (-1) =" + nama_lengkap[-1])
print("index ke (-2) =" + nama_lengkap[-2])
print("index ke [0:4] =" + nama_lengkap[0:4])
print("index ke [0,2,4,6,....] =" + nama_lengkap[0:20:2])

# item paling kecil
print("paling kecil = " + min(nama_lengkap))
ascii_code = ord(" ")
print("ASCII code untuk spasi = " + str(ascii_code))

# item paling besar
print("paling besar = " + max(nama_lengkap))
ascii_code = ord("w")
print("ASCII code untuk w = " + str(ascii_code))

# 4. Operator dalam bentuk method
data = "Zaki Ahmad Fitriawan"
jumlah = data.count("a")
print("jumlah 'a' pada " + data + " = " + str(jumlah))