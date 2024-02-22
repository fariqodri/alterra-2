# l = ['a', 'c', 'b', 'c']

# l1 = [
#     {
#         'name': 'John',
#         'age': 30,
#         'pendidikan': ['s1', 's2'],
#         'height': 180
#     },
#     {
#         'name': 'Jean',
#         'age': 35,
#         'pendidikan': ['s1', 's2'],
#         'height': 185
#     }
# ]

# d1 = {
#     'John': {
#         'name': 'John',
#         'age': 30,
#         'pendidikan': ['s1', 's2'],
#         'height': 180
#     },
#     'Jean': {
#         'name': 'Jean',
#         'age': 35,
#         'pendidikan': ['s1', 's2'],
#         'height': 185
#     }
# }

# d1['Jean']['height'] = 190
# print(d1)

# for i in range(0, len(l1)):
#     d = l1[i]
#     if d.get('name') == 'Jean':
#         d['height'] = 190

# print(l1)


# print(l[1])
# x = l.copy()
# y = l.copy()
# z = l.copy()

# x.sort()
# y.append('d')
# z.pop(2)

# print(l)

# l.sort(reverse=True)
# print(l)

# print('[BEFORE] x is:', x)

# l[0] = 'z'

# print('l is:', l)
# print('x is:', x)

# l = ['a', 'b', 'c', 'd', 'e']
# Urutkan supaya urutannya normal
# Elemen di index tengah berubah menjadi 'f'


# t = ('a', 'b', 'c')
# print(t[0])

# s1 = set(['a', 'b', 'c', 'c', 'd', 'd'])
# s2 = set(['d', 'e', 'f', 'f'])

# s3 = {{'c', 'd'}, {'c', 'd'}}
# print(len(s3))

# print('Union:', s1.union(s2))
# print('Intersection:', s1.intersection(s2))
# print('Difference:', s1.difference(s2))

# s2.add('z')
# print('Add', s2)

# s1.remove('d')
# print('Remove', s1)

# s1 = {'a', 'b', 'c'}
# s2 = {'b', 'c'}

# print(s1.issubset(s2))

# d = {
#     'name': 'John',
#     'age': 30,
#     'pendidikan': ['s1', 's2']
# }

# d['name'] = 'Jean'
# print(d)

# print(d.get('pendidikan')[1])

# print('Items:', d.items())
# print('Keys:', d.keys())
# print('Values:', d.values())
# d.setdefault('height', 178)
# print('Get:', d.get('weight', 60))
# print('name' in d)

mahasiswa = [
    {
        'name': 'Alex',
        'ipk': 3.5,
        'lulus': ['DE 1', 'DE 2']
    },
    {
        'name': 'Carter',
        'ipk': 3.0,
        'lulus': ['DE 3', 'DE 4', 'DE 1', 'DE 2']
    },
    {
        'name': 'Jean',
        'ipk': 3.2,
        'lulus': ['DE 10', 'DE 11', 'DE 2', 'DE 3']
    }
]

for m in mahasiswa:
    m['nilai'] = m['ipk'] * 25

# print(mahasiswa)

semua_matkul = set()
for m in mahasiswa:
    semua_matkul = semua_matkul.union(m['lulus']) # {DE 1, DE 2, DE 3, DE 4}

print(semua_matkul)

# for i in range(0, len(mahasiswa)):
#     m = mahasiswa[i]
#     m['nilai'] = m['ipk'] * 25

# print(mahasiswa)

# mahasiswa_nilai = []

# for i in mahasiswa:
#     nilai = i['ipk'] * 25
#     mhs_baru = i.copy()
#     mhs_baru['nilai'] = nilai
#     mahasiswa_nilai.append(mhs_baru)

# print(mahasiswa_nilai)




# 1. Tambahan data 'nilai', nilai = ipk * 25 -> Dictionary baru
# 2. Tunjukkan semua matkul yg mereka semua sudah lulus: DE 1, DE 2, 3, 4, 10, 11 -> List

# 20.50