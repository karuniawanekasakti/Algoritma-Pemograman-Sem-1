# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 10:06:29 2020

@author: user
"""

x=int(input("masukan nilai = "))
ratusan = (x //100)
puluhan = (x - ratusan * 100)//10
satuan =( x - ratusan * 100 - puluhan * 10 ) 
print("ratusan", ratusan)
print("puluhan", puluhan) 
print("satuan", satuan)

