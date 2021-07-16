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
judul = ""