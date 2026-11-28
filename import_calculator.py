# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 16:32:42 2026

@author: YADNYESH
"""
import calculator

print(calculator.add(5,3)) #output:8
print(calculator.sub(10,4)) #output:6
print(calculator.mul(6,7)) #output:42
print(calculator.div(8,2)) #output:4.0
######################
#main_script.py

from calculator import add

#Now you can add() directly without prefix
result = add(10,20)
print("Result:",result)
#######################
from calculator import add as summation

#using the alias(call function using alias name)
result = summation(15,20)
print("Result:",result)
##############

