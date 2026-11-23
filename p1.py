# -*- coding: utf-8 -*-
# BASIC PYTHON
print("Hello World")
x=1
print(x)
print(type(x))
x=10000000000000000000000000
print(x)
print(type(x))
age= input("please enter your age")
print(type(age))
print(age)
age1=input("please enter your age")
print(type(age1))
print(age1)
age2=input("please enter your age")
print(type(age2))
print(age2)
#concatenate
age=age1+age2
print(age)
age=int(input("please enter your age:"))
print(type(age))
print(age)
#floating Point
exchange_rate=1.83
print(exchange_rate)
print(type(exchange_rate))

int_value=100

float_value=1.5
string_value='1.5'
float_value=float(int_value)
print('int valur as a float:',float_value)
print(type(float_value))
float_value=float(string_value)
print('string value as a float:',float_value)
print(type(float_value))
#complex number
c1=1
c2=2j
print('c1:',c1,'c2:',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)
#boolean value
all_ok=True
print(all_ok)
all_ok=False
print(all_ok)
print(type(all_ok))
#convert string into boolean
status=bool(input('ok is it confirmed'))
print(status)
print(type(status))
#arithmetic operation
home=10
away=15
print(home+away)

print(type(home+away))

print(10*4)
print(type(10*4))
goals_for=10
goals_against=7
print(goals_for-goals_against)
print(type(goals_for-goals_against))
#division
print(100/20)
print(type(100/20))
#if we want op of divison in int
print(100//20)
print(type(100//20))
#if we want only reminder using modules
print('Modules division 100%13:',100%13)
print('Modulus division 3%2:',3%2)
#power operator
a=5
b=3
print(a**b)
#assignment operator
x=0
x+=1#has the same behavior as x=x+1
print(x)
Winner=None
print(Winner is None)
#alternatively you can also write:
print(Winner is not None)
#flow of using control statement
num=int(input('enter a number:'))
if num >0:
    print(num)
#else if statement
num=int(input('enter yet another number'))
if num<0:
    print('its negative')
else:
    print('its not negative')
#use of elif
saving=float(input("enter how much you have in saving"))

#iteration
#while loop
count=1
print('starting')
while count<=10:
    print(count)
count+=1 
#for loop
print('print out values in a range')
for i in range(2,10):
    print(i)
    print('done')
    #
print('only print code if iteration completed')
num=int(input("enter a number to check for"))
for i in range(0,16):
    if i==num:
        break
    print(i)
    print('done')
    ######
    
for _ in range(0,10):
    print('.',end='')
    print()
#break loop statement
print('only print code if all iteation completed')
num=int(input('enter a number to check for:'))
for i in range(0,6):
    if i==num:
        break
    print(i,'',end='')
print('Done')
#location of print is changed
for i in range(0,6):
    if i==num:
        break
    print(i,'',end='')
    print('Done')
####odd number 
start, end=4,19
#iterating each number in llist
for num in range(start,end+1):
    #checking condition
    if num%2!=0:
        print(num,end=" ")
start,end=4,19
for num in range(start,end+1):
    if num%2==0:
        print(num,end=" ")
###############15/01/26
x,y,z=5,6,7
print(x)
print(y)
print(z)
x,y,z=5
print(x)
print(y)
print(z)      
##global variable
x="awesome"
def my_function():
    print("python is" +x)
my_function()
######
#global and local variable
x="awesome"
def my_function():
    x="fantastic"
    print("python is "+x)
my_function()
print("python is "+x)
############
#range data type
x=range(6)
print(x)
print(type(x))
####Dictionary data type
#it contain key value pair
x={"name":"Yogita","age":21} 
print(type(x))
##List
lst=[1,2,3]
print(lst)
print(type(lst))  
##tuple
tup=(1,2,3)
print(tup)
print(type(tup)) 
###set
set1={1,2,3}
print(set1)
print(type(set1))
####
#assinging value
x=1
y=2.3
z=2+3j#complex
print(type(x)) 
print(type(y))
print(type(z)) 
####typecasting
x=int(1.3)
print(x)
x=1
z=float(x)
print(z)
######string
str1="hello"
str2=2
str3=str1+str2
print(f"hello{str2}")
###multiple string
x='''This is python.It is very powerful'''
print(x)
###string slicing
x="""This is python.It is very powerful"""
print(x[2:8])
##slicing from the start
print(x[:3])
###slicing to the end
x="""This is python.It is very powerful"""
print(x[4:])
###negative indexing
#counting fron the end
s="python"
print(s[-1])#output:n
print(s[-2])#output:o
print(s[-6])#output:p
print(s[0:5:2])#output:pto 
#its skip 1 value
print(s[:5:2])#output:pto
#####
s="powerful"
print(s[-6:-2])#op:werf
#example of empty slice
print(s[-2:-6])#slicing move forward not backward 
###using negative steps
s[-2:-6:-2]
####reversing the string
s="python"
print(s[::-1])
print(s[-2:-6:-1])#(moves backward)
####mixing positive and negative indexing
s="python"
print(s[1:-1])#op:'ytho'(from index 1 to second last)
print(s[-5:5])#op:same as above
####16/01/26
x="""This is python.It is very powerfil"""
#modify string
print(x.upper())
#####
x=x.upper()
print(x.lower)

###
#remove white spaces from initial to end
x=" This is python "
x
print(x.strip())
x=" This is python "
x
print(x.lstrip())
#####
x="This is python "
x
print(x.rstrip())
x
####split function
x="Hello","Gello"
print(x.replace("Hello","Gello"))
###########
#use of split which replaces white spaces
x="Hello_world"
print(x.split("_"))
x='Hello World'
print(x.split(' '))
x='red-green-blue'
print(x.split('-'))
x='''This is python.It is simple to understand.Difficult to implement'''
print(x.split('.'))
#####sorting given colors in alphabetically
##write a python function that accepts a hyphen-seperated sequence of
##of colors as input and returns the colors in hyphen
##-seperated sequence after sorting them alphabetically
input_colors="red-blue-green-yello"
def sorted_colors(input_colors):
    string_split=input_colors.split('-')
    string_split
    sort=sorted(string_split)
    sorted_string='-'.join(sort)
    return sorted_string
sorted_alphabetic=sorted_colors(input_colors)
print(sorted_alphabetic)
#############
x="Hello world"
string1=x[::-2]
print(string1)
string1=x[::-1]
print(string1)
##########palindrome it return same in the reverse
def is_palindrome(input):
    if input=="":
        return "you entered wrong input"
    else:
        string=input[::-1]
        if string==input:
            return True
        return False
print(is_palindrome("step on no pets"))
##############################
#find method,Searches the string for a specified value and returns
#the position of where it was found

x="This is python and it is very powerful"
print(x.find("and"))
 
address='4/116 sundar Apartment,Suyognagar'
print(address.find('sundar'))
address[6:22]
##########
#string concatenate
x="hello"
y="world"
print(x+y)#it not gives space between
 #to add white space
print(x+" "+y)
#####
###string format
x=36
y="my name is Anthony"
print(x+y)#it will gives you an error
#because we cannot concatenate int with string
#so we have to use (f) function
print(f'my namr is Anthony and my age is {x}')
############
quantity=3
item_no=54
price=67
print(f"I want {quantity}pieces and item number is{item_no},its price is{price}")
##################################
##format function
my_order="I want{}pieces and item number is {},its price is {}"
print(my_order.format(quantity,item_no,price))
##########
quantity=3
item_number=54
price=67
my_order="I want {0}items and its item number is{1},its price is{2}"
print(my_order.format(quantity,item_number,price))
###escape charecter
#the escape character allows you to use double quotes when
##you normally would not be allowed
text="This is fun fair and it has got big "round rigo""
#it will show you AN error.
text="This is fun fair and it has got big\"round rigo\""
print(text)#this is allowed
###############
#python Boolean
print(10>9)
print(10<9)
print(10==10)
############
a=20
b=10
if(a>b):
    print("The a is greater than b")
else:
    print("b is greater than a")

############
#python operators
a=20
b=10
print(a==b)
#####
a=20
b=10
print(a!=b)
##########
####operator precendence
print(3*3+3/3-3)#7 3*3=9 +3/3=1 =10-3=7
"""Rules for mathematical operations
PEMDAS
p:paranthesis
E:Exponential
M:multiplication
D:division
A:addition
s:substraction"""
##########
a=20
b=10
#identity operators
print(a is b)
print(a is not b)
#####19/01/26
###python list
lst=["cherry","banana","apple"]
print(lst)
print(lst[0])
print(lst[2])
#list can store heterogenious data types
lst=["cherry",1,1.3]
print(lst)
#######
#append()adds an element at the end of the list
lst=["cherry","banana","apple"]
lst.append("mango")
print(lst)
########################
#clear removes all the elements from the list
lst=["cherry","banana","apple"]
lst.clear()
print(lst)
########3
#copy() method
#if we want to create another list and copy element from first one then we can use copy().

lst=["cherry","banana","apple"]
lst2=lst.copy()
print(lst2)
######
#count()return the number of times value repeated in the list
lst=["cherry","cherry","banana"]
lst.count("cherry")
####
#extend()add the element of lst to the the lst1 list
lst=[1,2,3]
lst1=[4,5,6]
lst=lst+lst1
print(lst)

#####using extend()
lst=[1,2,3]
lst1=[4,5,6]
lst.extend(lst1)
print(lst)
#####
#insert()method insert the value in given position
lst=["cherry","cherry","banana"]
lst.insert(1,"mango")
print(lst)
####
#pop()removes elements from specified position
lst=["cherry","cherry","banana"]
lst.pop(1)
print(lst)
##################
#remove()removes the item with the specied value
lst=["cherry","cherry","banana"]
lst.remove("cherry")
print(lst)
######
#we can reverse entities
lst=["cherry","cherry","banana"]
lst.reverse()
print(lst)
################
#sort()use for sort the list alphabetically
lst=["cherry","orange","banana"]
lst.sort()
print(lst)
########
#here we sort by lenth
words=["apple","banana","kiwi","cherry"]
sorted_words=sorted(words,key=len)
print(sorted_words)
######creating nested list
nested_list=[[1,2,3],["a","b","c"],[True,False]]
print(nested_list)
####accesing elements in nested list
nested_list[0][2]
nested_list[1][0]
#####accessing the first inner list
print(nested_list[0])

###
##accessing the last element of the last sublist
print(nested_list[-1][-1])
####
#modifying elements in nested list
nested_list[1][1]="z"
print(nested_list)
##iterating over nested list
for sublist in nested_list:
    print(sublist)
flat_list=[sublist for sublist in nested_list]#comprehension list
print(flat_list)   
###############
#using two for loops(iterate over element)
for sublist in nested_list:
    for item in sublist:
        print(item,end=" ")

##########
#list comprehension with nested list
#flattering of list
#where we want to display all sublist element in one list
flat_list=[item for sublist in nested_list for item in sublist]
print(flat_list)
###############
#adding an entire sublist
nested_list.append(["new","list"])
print(nested_list)
##############
##adding an element insid a sublist
nested_list[0].append(4)
print(nested_list)
########
#removing an element from sublist
nested_list[1].remove('z')
print(nested_list)
##########
#tuple
tup=("cherry","cherry","banana")
print(tup)
print(tup[2])
###once tup is created ,you cannot change its value
#tuples is unchangable
x=("apple","banana","cherry")
x[1]='kiwi'
#first convert into list
y=list(x)
y
y[1]="kiwi"
#convert list to tuple
x=tuple(y)
print(x)
#######################
#tuple can have different data types
x=("apple",2,"cherry")
print(x)

#####
#you can also accesstuples items by refering to the index number,inside []brackeet
x=("apple","banana","cherry")
print(x[1])
##################
#for join two or more tuples you can use the + operator
tuple1=("a","b","c")
tuple2=(1,2,3)
tup1=tuple1+tuple2
print(tup1)
##############
####20/01/26
i=1

while i<6:
     print(i)
     if(i==3):
         break
      i=i+1
##############
#continue to next iteration if i is 3
i=1
while i<6:
    i=i+1
    if(i==3):
        continue
    print(i)
#############
#ffor loop
fruits=["Apple","banana","cherry"]
for i in fruits:
    print(i)
    #######
#use of break statement
fruits=["Apple","banana","cherry"]
for i in fruits:
    print(i)
    if(i=="banana"):
        break
#########
fruits=["Apple","banana","cherry"]
for i in fruits:
    if i=="banana":
         break
    print(i)
###########   
fruits=["apple","banana","cherry"]
for x in fruits:
    if x =="banana":
        continue
    print(x)
##lambda function
def add(a):
    sum=a+10
    return sum
add(20)
##instead of above code #we use lambda function and reduce code
add=lambda a:a+10
print(add(20))
##map function(imp)
lst=[34,12,64,55,75,13,63]
sqr_lst=list(map(lambda x:(x**2),lst))
print(sqr_lst)
#########3
#filter function
#find out even numbers
lst=[34,12,64,55,75,13,63]
even_lst=list(filter(lambda x:(x%2==0),lst))
print(even_lst)
###########
#dictionary{}
dict1={"brand":"maruti","model":"2345","year":2011}
print(dict1)
print(len(dict1))
print(type(dict1))
############find value related model
dict1.get("model")#get use for when we pass key it will return value 
dict1.keys()
################
car={
"brand":"ford",
"model":"mustang",
"year":1964}
x=car.keys()
print(x)
###adding one more key and value
car["color"]="white"
car
x=car.keys()
print(x)
print(len(car))
########
#removing the dictionary element
car={
"brand":"ford",
"model":"mustang",
"year":1964
}
car.pop("model")
print(car)
#in above #pop(index)#in remove(entity name)
##Accessing only values of the dictionary
car={
"brand":"ford",
"model":"mustang",
"year":1964
}
for x in car:
    print(car[x])
####Accessing both keys and values in dictionary
for key,value in car.items():
    print("%s =%s" %(key,value))#%called as placeholder
for key,value in car.items():
    print(f"{key}:{value}")
#########
#copying dictionary

car={
"brand":"ford",
"model":"mustang",
"year":1964
}
car2=car.copy()
car2
##another way to make copy is to use the built in function
thisdict={
"brand":"ford",
"model":"mustang",
"year":1964
}
dict1=dict(thisdict)
dict1
#########
#nested dictionary++
our_family={
"child1":{
    "name":"ram",
    "DOB":"21-05-2008"
    },
"child2":{
    "name":"sham",
    "DOB":"01-01-2008"
    }

}
our_family
############
#21/01/2026
#dictionary method
#clear():remove all elements from the car list
car={
     "brand":"ford",
     "model":"mustang",
     "year":1964
     }
car.clear()
car
#####copy method
car={
     "brand":"ford",
     "model":"mustang",
     "year":1964
     }
x=car.copy()
print(x)
#######
#fromkey
x={
   'key1','key2','key3'}
y=0
thisdict=dict.fromkeys(x,y)
thisdict
####
#get():to get value of key
car={
     "brand":"TATA",
     "model":"siara",
     "year":2026
     }
car.get("model")
###########
##item():return the dictionary's key-value pairs
car={"brand":"ford",
     "model":"mustang",
     "year":1964
     }
car.items()#when you use items()you will get tuples
######
car.keys()#you will only get keys
#####Values():give you only values of the dict

car={"brand":"ford",
     "modecarl":"mustang",
     "year":1964
     }
car.values()
########
#update():insert an item to the dict
car={"brand":"ford",
     "model":"mustang",
     "year":1964
     }
car.update({"color":"white"})
car
#####
#if you want updation then also you can use
car={"brand":"ford",
     "model":"mustang",
     "year":1964
     }
car.update({"brand":"maruti"})
car
########33
#sort by keys
data={'b':2,'a':5,'c':1}#here the keys in random form
data.items()
sorted_by_keys=dict(sorted(data.items()))
print(sorted_by_keys)#it will arrange the keys
#####sort by values
data={'b':2,'a':5,'c':1}#here the keys in random form
sorted_by_values=dict(sorted(data.items(),key=lambda item:item[1]))
print(sorted_by_values)#it will arrange the values
########
sorted_dict={'banana':40,'apple':100,'grapes':120,'mango':200}
free_item_key=min(sorted_dict,key=sorted_dict.get)
free_item_value=sorted_dict[free_item_key]
print(f"you will get the lowest priced item'{free_item_key}'({free_item_value})for free.")
##maximum
sorted_dict={'banana':40,'apple':100,'grapes':120,'mango':200}
free_item_key=max(sorted_dict,key=sorted_dict.get)
free_item_value=sorted_dict[free_item_key]
print(f"you will get the higest priced item'{free_item_key}'({free_item_value})for free.")
########
#sorting in descending order
sorted_by_values_desc=dict(sorted(sorted_dict.items(),
                                  key=lambda item:item[1],reverse=True))
print(sorted_by_values_desc)
################
#summing values of the dictionary
dict1={'apple':'100','grapes':'120','mango':'200','banana':'40'}
total=0
for value in dict1.values():
    total=total+int(value)#here you did typecasting using int
print(total)
#############
dict1={'apple':'100','grapes':'120','mango':'200','banana':'40'}
#convert values in integer and sum of them
total_sum=sum(int(value)for value in dict1.values())
print(total_sum)
############
#concatenation of dictionary
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
dict1.update(dict2)
print(dict1)
dict1=dict1|dict3
print(dict1)
#############
#write a program to check if a given key is already exist
dict1={'a':20,'b':30}
print('a'in dict1)
########22/01/26
#function
#function without an argument
def my_function():
    print("hello from a function")
my_function()
#function with an argument
def my_function(name):
    print("Hello  "+name)
 my_function("ram")
######## 
#function with positional arguments
def my_function(name1,name2):
    print(name1+" "+name2)
    print(name1+" "+name2)
my_function("Hello","World")
my_function("World","Hello")
  #######Arbitraty arguments
 """if you do not know how many arguments that will be
 passed into your function,
 #add*before the parameter name""" 
def my_function(*args):
    print(args[0]+" "+args[2])
    
my_function("Tappu","Sonu","Goli")
########
#function with kwargs
def myfun(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} :{value}')
myfun(first_name='papalal',mid_name='mohanlal',last_name='goyal')
########
"""we use the kwargs"""
##function with default parameter
"""if we call the function without arguments,
it uses the default value such as in below 
eg: we give norway as ddefault value"""
def my_function(country="Norway"):
    print("I am from "+country)
my_function('Dubai')
my_function('swedan')
my_function('India')
my_function()#i am from norvey
my_function('brazil')
###########
#passing list as an arguments
fruits=["orange","banana","guava"]
def my_function(fruits):
    for x in fruits:
        print(x)
my_function(fruits)
####function with return value
#to llet a function return value,use the return statement
def my_function(x):
    y=x*5
   return y
my_function(5)
########d
def my_function(x):
    y=x*5
    z=x*7
    return(y,z)
my_function(5)##error
###pass function
def my_function():
    pass
my_function()
 ###########
   ##recursive function
   def factorial(x):
       if x==1:
           return 1
       else:
           return(x*factorial(x-1))
       factorial(3)
       factorial(6)
##########
def add(a):
    sum=a+10
    return sum
add(20)
####instead of above code
""" lambda() can take any number of arguments"""
add=lambda a:a+10
print(add(20))
###########
add=lambda a,b:a+b
print(add(5,6))
###############
text="python123"
print(text.isalpha())#false
print(text.isdigit())#false
print(text.isalnum())#true
############
#upper,lower
text1="HELLO"
text2="Hello123"
text3="12345"
count1=0
for i in range(len(text1)):
    if text1[i].isupper():
        count1=count1+1
print(count1)


count2=0
for i in range(len(text2)):
    if text2[i].islower():
        count2=count2+1
print(count2)


text3="12345"
count3=0
for i in range(len(text3)):
    if text3[i].isupper():
        count3=count3+1
print(count3)
###########
#pre_requisite to decorators
def plus_one(number):
    number1=number+1
    return number1
plus_one(5)
#####
#defining function in other function
def plus_one(number):
    def add_one(number):
        number1=number+1
        return number1
    result=add_one(number)
    return result
plus_one(5)
###########
#passing function as arguments to other function
def plus_one(number):
    result1=number+1
    return result1

def function_call(function):
    result=function(5)
    return result

function_call(plus_one)
###########################
#26/01/26
#26/01/26
#write program to calculate sum of digits in number
num=[1,3,5,8,10]
total=0
for i in range(len(num)):
    if num[i]%2==0 or num[i]%2!=0:
        total=total+num[i]
        print(total)
###############
##other Approach
total=sum(i for i in num if i%2==0) 
print(total)
###################33
total=sum(i for i in num if i%2==0 or i%2!=0) 
print(total)
####################
total=sum(i for i in num if i%2!=0) 
print(total)
#######################

#write a program to calculate sum of digit in a number
num=int(input('enter a number'))
total=0
while(num!=0):
    digit=num%10
    total=total+digit 
    num=num//10
    print(total)
#####################
#write a program to calculate sum of digits 
#which is multiple of 3
num=int(input('enter the number'))
total=0
while(num!=0):
    digit=num%10
    if digit in(3,6,9) :
        total=total+digit
        num=num//10
        print(total)
#####################
num=int(input('enter the number'))
total=0
while(num!=0):
    digit=num%10
    if digit in(2,3,5,7):
        total=total+digit
    num=num//10
    print(total)
################################333
#write program to count the number of digit in a number
num=int(input('enter the number'))
count=0
while(num!=0):
    digit=num%10
    count=count+1
    num=num//10
print(count)   
##################
#write a program to count the number of times given digit occured
num=int(input('enter the number'))##written test
digit=int(input('which number is to count'))
count=0
while(num!=0):
    if num%10==digit:
        count=count+1
    num=num//10
print(count)
###################
"""write to program to check the duck number
#the duck number is number having 0 in it
#1207 is duck number where as 1277 is not duck number"""
num=int(input('enter the number'))
is_duck=False
while(num!=0):
    digit=num%10
    if digit==0:
        is_duck=True
    num=num//10
if is_duck:
    print('The number is duck')
else:
    print('The number is not duck')
#####################
#write a program to reverse number    
num=int(input('enter the number'))
reverse_num=0
while(num!=0):
    digit=num%10
    reverse_num=reverse_num*10+digit
    num=num//10
print(reverse_num)
###########################
#another approach
num=int(input('entr the number'))
lst=[]
while(num!=0):
    digit=num%10
    lst.append(digit)    
    num=num//10
    print(*lst)#unfolding of list
#####################
#another approach
num=input('enter the number')[::-1]
print(num)
##########################
#28/01/26
#fibonacci series most imp
num=int(input('enter the number'))
n1,n2=0,1
print(n1,n2,end=' ')
for i in range(2,num):
    n3=n1+n2
    print(n3,end=' ')
    n1,n2=n2,n3
################
num=int(input('enter the number'))
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    for i in range(0,num):
        print(fib(i),end=' ')
##############################
#niven number(also called as harshad number)
num=int(input('enter the number'))
result=0
temp=num
while(num!=0):
    digit=num%10
    result=result+digit
    num=num//10
    if num%result==0:
        print('number is niven')
    else:
        print('number is not niven')
############################
#special number((a+b)+(a*b)=n)
num=int(input('enter the number'))
digit1=num%10
digit2=num//10
if num==((digit1+digit2)+(digit1*digit2)):
    print('number is special')
else:
    print('number is not special')
#####################################
#prime numbers
def prime_num(num):
    if num < 2: #handle edge case for number<2
       return 'The number is prime'
    for i in range(2,int(num**0.5)+1):#check visibility only upto sqrt
        if num%i==0:
            return('the number is not prime')
        else:
            return('the number is prime')#Only return after checking all cases
########################################
#bubble sort algorithm
for i in range(n -1):#number of passes
    for j in range(n -1-i):#last i elememnts are already in list
        if arr[j] > arr[j+1]:
         #swap if elemements in wrong order
         arr[j],arr[j+1]=arr[j+1],arr[j]Approach
         print(*arr)
###################
#array with repeated elements
lst=[4,5,2,4,3,2,1,5,6]
#remove duplicates using the set and convert back to list
unique_lst=list(set(lst))
unique_lst
#optional1:sort the result if neded
#unique_lst.sort()
#output the result
print("original array",lst)
print("array after eliminating duplicates:",unique_lst)
########################
#mario pyranid#IMP
for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print()
##################################
for i in range(4):
    for j in range(i+1):
        print("#",end=" ")
    print()
##############################
for i in range(4):
    for j in range(4-i):
        print("#",end=' ')
    print()
######################
#symmetric triangle
rows=4#height of the triangle
for i in range(rows):
    #print spaces to centre the triangle
    for j in range(rows-i -1):
        print(" ",end=" ")
#print the # character
    for k in range(i+1):
        print("#",end="  ")#extra space for better symmetric
    print()# move to the next line
 ##################################
 #29/01/26
 #read input size
  b=int(input())
  #read list element
  arr=list(map(int,input().split()))
  #create two seperate listd for even and odd number
  even=[]
  odd=[]
  #separate elements
  for num in arr:
      if num%2 ==0:
          even.append(num)
      else:
          odd.append(num)
  #combine even first,then odd
  result=even+odd
  print(*result)

  ###################################
  ##step 1: read the input time in HH:MM format
  time_input=input()
  #example input "05:39

  #step 2: split the input into hours and min
  hh,mm=map(int, time_input.split(':'))
  #"05:39"- ["05","39"]-hh=5,mm=39

  #step 3: intialize a counter to track min passed
  minutes_passed=0
  #this variable count hoe many minutes we move forword

  #step 4:keep looping until we find a palindrom time
  while True:
  #step 5: covert hr to 2 - digit string
      hh_str=str(hh).zfill(2)
      #5 - "05"
      #12 - "12"
  #step6: covert minutes to 2-digit string
      mm_str=str(mm).zfill(2)
      #7-"07"
      #45-"45"
  #step 7: combine hr and min
      time_str=hh_str + mm_str
      #example: "05"+"39"-"0539"
  #step 8:check if the time is palindrom
      if time_str == time_str[::-1]:
          #if time reads same forword and backword
          
          print(f"user will get power after {minutes_passed}minutes")
          #clear,meaningful output
          
          break
           #exit loop once answer is found
  #step 9: move forword by 1 minutes
      mm+=1 
      minutes_passed +=1 
  #step 10: handle minutes overflow
      if mm==60:
          mm =0
          hh+=1 
  #step 11: handle hr overflow (24-hr clock)       
  if hh==24:
      hh =0
  ###############
  #test case 1#input=  "wipro technologies"
  #test case 2
  #test case 3
  input1=  "AI 101 @Home  "
  #step 1:split into words
  words=input1.split()
  words
  #step 2: covert words into list of charechter
  char_lists =[list(word)for word in words]
  char_lists
  #step 3: count letters in each list
  letter_count=[len(chars)for chars in char_lists]
  letter_count
  #[5,12]
  print("charecter lists:",char_lists)
  print("letter count:",letter_count)
  def sum_digit(num):
      total=0
      while num!=0:
          last_digit=num%10
          total=total+last_digit #get the last digit
          num=num//10 #remove the last digit
      return total
  #for sum_digit(456)-
  #4+5+6=15
  #print(sum_digit(456))
  total=[sum_digit(i)for i in letter_count]
  total
  total_sum=0

  for i in total:
      total_sum=total_sum+i
  total_sum
  if (total_sum//10)!=0:
      total=sum_digit(total_sum)
      print(total)
  else:
      print(total_sum)

  #if total sum is two digit then
  ##################################
  #30/01/26
  #corner case1:empty string
  input1=""
  #split()->[]

