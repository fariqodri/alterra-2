# hour = 15

# if hour < 12:
print("Selamat Pagi")
print("Selamat Pagi")
print("Selamat Pagi")
print("Selamat Pagi")
print("Selamat Pagi")
# If block

# elif hour < 18:
#     print("Selamat Sore")
# elif hour < 20:
#     print('Selamat petang')
# elif hour < 22:
#     print('Selamat malam')
# elif hour < 24:
#     print('Selamat istirahat')
# else:
#     print("Selamat dini hari")


v1 = 400 
v2 = 700 

# Nested if
if v1 == 400:
    if v2 == 700:
        print("Value of v1 is 400 and v2 is 700" )
    elif v2 == 800:
        print("Value of v1 is 400 and v2 is 800" )

if v1 == 400 and v2 == 700:
    print("Value of v1 is 400 and v2 is 700" )
elif v1 == 400 and v2 == 800:
    print("Value of v1 is 400 and v2 is 800" )


"""
BUATLAH SEBUAH CODE YANG MENERIMA 2 INPUT ANGKA: A DAN B
HITUNG HASIL PERKALIAN A DAN B, KEMUDIAN DI-PRINT
JIKA HASIL PERKALIANNYA GANJIL, PRINT JUGA TULISAN "GANJIL"
JIKA HASIL PERKALIANNYA GENAP, PRINT JUGA TULISAN "GENAP"

"""

a = int(input('Angka pertama'))
b = int(input('Angka kedua'))

hasil = a * b

print (hasil)

if hasil % 2 == 0:
    print ("genap")
else:
    print ("ganjil")


