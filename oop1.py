# Parent class atau superclass
class Vehicle:
    def __init__(self, wheels, engine_capacity, color, length, width):
        self.wheels = wheels
        self.engine_capacity = engine_capacity
        self.color = color
        self.length = length
        self.width = width
    
    def accelerate(self, speed):
        print(f'Accelerating to speed {speed} km/h')

    def brake(self, speed):
        print(f'Braking to speed {speed} km/h')

# Subclass
class Car(Vehicle):
    def __init__(self, wheels, engine_capacity, color, length, width, rear_camera):
        super().__init__(wheels, engine_capacity, color, length, width)
        self.rear_camera = rear_camera
    
    def buka_pintu(self, nomor_pintu):
        print(f'Pintu nomor {nomor_pintu} dibuka')

class Sedan(Car):
    def __init__(self, wheels, engine_capacity, color, length, width, rear_camera):
        super().__init__(wheels, engine_capacity, color, length, width, rear_camera)
    
    def buka_bagasi(self):
        print(f'Bagasi dibuka')

class Motorcycle(Vehicle):
    def __init__(self, wheels, engine_capacity, color, length, width, fuel_capacity):
        super().__init__(wheels, engine_capacity, color, length, width)
        self.fuel_capacity = fuel_capacity

mobil_biasa = Car(4, 1200, 'Merah', 5, 3, 2)
mobil_sedan = Sedan(4, 1200, 'Merah', 5, 3, 2)
motor = Motorcycle(2, 200, 'Hitam', 2, 0.5, 5)

def maju(kendaraan):
    print('Kendaraan akan melaju')
    kendaraan.accelerate(70)
    kendaraan.brake(0)
    print('Kendaraan akan berhenti')

maju(mobil_biasa)
maju(mobil_sedan)
maju(motor)