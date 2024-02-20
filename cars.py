# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
if __name__ == "__main__": 
    main()

class car():
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
        
    def info(self):
        return self.year, self.make, self.model
