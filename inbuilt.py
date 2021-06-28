# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 13:20:17 2020

@author: OSMAN FATAW
"""
female = "jane Doe"
male = "john doe"


print("Hello "+ female)
print("Hello "+female + " and " +male) 



amount = 4000.00


tax = 0.3

income_tax = amount * ( tax /100)
salary = (amount - income_tax)

print(female + " your income is " +str(salary))
