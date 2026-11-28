# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 18:01:05 2026

@author: YADNYESH
"""
lst=[]
for num in range (0,20):
    lst.append(num)
print(lst)    
##########################
#we can write same method using list comprehension
lst=[num for num in range(0,20)]
print(lst)
#################################
names=['dada','mama','kaka']
lst=[name.capitalize() for name in names]#list comprehension
print(lst)
#############################
#list comrehension with if statement
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]

print(lst)
###########################
#list comprehension
evens = [num for num in range (10) if num%2==0]
print(evens)
####################################
#in iinterview such question are asked so for practice use all list question
#for practice
def  is_even(num):
    return num%2==0
lst=[num for num in range (10) if is_even(num)]#righthand side write it for if sentence

print(lst)
########################################3
#list comprehension for inside for
lst=[f"{x}:{y}"for x in range(3)for y in range(3) ]#righthand side if it is inside for loop 
print(lst)
#for x in range
#for y in range
#########################################
#set comprehension{}
set_one={x for x in range(3)}
print(set_one)
#####################
dict={x:x*x for x in range(3)}
print(dict)
############################################
#Generator Expression
sum_evens =sum(num for num in range(10) if num%2==0)
sum_evens
print(sum_evens)
################################3
#Generator
#it is another way of creating iterators
#in a simple way where
#it uses the keyword "yeild
#instead of returning it in a defined function
#generator are implemented using a function
gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)
#############################
gen=(x for x in range(3))
next(gen)
##############################
#Function which returns multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
        
range_even(6)
for num in range_even(6):
    print(num)         
###########################
gen=range_even(6)
next(gen)
next(gen)
#########################        
#Assignment
#let us hide password entered on screen
#chaining generator
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'        
passwords=["not-good","give'm-pass","00100-100"]

for password in hide(lengths(passwords)):
    print(password)        
####################################       
#Enumerate
#printing list with index
lst=["milk","Egg","Bread"]
for index in range(len(lst)):
    print(f"{index+1} {lst[index]}")
#same code be implemented using enumerate
lst=["milk","Egg","Bread"]
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")
##############################################
#use zip function
name=["dada","mama","kaka"]
info=[9850,6032,9785]
for nm,info in zip(name,info):
    print(nm,info)
###############################
#use zip function witn mis-match list
name=["dada","mama","kaka","baba"]
info=[9850,6032,9785]
for nm,inf in zip (name,info):
    print(nm,inf)
#it will not display excess mismatch item in name
#i.e.baba
###################################
##zip longest
from itertools import zip_longest
name=["dada","mama","kaka","baba"]
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info):
  print(nm,inf)  
######################################
#use of fill value instead none
name=["dada","mama","kaka","baba"]
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)
#####################
#use of all(),if all the values are
#true then it will produce output
lst=[2,3,-6,8,9]#values must be non-zero,+ve or -ve
if all(lst):
    print('all values are True')
else:
    print('there are null values')    
##############################################
lst=[2,3,0,8,9]
if all(lst):
   print('all values are true')
else:
   print('there are null values')
########################
#use of any(non-zero values)
lst=[0,0,0,0,0]
if any(lst):
   print('it has some values')
else:
   print('all values are null in the list.')
##############################
#count()
from itertools import count
counter=count()
print(next(counter)) 
print(next(counter))
print(next(counter))    
#############################
#noe lets start from 1
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))
################################
#cycle
#suppose you have repeted tasks to be done,then you can use this method
import itertools

instructions=("Eat","code","sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)
#########################
#repeat()
from itertools import repeat
for msg in repeat("keep patience",times=3):
    print(msg)
################################################### 
#combinations()
from itertools import combinations
players=['john','jani','janardhan']
for i in combinations(players,2):
    print(i)
#################################
 #permutation
from itertools import permutations
players=['john','jani','janardhan']
for seat in permutations(players,2):
    print(seat)
##################################
#product
from itertools import product
team_a=['Rohit','pandya','Bumrah']
team_b=['Virat','manish','Sami']
for pair in product(team_a,team_b):
    print(pair)
################################
age=[27,17,21,19]
adults=filter(lambda age:age>=18,age)

print([age for age in adults])
#################################
#Assigment operation
#This will only create a new variable with same refrence. modifying one
list_a=[1,2,3,4,5]
list_b=list_a
print('ID of old list:',id(list_a))
print('ID of new list:',id(list_b))
list_a[0] = -10
print(list_a)
print(list_b)
#########################################
old_list =[[1,2,3],[4,5,6],[7,8,'a']] #nested list
new_list = old_list

new_list[2][2] = 9

print('Old List:',old_list)
print('ID of Old List:',id(old_list))
print('New List:',new_list)
print('ID of New List:',id(new_list))
###################################
#shallow copy
#One level Deep.Modifying on level 1 does not affect the other list.
#use copy.copy(),or object-specific copy function/copy constructor.
import copy
list_a = [1,2,3,4,5]
list_b = copy.copy(list_a)

#not affects the other list
list_b[0] = -10

print('Old List:',list_a)
print('ID of Old List:',id(list_a))#ID3132738379584
print('New List:',list_b)
print('ID of New List:',id(list_b))#ID3132738374272
#address is diffrent
#################################################
#but with nested objects,modifying on level 2 or
#deeper does affect other!
#although address is different it is going to affect
#on second list
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.copy(list_a)

#affect the other!
list_a[0][0]=-10
print(list_a)
print(list_b)
print('ID of Old List:',id(list_a))#ID=3132738177152
print('ID of New List:',id(list_b))#ID=3132738384512
######################################################
#deep copies
#full independant clones.use copy.deepcopy().
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.deepcopy(list_a)
#not affect the other
list_a[0][0]= -10
print(list_a)
print(list_b)
print('ID of Old List:',id(list_a))#ID=3132738385280
print('ID of New List:',id(list_b))#ID=3132738392448
###########################################################








