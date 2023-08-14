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
