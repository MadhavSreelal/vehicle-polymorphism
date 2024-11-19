class BMW:
    def __init__(self):
        self.fuel_type = "Petrol"
        self.max_speed = 200

    def fuel_type(self):
        print(f"Fuel type: {self.fuel_type}")

    def max_speed(self):
        print(f"Max speed: {self.max_speed}")

class Ferrari:
    def __init__(self):
        self.fuel_type = "Petrol"
        self.max_speed = 300

    def fuel_type(self):
        print(f"Fuel type: {self.fuel_type}")

    def max_speed(self):
        print(f"Max speed: {self.max_speed}")


def display_information(car):
    car.fuel_type()
    car.max_speed()

bmw_car = BMW()
ferrari_car = Ferrari()

display_information(bmw_car)
display_information(ferrari_car)
