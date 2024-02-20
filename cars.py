class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        return self.year, self.make, self.model

if __name__ == "__main__":
    vehicle = car("Kia", "Sportage", "2014")
    x, y, z = vehicle.info()
    print(f"This car is a {x} {y} {z}.")