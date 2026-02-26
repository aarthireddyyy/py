def fun():
    print("hey")
fun()

def evenodd(x):
    if (x%2 == 0 ):
        print("even")
    else:
        print("odd")
evenodd(5)

#default arguements
def fun(x, y=50):
    print("x and y are ",x,y)
fun(78, 79)

#keyword arguements
def student(fname, lname):
    print(fname, lname)
student(fname = 'raja', lname ='ram')
student(lname= 'rama', fname='sweya')

#positional arguements
def nameage(name, age):
    print("hi ", name)
    print("age is", age)
nameage("suraj", 67)
nameage(90, "pintu")

#arbitary arguements
def myfun(*args, **kwargs):
    print("non-keywords arguements are : ",)
    for arg in args:
        print(arg)
    print("keyword arguments are :",)
    for key, value in kwargs.items():
        print(f"{key} == {value}")
myfun("hello", "word", first="basic", second="okay")

#functions in functions
def f1():
    print('outer')
    def f2():
        print('inner')
    f2()
f1()

#pass by reference and pass by value
def ref(x):
    x[0] = 20
lst=[10,19,18,17]
ref(lst)
print(lst)
#here the list is an mutable object it are writing a reference

def vall(x):
    x= 20

a=10;
vall(a)
print(a)
#here we are the passing a value to variable which is immutable 

#recursive functions
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(9))

##OOPS CONCEPTS IN PYTHON 
#class
class Animal:
    type = "dog"

    def __init__(self, name, typo):
        self.name = name
        self.typo = typo
Ani1 = Animal("Paru", "Parrot")
print(Ani1.type)
print(Ani1.name)
print(Ani1.typo)

#Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print('implementation of inheritance')
class Dog(Animal):
    def speak(self):
        print(f'{self.name} barks.')
class Cat(Animal):
    def speak(self):
        print(f'{self.name} meows.')

dog = Dog("ooreo")
cat = Cat("meawwww")

dog.speak()
cat.speak()

#Error Handling
n = 10 
try:
    res=n/0
except ZeroDivisionError:
    print("Cant divide by zero")

try:
    n = 120
    res = n/0
except ZeroDivisionError:
    print("error caught")
except ValueError:
    print("ranodm error")
else:
    print(res)
finally:
    print('this line prints anyways')

