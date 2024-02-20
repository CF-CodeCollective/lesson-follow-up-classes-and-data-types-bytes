# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 18:07:43 2024

@author: lab40-204-4
"""

import random as camy

random_nums = []
def run():
    for i in range(50):
        x = camy.randint(1, 1000)
        while x in random_nums:
            x =  camy.randint(1, 1000)
        random_nums.append(x)
    return random_nums
    
print(run())
    