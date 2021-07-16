# Variabel adalah tempat menyimpan data

# Menaruh / Assignment Nilai
a = 5
b = 10

# Pemanggilan Pertama
print("Nilai a adalah: ", a)
print("Nilai b adalah: ", b)

# Penamaan Variabel
Namavariabel = "saya ganteng banget kaya bagong"
nama_variabel = "kamu jelek kaya badut ancol" # jangan ada underscore pada nama variabel, gunakanlah _ okey
namavariabel10 = 1000 # menambahkan angka pada variabel, angkanya tidak boleh di depan

# Pemanggilan kedua
print("Nilai b adalah: ", b)
b = 30
print("ini dia si b", b)

# Assignment indirect
a = b
print(b)

# Tipe Data
# a = 20 a adalah nama variabel sedangkan 20 adalah nilai dari variabel

# 1. Tipe Data: angka satuan yang tidak ada komanya (integer)
data_integer = 2000
print("Data : ", data_integer)
print("-Tipe Datanya adalah ", type(data_integer))

# 2. Tipe Data: angka dengan koma (float)
data_float = 0.5
print("Data : ", data_float)
print("-Tipe Datanya adalah ", type(data_float))

# 3. Tipe Data: kumpulan karakter (string)
data_string = "Bapak Bambang"
print("Data : ", data_string)
print("-Tipe Datanya adalah ", type(data_string))

# 4. Tipe Data: biner True/False (boolean)
data_bool = False
print("Data : ", data_bool)
print("Tipe Datanya adalah ", type(data_bool))

# Tipe Data Khusus

# 1. Bilangan Kompleks
data_kompleks = complex(2,3)
print("Data : ", data_kompleks)
print("-Tipe Datanya adalah ", type(data_kompleks))

#Tipe data dari bahasa C

from ctypes import c_double

data_c_double = c_double(10.5)
print("Data : ", data_c_double)
print("-Tipe Datanya adalah ", type(data_c_double))

# Kita belajar CASTING DATA 
# Merubah satu tipe data ke tipe data lain

## 1. INTEGER
print("====INTEGER====")
data_integer = 10;
print("data = ", data_integer, ",type =", type(data_integer))

data_float  = float(data_integer)
data_string = str(data_integer)
data_bool   = bool(data_integer) # akan false jika int = 0
print("data = ", data_float, ",type =", type(data_float))
print("data = ", data_string, ",type =", type(data_string))
print("data = ", data_bool, ",type =", type(data_bool))

## 2. FLOAT
print("====FLOAT====")
data_float = 10;
print("data = ", data_float, ",type =", type(data_float))

data_integer = int(data_float) # akan dibulatkan kebawah
data_string  = str(data_float)
data_bool    = bool(data_float) # akan false jika float = 0
print("data = ", data_integer, ",type =", type(data_integer))
print("data = ", data_string, ",type =", type(data_string))
print("data = ", data_bool, ",type =", type(data_bool))

## 3. STRING
print("====STRING====")
data_string = "0";
print("data = ", data_string, ",type =", type(data_string))

data_integer = int(data_string) # string harus angka
data_float   = float(data_string) # string harus angka
data_bool    = bool(data_string) # false jika string kosong
print("data = ", data_integer, ",type =", type(data_integer))
print("data = ", data_float, ",type =", type(data_float))
print("data = ", data_bool, ",type =", type(data_bool))

## 4. BOOLEAN
print("====BOOLEAN====")
data_bool = True;
print("data = ", data_bool, ",type =", type(data_bool))

data_integer = int(data_bool)
data_float   = float(data_bool)
data_string  = str(data_bool)
print("data = ", data_integer, ",type =", type(data_integer))
print("data = ", data_float, ",type =", type(data_float))
print("data = ", data_string, ",type =", type(data_string))

# INPUT USER

# data yang dimasukkan pasti string
data = input("Masukkan Data Anda: ")

print("Data= ", data, "Type= ", type(data))

# jika memasukkan data int dan float maka
angka = float(input("Masukkan Angka: "))

print("Angka = ", angka, "type = ", type(angka))

# jika boolean maka
biner = bool(int(input("Masukkan Data Biner: ")))

print("biner = ", biner, "type = ", type(biner))

# 5. LIST
data_list = [0, 1, 2, 3]
print('data=', data_list, 'type datanya adalah=', type(data_list))