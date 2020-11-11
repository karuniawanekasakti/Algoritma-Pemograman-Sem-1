# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 10:25:32 2020

@author: user
"""

x=int(input("masukan nilai = "))
ratusan = (x //100)
puluhan = (x - ratusan * 100)//10
satuan =( x - ratusan * 100 - puluhan * 10 ) 
r = ratusan
p = puluhan
s = satuan
print("r*p+s =", r*p+s)





