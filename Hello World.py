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
a = int(input("Enter First Number"))
b = int (input("Enter Second Number"))
c=a+b
print("Addition of two numbers", c)
