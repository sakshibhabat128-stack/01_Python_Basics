# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 17:24:31 2026

@author: YADNYESH
"""
with open('c:/2-Ad_python/pi_digits.txt','r')as file:
    contents = file.read()
print(contents)    
###############################
#to avoid this rstrip()method is used
with open('c:/2-Ad_python/pi_digits.txt')as file_object:
    contents = file_object.read()
    
print(contents.rstrip())    
####################
file_path = 'c:/2-Ad_python/pi_digits.txt'
with open(file_path)as file_object:
    contents = file_object.read()
print(contents.rstrip())    
#############3
#reading line by line
filename = 'c:/2-Ad_python/pi_digits.txt'
with open(filename)as file_object:
    for line in file_object:
        print(line)
##################
filename = 'c:/2-Ad_python/pi_digits.txt' 
with open(filename)as file_object:
    lines=file_object.readlines()#file object converted into list


lines
for line in lines:
    print(line.rstrip())       
#############################
filename = 'c:/2-Ad_python/pi_digits.txt'
with open(filename)as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()
        print(pi_string)
        print(len(pi_string))
##########
#Writing to a File
#One of the simplest ways to save data is to write it
#to a file.when you write text to a file
#the output will be
filename = 'c:/2-Ad_python/programming.txt'
with open(filename, 'w')as file_object:
    file_object.write("I am learning AI in AIGenius")
##################
#writing multiple lines
#the write() function doesn't add any newlines
filename = 'c:/2-Ad_python/programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I am learning AI in AIGenius.")
    file_object.write("I am really feeling that I am Genius")
################
09-02-26
#newline
filename ='c:/2-Ad_python/programming.txt'
with open(filename, 'w')as file_object:
    file_object.write("I am learning AI in AIGenius.\n")
    file_object.write("I am really feeling that I am Genius.\n")
###################
#Appending file
filename='c:/2-Ad_python/programming.txt'
with open(filename, 'a')as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
##########
#Error handling
filename='c:/2-Ad_python/pi_digits.txt'
try:
    with open(filename, 'r',encoding='utf8')as f:
        lines = f.readlines()
        for line in lines:
           print(line.rstrip())
except FileNotFoundError:
   print(f"Error:file '{filename}' not found.")
except PermissionError:
   print("Error: permission denied while accessing the file")           
#####################3
text = "मी AIGenius मध्ये skilling करत आहे आणि मला skilling करण्याचा आनंद होत आहे"
with open('sample_utf8.txt', 'w',encoding='utf-8')as f:
    f.write(text)

with open('sample_latin1.txt', 'w',encoding='latin-1',errors='replace')as f:
    f.write(text)
#all other file should also edited all file in2-Ad_python.txt
#################


