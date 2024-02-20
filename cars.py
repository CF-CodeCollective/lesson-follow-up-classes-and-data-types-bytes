# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class car():
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
        
    def info(self):
        return self.year, self.make, self.model
    
kia = car(2014, "Kia", "Sportage")
year, make, model = kia.info()
print(f"This car is a {year} {make} {model}")