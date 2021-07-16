# Operator dalam bentuk methods

## Merubah case dari string
# Merubah semua ke upper case
gretting = "hai bro!"
print('ini normalnya = ' + gretting)
gretting = gretting.upper()
print('ini uppernya = ' + gretting)

# Merubah semua ke lower case
salam = "Halo MamanK!"
print('ini normalnya = ' + salam)
salam = salam.lower()
print('ini lowernya = ' + salam)

## Pengecekan dengan isX methods
# contoh pengecekan lower case
gretting = "hai bro!"
apakah_lower = gretting.islower()
print(gretting + " is lower = " + str(apakah_lower))
apakah_upper = gretting.isupper()
print(gretting + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
huruf = "bambang"
apakah_alpha = huruf.isalpha()
print(huruf + " is alpha = " + str(apakah_alpha))

# isalnum()
alnum = "bambang123"
apakah_alnum = alnum.isalnum()
print(alnum + " is alnum = " + str(apakah_alnum))

# isdecimal()
desimal = "1000"
apakah_decimal = desimal.isdecimal()
print(desimal + " is decimal = " + str(apakah_decimal))

# isspace()
space = "   "
apakah_space = space.isspace()
print(space + " tab " + " is space = " + str(apakah_space))

# istitle()
judul = "Zaki Adalah Seorang Kapiten"
apakah_judul = judul.istitle() # Hasilnya akan boolean
print(judul + " is judul = " + str(apakah_judul))

## Mengecek komponen startswith() dan endswith()
cek_start = "Zaki Ahmad Fitriawan".startswith("Zaki")
print("start = " + str(cek_start))

cek_end = "Zaki Ahmad Fitriawan".endswith("Fitriawan")
print("End = " + str(cek_end))

# Penggabungan komponen join() split()
pisah = ["Zaki","Ahmad","Fitriawan"]
gabungan = " ".join(pisah)
print(pisah)
print(gabungan)

gabungan = "Zaki Ahmad Fitriawan"
print(gabungan.split())

# alokasi karakter rjust(), ljust(), center()
kanan = "SOAL 1".rjust(10)
print(":" +kanan+ ":")

kiri = "SOAL 2".ljust(10)
print(":" +kiri+ ":")

tengah = "Tengah".center(40,"=")
print(tengah)

# Kebalikannya --> Strip()
tengah1 = tengah.strip()
print(tengah1)