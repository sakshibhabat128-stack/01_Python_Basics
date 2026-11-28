# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 17:14:43 2026

@author: YADNYESH
"""
#Exception Handling
a=10
b=0
result =a/b
#Throws ArithmeticException: / by zero
#######################################################
#Zero Division Error
try:
    result = a/b
except ZeroDivisionError:
    print("Cannot divide by zero!")
#################################    
#index error
numbers=[1, 2, 3]
print(numbers[5])#raises IndexError:list index out of range    
try:
    print(numbers[5])
except IndexError:
    print("Index out of range!")
#############################################
#Handling Exception without naming them.
try:
    numerator=50
    denom=int(input("Enter the denominator ")) #enter 10.3 SECOND TIME 0
    quotient=(numerator/denom)
    print("Division performed successfully")
except ValueError:
    print("Only INTEGERS should be entered ")
except:
    print("OPPS....................SOME EXEPTION RAISED")
#####################################################################
#"HANDLING exception using try.........except.........eles"
try:
    numerator=50
    denom=int(input("Enter the denominator: "))#enter10 then0 then10.3
    quotient=(numerator/denom)
    print("Division performed successfully")
except ZeroDivisionError:
    print("Denominator as ZERO is not allowed")
except ValueError:
   print("Only INTEGERS should be entered")
else:
   print("The result of division operation is",quotient)    
################################################################
#"Handling exception using try...except....else......finally"
try:
    numerator=50
    denom=int(input("Enter the denominator"))#enter then10 then0 then10.3
    queotient=(numerator/denom)
    print("Division performed successfully")
except ZeroDivisionError:
    print("Denominator as ZERO is not allowed")    
except ValueError:
    print("Only INTEGERS should be entered")
else:
    print("The result of division operration is",queotient)
finally:
    print("OVER AND OUT")    
###############################################
with open('c:/2-Ad_python/pi_digits1.txt', 'r')as file:
        contents = file.read()
        print(contents.rstrip())
#############################################        
try:
    with open("c:/2-Ad_python/pi_digits1.txt", "r")as file:
        contents = file.read()
except FileNotFoundError:
    print("File not found")        
###################################################################################
#permissionError
with open("c:/2-Ad_python/pi_digits.txt")as file:
     content = file.read()
     print(content.rstrip())
##########################################################
try:
    with open("c:/2-Ad_python/pi_digits.txt")as file:
         content = file.read()
         print(content.rstrip())
except PermissionError:
    print("You don't have permission to access this file")      
###################################################
06-02-26
#Attribute Error
obj = None
print(obj.some_attribute) #Raise Attribute error   
############################
if obj is not None:
    print(obj.some_attribute)
else:
    print("object is None!")    
###################################
#Memory Error
huge_list =[1]*(10**10) #Raises MemoryError if system runs out of memory
####################
#Handling using Generator
def generator_numbers():
    for i in range(10**10):
        yield i #yield numbers one by one,preventing MemoryError
        
gen =generator_numbers()
print(next(gen)) 
#######################       
#Recursive function
def recursive_function():
    return recursive_function() #infinite recursion leads to recursive error

recursive_function()#raises recursiveerror
################
import sys
sys.setrecursionlimit(1000) #set Recursion limit to a safe value

def safe_recursive_function(depth=0,max_depth=10):
    if depth>= max_depth:
        return "Done"
    return safe_recursive_function(depth +1,max_depth)

print(safe_recursive_function())#works Safely
##############
#use case
#intial Balance
balance=500

def withdraw(amount):
    global balance #Allow modification of the global balance
    
    try:
        #check if the amount is valid number
        if not isinstance(amount,(int,float)):
            raise TypeError("Invalid amount type! Please enter a number.")
            
        #check if the amount is non-negative
        if amount<= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
            
        #check for insufficient balance
        if amount > balance:
            raise ValueError("Insufficient balance!")
            
        #dedcut amount
        balance -= amount
        print(f"Withdrawal successful! New balance:${balance:.2f}")
        
    except TypeError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Transaction Failed: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
        
#....Test Cases....
withdraw(100)    # Success
withdraw("fifty")#Error:Invalid amount type!
withdraw(-50)    #Error:Amount must be greater than zero.
withdraw(1000)   #Error:Insufficient balance!
#################################
def get_user_age():
    try:
        age =int(input("Enter the age:"))#convert input to integer
        
        if age<0:
            raise ValueError("Age cannot be negative!")
        elif age<18:
            raise ValueError("You must be at least 18 years old to proceed.")
            
            print("Access granted:")
    except ValueError as e:
        print(f"Invalid input:{e} ")
    except ValueError as e:
        print(f"Unexpected error:{e}")
#Test
get_user_age()

Test Case 1: valid adult age
Input:25
Excepted output :access granted!
reasoning :age is valid and >18

Test Case 2: underage
Input:17
Expected output: Invalid input:you must be at least 18 years old to proceed.
reasoning: age cant be negetive ,raises ValueError
    
Test case 3: non integer input
Input:"abc"
expected output:Invalid input:invalid literal for int() with base 10: 'abc'


#################
 
