class Car:
    def __init__(self, pax_count, car_mass, gear_count):
        self.pax_count = pax_count
        self.car_mass = car_mass
        self.gear_count = gear_count
        if self.pax_count > 5:
            print("IllegalCarError: too much allowed passengers!")
            exit()
        elif self.pax_count < 1:
            print("IllegalCarError: at least one passenger is required!")
            exit()
        elif self.car_mass > 2000:
            print("IllegalCarError: the car is too heavy!")
            exit()
    def print_car_spec(self):
        print(f"-Car specification: Passengers number: {self.pax_count}, Car mass: {self.car_mass}kg, Gear count: {self.gear_count}.")
    def total_mass(self):
        print(f"-total car mass: {self.car_mass + self.pax_count*70}kg")


def main ():
    #create instance of Car class
    c = Car(3, 1600, 5)

    c.print_car_spec()
    c.total_mass()

if __name__ == "__main__":
    main()