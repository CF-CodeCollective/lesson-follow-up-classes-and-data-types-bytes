class Car:
  def __init__(self, year, make, model):
    self.year = year
    self.make = make 
    self.model = model

  def info(self, year, make, model):
    return year, make, model

kia = Car(2014, "Kia", "worm car which i do enjoy")
year, make, model = kia.info(2014, "Kia", "worm car which i do enjoy")
print(f"this is a {year} {make} {model}.")
