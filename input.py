# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 02:05:20 2020

@author: OSMAN FATAW
"""

name = input("What Is Your Name ")

age = input("How Old Are You:")

drunker = input("Do You Drink?:").lower()

if drunker == "yes":
 drinkType= input("What Type of Drink Do You Take?")
 print("Welcome " + name + " You Are " + age + " years ")
else:
    print("You Are Inocent And Too Young")

