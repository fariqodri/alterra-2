class Mobil:
    # Initialization
    def __init__(self, merk, color, length, width, seats, engine):
        self.merk = merk
        self.color = color
        self.length = length
        self.width = width
        self._seats = seats
        self.__engine = engine
        self.__odometer = 0
    
    def accelerate(self, speed):
        print(f'Accelerating car {self.merk} to speed {speed} km/h')
    
    def brake(self, speed):
        print(f'Breaking car {self.merk} to speed {speed} km/h')
    
    def tune_up(self, new_engine):
        self.__engine = new_engine
        print(f'Engine has been upgraded to {self.__engine}')
    
    def use(self, km):
        self.__odometer += km
    
    def get_odometer(self):
        return self.__odometer
    
    def __start_busi(self):
        print('Menyalakan busi')
    
    def __ignition(self):
        print('Membakar bensin')
    
    def __check_engine(self):
        print('Mengecek kondisi mesin')

    def start_engine(self):
        print('Masukkan kunci')
        self.__check_engine()
        self.__start_busi()
        self.__ignition()
        print('Mobil menyala')
    


m = Mobil('Hyundai', 'Merah', 5, 3, 4, 1200) # Instantiation
m.start_engine()

m2 = Mobil('Toyota', 'Biru', 5, 3, 4, 1200)



# Cat
# Fur = warna bulu
# Leg = panjang kaki (cm)
# Tail = panjang ekor (cm)

# Make sound = bisa meowing, purring, dst
# Eat = bisa makan dry food, wet food, dst
# Jump = lompat X cm

# 20.00