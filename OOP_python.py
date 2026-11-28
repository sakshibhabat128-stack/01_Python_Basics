# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 17:13:40 2026

@author: YADNYESH
"""
#object-oriented programming(OOP) in python
#key concepts oop in
#1Class
#A blueprint for creating objects(a kind of template).
class circle:
                                   
    def __init__(self, x, y, r):
        self.x= x
        self.y= y
        self.r= r
    def circumference(self):
       return 2*3.14*self.r 
    
    def area(self):
        return 2*3.14*self.r*self.r
#creating an object of circle
a_circle =circle(2.0,2.0,1.0)
b_circle =circle(3.0,3.0,2.0)

#Accessing data and methods
print("Radius:",a_circle.r)
print("circumference:",a_circle.circumference())
print("Area:",a_circle.area())

#Accessing data and methods
print("Radius:",b_circle.r)
print("circumference:",b_circle.circumference())
print("Area:",b_circle.area())
#############    
#Encapsulation
'''concept:hiding internal data by making attributes
   private and exposing  '''
class circle:
  def __init__(self,x,y,r):
     self.__x = x  #private
     self.__y = y
     self.__r = r

  def get_radius(self):
     return self.__r 
   
  def set_radius(self,r):
     if r>0:
         self.__r =r
     else:
         print("Invalid radius")
         
#usage
c2 = circle(1,1,3)
print(c2.get_radius())
c2.set_radius(10)
#data is protected; direct access is avoided usig__r 
print(c2.get_radius())
###########
#inheritance
#base class
class circle:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
    def area(self):
        return 3.14*self.r**2 
    def circumference(self):
        return 2*3.14*self.r
    def display_info(self):
        print(f"Center:({self.x},{self.y}),Radius:{self.r}")         
        print(f"Area:{self.area():.2f}")
        print(f"Circumference:{self.circumference():.2f}")
        
#derived class
class coloredcircle(circle):
        def __init__(self,x,y,r,color):
            super().__init__(x,y,r)#call parent constructor
            self.color = color     #new property in child class
            
        #Overriding the display_info method
        def display_info(self):
            super().display_info()
            print(f"color:{self.color}")
#--------------------            
#usage
#--------------------
c1 = coloredcircle(0,0,5,"red")
c1.display_info()
##########################
#polymorphism
'''
polymorphism is one of the core  
  '''
class calculator:
    def add(self,a,b=0,c=0):
       return a + b + c
   
calc = calculator()
print(calc.add(5))  #output:5
print(calc.add(5,3)) #output:8
print(calc.add(5,3,2))   #output:10
'''
run-time polymorphism
also know as method overriding'''
##############Example
#method overriding
class Animal:
    def speak(self):
        print("Animal speaks")
        
class dog(Animal):
    def speak(self):
        print("Dog barks")
        
class cat(Animal):
    def speak(self):
        print("Cat meows")  
          
#polymorphism in action
for animal in [dog(),cat()]:
    animal.speak()
###########
        
        