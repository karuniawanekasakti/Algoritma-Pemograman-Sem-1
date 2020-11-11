# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:53:44 2020

@author: user
"""

x = int(input())
ratusan = (x //100)
puluhan = (x - ratusan * 100)//10
satuan = (x - ratusan *100 - puluhan * 10)
jumlah = ( ratusan + puluhan + satuan)
print(jumlah)
