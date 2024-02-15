# def my_function():
#     print("Selamat Pagi")
#     print("Selamat Pagi")
#     print("Selamat Pagi")
#     print("Selamat Pagi")
#     print("Selamat Pagi")

# def my_function_with_param(name):
#     print("Selamat Pagi " + name)
#     print("Selamat Pagi " + name)
#     print("Selamat Pagi " + name)
#     print("Selamat Pagi " + name)

# def my_function_with_two_params(name, jam):
#     print("Selamat Pagi " + name + ' ini sudah jam', jam)
#     print("Selamat Pagi " + name + ' ini sudah jam', jam)
#     print("Selamat Pagi " + name + ' ini sudah jam', jam)
#     print("Selamat Pagi " + name + ' ini sudah jam', jam)


# def sum_return(a, b):
#     return a + b

# def multiply(a, b):
#     return a * b

# # (5 + 2) * 10 = 70
# x = sum_return(5, 2) # x = 7
# y = multiply(x, 10) # y = 7 * 10 = 70
# print(y)


# APAKAH ANGKA "a" ADALAH BILANGAN GANJIL

def is_ganjil(a):
    return a % 2 != 0

# Cari semua bilangan ganjil dari a sampai b
def cari_semua_prima(a, b):
    ganjil_list = []
    for x in range(a, b):
        if is_ganjil(x):
            ganjil_list.append(x) 
    return ganjil_list


