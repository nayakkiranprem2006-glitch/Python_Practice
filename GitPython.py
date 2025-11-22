import time

# 1. Exit on negative number  
# Write a while loop that keeps asking the user to enter a number. If the user enters a negative number, use break to stop the loop.a = int(input("Enter a Number :"))
'''a = int(input("Enter a New Number :"))
while(a >= 0):
        if (a < 0):
            break
        
print("Game Over")'''

# 2. Skip even numbers  
# Use a while loop to print numbers from 1 to 10, but use continue to skip even numbers

'''a = 1
while a < 100000:
    if a%2 == 0:
        a += 1
        continue
    else:
        print (a)
        a += 1
    
print("Game Over")'''

# 3. Password retry system  
# Create a while loop that asks for a password. If it's incorrect, ask again. If it's correct, print “Welcome” and break. (You can use a counter to prevent infinite loops if you want.)

'''a = 5798
b = int(input(" ENTER THE PASSWORD :"))
while a != b:
    print("WARNING : Incorrect Password")
    b = int(input("Re-enter Password :"))
    if a == b:
        break

print("!! WELCOME !!")'''

# 4. Skip multiples of 3  
# Print numbers from 1 to 20 using a while loop. Skip numbers that are multiples of 3 using continue.

'''a = 0
while a <= 20:
    a += 1
    if a % 3 == 0:
        continue
    print(a)

print("The End !!")'''

# 5. Stop at a specific word  
# Write a while loop that takes words from the user. Stop the loop if the user types "stop" using break.

'''a = input(" Enter the word:")
while a !="stop":
    a = input("Enter another word :")
    if a == "stop":
        print("game over")'''

# 6.Problem: Print numbers 1 to 10 (skip 5)  
# Use a for loop to print numbers from 1 to 10, but skip number 5 using continue.

'''for i in range(1,11):
    if i == 5:
        continue
    print(i)'''

# 7.Problem: Sum of odd numbers from 1 to 20  
# Write a for loop to calculate and print the sum of all odd numbers between 1 and 20.
'''a = 0
for i in range(1,21):
    if i % 2 == 0:
        continue
    a += i

print (a)'''

# 8.Challenge: Print all numbers from 1 to 30 except multiples of 4  
# Write a for loop that prints numbers 1 to 30, but skip (don’t print) multiples of 4 using continue.

'''for i in range(1, 31):
    if i % 4 == 0:
        continue
    print(i)'''

# 9.Challenge: Use a for loop to print numbers from 1 to 50,  
# but stop the loop completely if you encounter a number divisible by both 5 and 7 (use break), and skip all even numbers (use continue).

'''for i in range(1, 51):
    if i%2 ==0:
        continue
    if i%5 == 0 and i%7 == 0:
        break
    print(i)'''

# 10.Challenge: Count how many numbers (1 to 100) are not divisible by 3 or 5  

'''count = 0
for i in range(1, 101):
    if i%3 != 0 and i%5 != 0:
        count += 1

print(count)'''

# 11.Write a function to find the length of the list

'''countries = ["America", "England", "Poland", "Thailand", "Russia", "India"]
religions = ["Hindu", "Muslim", "Sikh", "Isai"]

def length(list):
    print(len(list))

length(countries)
length(religions)'''

#12.Write a function to print the elements of list

'''countries = ["America", "England", "Poland", "Thailand", "Russia", "India"]
religions = ["Hindu", "Muslim", "Sikh", "Isai"]

def ele(list):
    for i in list:
        print(i, end=" ")

ele(countries)'''

# 13.Write a function to find the factorial of n . (n is the parameter and take it as an input)

'''n = int(input("Enter the Value :"))
def calc_fact():
    fact = 1
    for i in range(1, n +1):
        fact *= i
    print(fact)

calc_fact()'''

# 14.Write a Function to convert USD Currency into INDIAN Currency

'''def calc():
    n = int(input("How much USD Dollars you have ? "))
    cal = n * 83
    print(n,"USD_VAal = ", cal, "INR_Val")

calc()'''

# 15.WAF to detect the value n is odd or even. (n should be take as an input)

'''def check():
    n = int(input("Enterr the number :"))
    if n%2 == 0:
        print("The value Of", n, "is EVEN.")
    else:
        print("The value Of", n, "is ODD.")

check()'''

# 16. Sum of two numbers  
# Write a function add(a, b) that returns the sum of two numbers. 

'''def sum(a, b):
    s = a + b
    print(s)

sum(65, 86)'''

# 17. Find maximum of three numbers  
# Write a function maximum(a, b, c) that returns the largest among three numbers.

'''def check_max(a, b, c):
    s = 0
    if a > b and a>c:
        s = a
    elif b > a and b > c:
        s=b
    else:
        s = c
    print(s)

check_max(3,5,9) '''

#18. Task: Write a function count_vowels(s) that takes a string and returns 
# the number of vowels (a, e, i, o, u) in it.  
# (Both lowercase and uppercase should be counted.)

'''list = ["a","e", "i", "o", "u","A","E","I","O","U"]

def count_vowel():
    n = input("Enter a String :")
    cout = 0
    for i in n:
        if i in list:
            cout += 1
    
    print(cout)

count_vowel()'''

# 19.Task: Reverse a string  
# Write a function reverse_string(s) that returns the reverse of the input string.

'''def recursion():
    char = input("Enter Word :")
    rec = char[:: -1]
    
    print(rec)
     
recursion()'''

# 20. Task: Palindrome Checker
# Check the input is palindrome or not

'''def palindrome(s):
    char = s[::-1]
    if char == s:
        print("Yes,", s, "is Palindrome.")
    else:
        print("No,", s, "is not Palindrome.")
    
palindrome("Hello")
palindrome("madam")'''

# 21. Task: Count digits in a string
# Write a function which counts the elements of the string


'''def count_digits(s):
    cout = 0
    for char in s:
        if char.isdigit():
            cout += 1
            print(char)
    print("The number of digit is ", cout)

count_digits("Hello World 5645!")'''


# 22. Write a function to show the recursion from 9 to 0

'''def recursion(n):
    if n==-1:
        return 0
    print(n, end=", ")
    recursion(n-1)

recursion(9)'''

# 23. Calculate the nth Fibonacci number
# Write a recursive function to find the nth Fibonacci number.  
# (Sequence: 0, 1, 1, 2, 3, 5, 8, ...)

# 24. Sum of Digits  
# Write a recursive function that returns the sum of digits of a number.  
# (E.g., 123 → 1 + 2 + 3 = 6)

'''def sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum(n // 10)

print(sum(3823))'''

# 25. Power Calculation  
# Write a recursive function to compute a^b (a raised to the power b). (E.g., 2^3 = 8)
    
'''def func(a,b):
    if b == 0:
        return 1
    else:
        return a* func(a,b-1)
    
print(func(3,3))'''

# 26. Count Down  
# Write a recursive function that prints numbers from n to 1.  
# (E.g., input: 5 → output: 5 4 3 2 1)

'''def func(n):
    if n == 0:
        return 0
    else:
        print(n, end=" ")
        return func(n-1)
    
func(9)'''

# 27. Fibonacci Term  
# Write a recursive function to return the nth term of the Fibonacci series.  
# (E.g., fibo(6) → 8)

'''def func(n):
    a, b = 0, 1
    if n == 0:
        return 0
    elif(n == 1):
        return 1
    else:
        return func(n-1) + func(n- 2)

print(func(5))'''

# 28. Write a code for fibonacci series by using loop. 

'''n = int(input("Enter how many terms you want: "))

a = 0
b = 1

print("Fibonacci Series:")
print(a, end=' ')
for i in range(n - 1):
    print(b, end=' ')
    a, b = b, a + b'''

# 29. Reverse a String (Recursion)  
# Write a recursive function that takes a string and returns its reverse.  
# Input: "hello" → Output: "olleh"

'''def func(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1]+ func(s[:-1])
    
print(func("Hello"))'''

# 30. Write a recursive function to find the GCD (HCF) of two numbers using Euclid's algorithm.  
# Input: gcd(20, 8) → Output: 4

'''def func(a, b):
    if b == 0:
        return a
    else:
        return func(b,a%b)
    
print(func(45,27))'''

# 31. Write a recursive function to print all elements in a list.
# (use list & index as parameter)

'''def func(n):
    jkl = ["Om Prakash", "Jhallu", "Pravesh", "Mukesh", "silsila"]
    if n == len(jkl):
        return ""
    else:
        return jkl[n] +" " + func(n+1)

print(func(0))'''

# 32. Check Palindrome (Recursion)  
# Write a recursive function to check whether a string is a palindrome.  
# Input: "madam" → Output: "Yes"  
# Input: "hello" → Output: "No"

'''def func(s):
    x = s[::-1]
    if len(s) == 0:
        return ""
    elif(s == x):
        print("Input :",s, "--> Output : Yes")
    else:
        print("Input :",s, "--> Output : No")

func("Naman")'''

# 33. Create a text file named *data.txt* and write the following lines into it:
# Python is fun.
# Learning Python is interesting.
# Python is powerful.

'''with open("data.txt", "w") as f:
    data = f.write("Python is fun.\nLearning Python is interesting.\nPython is powerful.")'''

# Part 2: reading and counting how many times "Python" appears.

'''with open("data.txt", "r+") as f:
    data = f.write("Python is fun.\nLearning Python is interesting.\nPython is powerful.\n Python Python Python")

word= "Python"
count = 0
with open("data.txt","r") as f:
    for line in f:
        if word in line:
            count += line.count(word)

print(count)'''

# 34 Write a program that asks the user to enter a word, then checks if that word exists in the file data.txt.  
# → Print “Found” or “Not Found”.

'''with open("data.txt", "w") as f:
    data = f.write("Hello Everyone.\nThis is Data.txt file.\nThank You !")

word = input(" Enter the word :")

found = False
with open("data.txt", "r") as f:
    for line in f:
        if word in line:
            found = True
            break

if found:
    print(" Found !!")
else:
    print(" Not Found !!")'''

# 35. Copy File Content
# Read content from a file called data.txt and write the same content into another file called copy.txt.

'''with open("data.txt", "r")as f:
    data = f.read()
    with open("check.txt", "w")as f:
        new_data = f.write(data)

with open("check.txt", "r")as f:
    qwerty = f.read()
    print(qwerty)'''

# Question 36: Count Lines in a File
# Write a program that opens a file named story.txt and counts how many lines are in it.  
# Then print:  
# Total lines in file: X

'''with open("story.txt", "w")as f:
    data = f.write("This is a story file.\nThis is ques. no. 36.")

count = 0
with open("story.txt", "r") as f:
    for line in f:
        count += 1

print("Total lin in file :",count)'''

# Question 37: Write Even Numbers to a File
# Task:Write a Python program that:
# 1. Creates a file named *even.txt*  
# 2. Writes all even numbers from 1 to 100 into this file  
# 3. Each number should be on a new line

'''with open ("even.txt", "w")as f:
    for num in range(1,101):
        if num % 2 == 0:
            f.write(str(num) + "\n")

with open ("even.txt", "r")as f:
    data = f.read()
    print(data)'''

# Question 38: Append User Input to a File
# Task: Write a Python program that:
# 1. Asks the user to enter a note (any text).  
# 2. Appends this text to a file named *notes.txt*.  
# 3. After appending, reads and prints the full content of notes.txt.

'''n = input("Enter the text :")
with open("notes.txt", "a") as f:
    data = f.write(n + "\n")
    
with open("notes.txt", "r") as g:
    read = g.read()
    print(read)'''

# Ques 39: Display Fibonacci series up to nth term, given by user 

'''n = int(input(" Enter the starting number of Fibonacci Series: "))

count= 0
a,b = 0,1

while count < n:
    print(a, end =' ')
    a,b =b, a+b
    count += 1'''

# Challenge 40: Vowel Counter & Save
# Task:
# 1. Ask the user to input a sentence.  
# 2. Count how many vowels are in it (both uppercase & lowercase).  
# 3. Save the count in a file called vowels.txt with a message like:  
#    "The sentence has 5 vowels."

'''n = (input("Enter the sentence: "))
list = "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"
count = 0

for char in n:
    if char in list:
        count += 1

with open("vowels.txt", "a") as f:
    data = f.write("The number of vowels are" + str(count)+ "." )


with open("vowels.txt", "r") as f:
    read = f.read()
    print(read)'''

# Question 41: Recursive Digit Sum
# Task:
# 1. Ask the user to enter a number (e.g. 9372).  
# 2. Write a recursive function that returns the sum of its digits.  
# 3. Print the result.

'''def sum_count(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_count(n//10)
    
print(sum_count(5632))'''

# ===== OOPS LAW IN PYTHON =====

# Question 42: Student Info
# Task: Create a class called Student that stores the following details:
# - Name
# - Class (e.g., "10th")
# - Roll number

# Create a method display() to print all student details.
# Then:  
# - Create an object with your own data  
# - Call the display() method

'''class Student:
    def __init__(self,name , Class, roll_no):
        self.name = name 
        self.Class = Class
        self.roll_no = roll_no
    
    def display(self):
        print(f"{self.name} is in class {self.Class} and having roll no. {self.roll_no}.")

a = Student("Prem", "10th", "36")
a.display()'''

# Question 43: Car Info
# Task:
# 1. Create a class Car with the following instance variables:
#    - brand
#    - model
#    - year
# 2. Create a method show_info() that prints the car details in this format:  
#    "Brand: Toyota, Model: Fortuner, Year: 2022"
# 3. Create 2 objects of the class with different data and call show_info() for both.

'''class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = int(year)

    def show_details(self):
        print(f"Brand : {self.brand}, Model : {self.model}, Year : {self.year}")
a = Car("Toyota","Fortuner",2026)
a.show_details()
b = Car("Mercedes", "AZ-108", 1956)
b.show_details()'''

# Question 44: Animal Sounds
# 1. Create a class Animal with an instance variable name.  
# 2. Add a method make_sound() that prints a generic message like:  
#    "Animal makes a sound."  
# 3. Create two subclasses: Dog and Cat.  
# 4. Override make_sound() in each subclass to print:  
#    - Dog: "Dog barks."  
#    - Cat: "Cat meows."  
# 5. Create objects of both subclasses and call make_sound().

'''class Animal:
    def make_sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def make_sound(self):
        print("Dogs Barks.")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows.")

n = input("Enter the animal name (Dog or Cat): ")

if n == "Cat":
    a = Cat()
elif(n == "Dog"):
    a = Dog()
else:
    a = Animal()

a.make_sound()'''

# Question 45: Employee Salary Info
# 1. Create a class Employee with attributes: name, id, and salary.
# 2. Write a method display_info() to print the details.
# 3. Create a method bonus() that adds a fixed bonus (say ₹2000) to salary and prints the updated salary.
# 4. Create two objects and call both methods for each.

'''class Employee:
    def display_info(self, name, id, salary):
        self.name = name
        self.id =id
        self.salary = salary

    def show(self):
        print(f"Name  = {self.name}\nEmployee Id = {self.id}, Salary : ₹{self.salary}")

    def bonus(self):
        self.salary += 2000

a = Employee()
a.display_info("Parveen", 6984563, 25000)
a.bonus()
a.show()

b = Employee()
b.display_info("Sukhi", 1616410, 18000)
b.bonus()
b.show()'''

# Question 46 : Product Inventory

# 1. Create a class Product with attributes: name, price, and quantity.  
# 2. Use the _init_ constructor to initialize values.  
# 3. Create a method total_cost() that calculates and prints the total cost (price × quantity).  
# 4. Create 2 product objects and display their total cost.

'''class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_cost(self):
        print(f"Product Name : {self.name}\nQuantity : {self.quantity}, Per Piece Price : {self.price}\nTotal Price Shown below")
        print(int(self.price) * int(self.quantity))
    

a= Product("Shirt", 500, 3)
a.total_cost()

b= Product("Jeans", 900, 5)
b.total_cost()'''

# Question 47 : Write a decorator that prints “Function is being called” before any function runs.
    
'''def my_decorator(fu):
    def crapper():
        print("Function is being called")
        fu()
        print("")
    return crapper

@my_decorator
def call():
    print("=====Call function=====")

call()'''

# Question 48 : Write a decorator that keeps track of how many times a function has been called,
# and prints the count each time.

'''def decorator(func):
    count = 0
    def sector():
        nonlocal count
        count += 1
        func()
        print("Function has been called ",count, " time .")
    return sector

@decorator
def function():
    print("Hello")

function()
function()
function()
function()
function()
function()'''

# Question 49 : Rewrite your decorator so it *doesn’t use nonlocal*, and instead tracks how many times 
# a function is called using a function attribute.

'''def decorator(func):
    def wrapper():
        wrapper.count += 1
        func()
        print("Function has been called", wrapper.count, "times.")
    wrapper.count = 0
    return wrapper

@decorator
def hello():
    print("Hello World !!!")

hello()
hello()
hello()
hello()
hello()
hello()'''

#Question 50 : Write a code for playing rock, paper, scissorss.

'''import random
def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissorss): ")
    options = ["rock","paper", "scissors"]
    computer_choice = random.choice(options)

    choices = {"Player" : player_choice, "Computer" : computer_choice}
    return choices

choices = get_choices()
print(choices)'''


#Question 51:  Write a decorator that measures and prints the execution time of a function.
#  (use time module that is [import time])

'''start = time.time()
end = time.time()
print(end)
print("Execution time :", end - start,"seconds")'''

# Question 52 :Create a class Person with attributes name and age. Write a method to display the details.

'''class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def output(self):
        print(f"The name of the person is {self.name} and his age is {self.age}.")

a = Person("Raghuveer", 65)
a.output()'''

# Question 53: Create a class Circle with a radius. Add methods to calculate and return the area and circumference.*

'''class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def output(self):
        circumference = 2*3.14*self.radius
        area = 3.14*self.radius*self.radius
        print(f"The circumference of circle is {circumference}.\nThe area of circle is {area}.")

a = Circle(6)
a.output()'''

# Question 54 . Create a class BankAccount with attributes account_holder and balance. Add methods to deposit and withdraw money.

'''class BankAccount():
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} is deposited.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance !!")
        else:
            self.balance -= amount
            print(f"Rs.{amount} is withdrawl.")

    def check_balance(self):
        print(f"Total amount in your account is {self.balance}.")

a = BankAccount("Abhiraj")
a.deposit(30000)
a.withdraw(5000)
a.check_balance()'''

# Question 55. Create a class Rectangle with length and width. Write a method to check if it's a square or not.

'''class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def check(self):
        if self.length == self.width:
            print("Yes, it's square !!")
        else:
            print("It's not a square !!")
            
r1 = Rectangle(5, 5)
r1.check()

r2 = Rectangle(5, 7)
r2.check()'''

# Question 56 : Create a class *Student* with the following:
# - Attributes: name, roll_no, and marks (out of 100)
# - A method *grade()* that:
#   - Prints "A" if marks ≥ 90
#   - "B" if marks ≥ 75
#   - "C" if marks ≥ 60
#   - "Fail" otherwise
# - Add a method *display_info()* to show student details.

'''class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name 
        self.roll_no = roll_no
        self.marks = marks
        
    def display_info(self):
        print(f"Name : {self.name} \nRoll no.-{self.roll_no}\nMarks (in %): {self.marks}%")

    def grade(self):
        if self.marks >= 90:
            print("A - Grade")
        elif self.marks >= 75:
            print("B - Grade")
        elif self.marks >= 60:
            print("C - Grade")
        else:
            print("Candidate FAIL !!")

a = Student("Abhiraj", 28, 75.6)
a.display_info()
a.grade()'''

# ===== OOP QUESTION BASED ON THEIR IMPORTANT TOPICS =====

# Topic: Class & Object 
# Question 57 : Create a class Laptop with attributes brand, model, and price. Create two objects and display their details.

'''class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


obj1 = Laptop("ASUS", "Gc 19", "Rs.57998")
print(obj1.brand)
print(obj1.model)
print(obj1.price)

obj2 = Laptop("HP", "HB 28", "Rs.64999")
print(obj1.brand)
print(obj1.model)
print(obj1.price)'''

# Topic: Constructor (_init_)  
# Qusetion 58: Create a class Book with attributes title, author, and price. Use a constructor to initialize values and a method to display them.

'''class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def output(self):
        print("Title  : ", self.title)
        print("Author : ", self.author)
        print("Price  : ", self.price)

obj1 = Book("Mathematics", "R.D Sharma", "Rs.649")
obj1.output()'''

# Topic: Encapsulation  
# Qusetion 58: Create a class Account with private balance. Provide methods to deposit, withdraw and show balance safely.
# Create two accounts and perform some deposits/withdrawals on both.  

'''class Account:
    def __init__(self,name ):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Rs.{amount} has been credited.")

    def withdrawl(self, amount):
        if amount > self.balance:
            print("=====INSUFFICIENT BALANCE=====")
        else:
            self.balance -= amount
            print(f"Rs.{amount} has been debited.")

    def check_balance(self):
        print(f"The total amount in your account is Rs.{self.balance}.")

obj1 = Account("Sassori")
obj1.deposit(75000)
obj1.withdrawl(5000)
obj1.check_balance()

obj2 = Account("Hitachi Uchiha")
obj2.deposit(75000)
obj2.withdrawl(5000)
obj2.check_balance()'''

# Topic: Inheritance
# Qusetion 59: Create a base class Vehicle with method start(). Create two subclasses Car and Bike which inherit and override the method.

'''class Vehicle:
    def start(self):
        print("Engine Started !!")

class Car(Vehicle):
    def start(self):
        print("Car Engine Started !!")

class Bike(Vehicle):
    def start(self):
        print("Bike Engine Started !!")

a = Car()
a.start()

b = Bike()
b.start()'''

# Topic: Polymorphism (Method Overriding)  
# Qusetion 60: Create a base class Shape with method area(). Inherit it in Circle and Square classes and override the method accordingly.

'''class Shape:
    def area(self,n):
        return n
    
class Circle(Shape):
    def area(self,r):
        print(3.14 * int(r) * int(r) )

class Rectangle(Shape):
    def area(self,length, width):
        print(int(length)*int(width) )

class Square(Shape):
    def area(self,side):
        print(int(side)* int(side))

a = Rectangle()
a.area(6,3)

b = Square()
b.area(6)

c = Circle()
c.area(7)'''
    
# Topic: Class Method & Static Method  
# Qusetion 61: Create a class Student. Use a class method to keep track of number of students. Also use a static method to display school name.
    
'''def wrapper():
    def decorator(fu):
        count = 0
        fu()
        count += 1
    return decorator

@wrapper
class Student:
    @staticmethod
    def school_name():
        print("School Name : NEW BAL VAISHALI PRIVATE SCHOOL")

a = Student()
a.school_name()'''
        

