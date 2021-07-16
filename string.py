string = "Ini adalah string"
print(string, type(string))

# 1. Cara membuat string

'''
    1. Dengan menggunakan single quote '...'
    2. Dengan menggunakan double quote "..."
'''

string = 'ini pake single quote'
print(string)

string = "kalo ini pake double quote"
print(string)

print('"Hai, kamu apa kabar?"')
print("'Hai, kamu apa kabar?'")
print("sekarang hari jum'at")

# 2.Menggunakan tanda \

# membuat tanda ' menjadi string
print('hari ini hari jum\'at')

# backlash
print("c:\\user\\zaki ganteng")

# tab
print("zaki\t\t\tbambang, ini sangat jauhan")

# backspace
print("zaki \bbambang, ini deketan")

# newline
print("baris pertama.\nbaris kedua.") # LF -> ini biasa di pake di OS mac dan linux
print("baris pertama.\rbaris kedua") # CR -> ini di gunakan di b.programming dulu
print("baris pertama.\r\nbaris kedua.") # CRLF -> ini dipake di OS windows

# 3. String literal atau raw

# hati hati
print('C:\new folder') # ini akan salah pathnya

# Menggunakan raw string
print(r'C:\new folder') 

# multiline literal string dan raw
print(r"""
Nama saya adalah Zaki Ahmad Fitriawan
Saya adalah seorang programmer handal di bidang machine learning
jika anda tertarik dengan apa yang saya tawarkan bisa hubungi no di mana
""")
