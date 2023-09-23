#This is printing in Python
print("Hello World")
print("My Name is Andrew")
#Identation
if 10>3:
    print("Ten is greater than three")
if 10>3:
    print("Ten is greater than three")
#variables
x = 5
y = "This is variable y"
z = 0.8
Z = 40
print(x)
print(y)
print(Z)
print(type(x))
print(type(y))
print(type(z))

#Assigning many values to multiple variables
r, s, t = "Ian", "Brian", "Nate"
print(r)
print(s)
print(t)

#Assign one value to multiple variables
a = b = c = "Volvo"
print(a)
print(b)
print(c)

#Unpack a collection
vehicles = ["Volvo","Toyota","BMW"]
q,w,e = vehicles
print(q)
print(w)
print(e)

#Numbers
y=100
p=25
s=y+p#addition
d=y-p#subtraction
f=y*p#multiplication
g=y/p#division
print(s)
print(d)
print(f)
print(g)

#Inputing numbers and doing calculations
#a = int(input("Enter First Number"))
#b = int (input("Enter Second Number"))
#c=a+b
#print("Addition of two numbers", c)

#python numbers
x = 5
y = 5.1
z = 5j
print(type(x))
print(type(y))
print(type(z))
#strings

e = "Andrew"
print(e)
print(type(e))

#multilinestring
f = """ My Name is Andrew
    First of His Name
    Leader of the Free World """
print(f)

t = "Hello World"
print(t[5])

#strings as arrays
for x in "banana":
    print(x)

#checkstringlength
p = "Kenya is the best"
print(len(p))

#check string
txt = "The Best things in Life are Expensive"
print("Expensive" in txt)
print("Free" in txt)

#Strings in if statements
txt = "The best things in life are Expensive"
if "Expensive2" in txt:
    print("Expensive is present")

#check if not
txt= "The best things in life are expensive"
print("free" not in txt)

#slicing strings
b = "  Hello, World  "
print(b[2:5])
print(b[:5])
print(b[5:])
#modify string
#upppercase
print(b.upper())
#lowecase
print(b.lower())
#Removewhitespace
print(b.strip())
#Replacestring
print(b.replace("H","K"))
#split string
print(b.split(","))

#stringconcatination
a = "Hello"
b = "World"
c= a+b
print(c)

#formatmethod
age= 20
txt = "My Name is Andrew and I am {}"
print(txt.format(age))

#Boolean
print(10>9)
print(10==9)
print(10<9)

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#Evaluate a string and a number
print(bool("Hello"))
print(bool(15))

#Evaluate two variables
a = "Hello"
b=15
c=0
d=""
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))

#print the answer to a function
def myfunct():
    return True
print(myfunct())

#modulus operator
a=17%3
print(a)

#Lists

thislist = ["apple","banana","cherry","orange","kiwi","lemon"]
print(thislist)
print(thislist[1])
print(thislist[-1])
print(thislist[-2])
#print range
print(thislist[2:5])
print(thislist[-3:-1])

#check if items exist
if "apple" in thislist:
    print("Apple is in this list")
else:
    print("Apple is not in this list")

#change item value

thislist[1]="Black Current"
print(thislist)
#insertmethod
thislist.insert(2,"watermelon")
print(thislist)
#appendmethod
thislist.append("watermelon")
print(thislist)

#extendlist method
tropical=["mango","passion","papaya"]
thislist.extend(tropical)
print(thislist)

#removemethod
thislist.remove("papaya")
print(thislist)

#popindex
thislist.pop(1)
print(thislist)

#Delete list
#del thislist
#print(thislist)

#clearmethod
thislist.clear()
print(thislist)

#tuple
thistuple = ("apple","banana","cherry")
print(thistuple)
print(len(thistuple))

#single tuple
thistuple=("watermelon",)
print(type(thistuple))

thistuple = ("apple","banana","cherry","watermelon","papaya","mango","maize","potato")
print(thistuple[1]) #access tuple items
print(thistuple[-1]) #negative indexing
print(thistuple[2:5]) #range of indexes
print(thistuple[-4:-1]) #range of negative indexes

#update  tuples
x= ("apple","banana","papaya")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#createaset
x={"apple","papaya","cherry"}
print(type(x))

#python dictionaries
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

#UserInput
#username = input("Enter your Username")
#print("Username is:"+username)

#Ifstatement
a = 20
b=100
if b>a:
    print("b is greater than a")

#elif - If the previous condition were not true, then try this condition
a = 55
b = 55
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")

#else-catches anything that isn't caught by preceding conditions
a = 500
b = 100
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater tha b")

#nestedif - if statement inside an if statement
x = 15
if x>10:
    print("Above ten")
    if x>20:
        print("and also above 20")
    else:
        print("but not above 30")

#while loop
i = 1
while i<6:
    print(i)
    i+=1

#break statement

i = 1
while i<6:
    print(i)
    if i == 3:
        break
    i+=1

#continue statement

i = 0
while i<6:
    i+=1
    if i == 3:
        continue
    print(i)

#else statement
i=1
while i <6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")

#for loops
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)

#looping through a string
for x in "banana":
    print(x)

#if else, break statement
for x in range(6):
    if x ==3: break
    print(x)
else:
    print("Finally finished")

#nested loops

adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)

#functions

def my_function():
    print("Hello from a function")
my_function()

#arguments
def my_function(fname):
    print(fname+" Refsnes")

my_function("Andrew")
my_function("Emily")
my_function("Ian")

#number of arguments
def my_function(fname,lname):
    print(fname+" "+lname)
my_function("Ian","Andrew")

#default parameter value
def my_function(country="Kenya"):
    print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#return values
def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#class

class Person:
    def __init__(self, name, age, height, weight, catch_phrase):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.catch_phrase = catch_phrase

p1 = Person("Ian",102,20,75,"Mambo ni matatu")

#print(p1.name)
#print(p1.age)
#print(p1.height)
#print(p1.weight)
print(p1.catch_phrase)

class person2:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name}{self.age}"

p1=person2("john",36)
print(p1)

class person3:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = person3("John", "Doe")
x.printname()

class Student(person3):
 x = Student("Mike", "Olsen")
 x.printname()



