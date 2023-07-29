#Syntax-Identation
if 5 > 2:
 print("Five is greater than two")

#Variables
userAge=0
print(userAge)

#defining multiple variables in onego
userAge2, userName =22 , "Thor"
print(userAge2)
print(userName)

#Assigning same value to multiple variables
x = y = z = "Oranges"
print(x)
print(y)
print(z)

#unpacking lists to variables
fruits = ["Apple","Sugar Cane","Banana",512]
a,b,c,d = fruits
print(a)
print(b)
print(c)
print(d)

#GlobalFunction
s = "awesome"
def myfunct():
 print("Python is "+s)
myfunct()

#create a variable with the same name as the global variable
t = "awesome"
def myfunction():
 t="fantasic"
 print("Python is " +t)
myfunction()
print("Python is "+t)

#DataTypes
w=5 #integer
print(w)
print(type(w))

e=5.0 #float
print(e)
print(type(e))

t="cow" #string
print(t)
print(type(t))

u = 5j
print(5j)
print(type(u))

#randomnumberfunction
import random
print(random.randrange(1,10))

#This is a comment in one line
#This is a multi-line comment with docstrings
#print("Hello world")
#print("Hello universe")
#print("Hello everyone")
#"""