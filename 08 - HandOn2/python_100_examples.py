

# write a python program to read and print contents of a file

filepath = 'data.txt'
with open(filepath, 'r') as file:
    data = file.read()
    print(f'Data: {data}')

# write a python function to add numbers in a list

def add(list):
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]
    return sum


# write a function to check if a number is positive or not

def check(num):
    if num > 0:
        return True
    return False

# write a python function to that performs as ReLU

def ReLU(num):
    if num > 0:
        return num
    return 0

# write a boolean python function to check if a given string matches a given pattern

import re

def match(pattern, string):
    if re.match(pattern, string):
        return True
    return False

# write a python program to swap two numbers and print them

num1 = 2
num2 = 4

num1, num2 = num2, num1

print(num1, num2)

# write a python function to get the maximum element in a list

def max(list):
    return max(list)

# write a python program list comprehension to make a list of size n of random integers in ranges a and b

import random

n = 10
a = 1
b = 100

rand = [random.randint(a, b) for i in range(n)]
print(f'list : {rand}')

# write a python program to tokenise a string into words and print them

string = 'the sun is shining'

words = string.split()
print(words)

# write a python program to print the command line arguements given to a file

import sys
args = sys.argv 
print(args)

# write a python program to print a string in lowercase

string = 'SFG';
print(string.lower())

# write a python function to return the absolute difference between two numbers

def abs_diff(num1, num2):
    return abs(num1 - num2)

# write a program to terminate the program execution

import sys
sys.exit()

# write a python program to print the datatype of a variable
x = 2
print(type(x))

# write a python program to sort a list in descending order and print it

list = [3, 1, 5, 6]
result = sorted(list, reverse = True)
print(result)

# write a python function to check if a string contains a vowel or not

def check_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        if vowel in string:
            return True
    return False

# write a python program to filter a list and return words with alphabets only and print it
 

list = ['sadgas1', 'sasg.as3$', 'hsd', '^atg', 'gaf']
result = [item for item in list if item.isalpha()]
print(result)

# write a python program to trim whitespace characters from a string and print it

string = ' asdga \t\r'
print(string.strip())

# write a python program to typecast an integer to string and print it

x = 2
y = str(x)
print(y)

# write a python program to round up a number and print it

import math
x = 2.3
y = math.ceil(x)
print(y)

# write a function to accept a simple iterable and print the elements 

def print_iter(iter):
    for item in iter:
        print(item)

# write a function to reverse a string 

def reverse_string(string):
    return string[::-1]

# write a function to check if a string is a palindrome or not

def reverse_string(string):
    return string[::-1]

def ispalin(string):
    if string == reverse_string(string):
        return True
    return False

# write a python function to return the largest value in a dictionary

def dic_largest(dic):
    return max(dic.values())

# write a python print to return the first n fibonacci numbers

def fibonacci(n):
    a, b = 0, 1
    print(a)
    print(b)
    for i in range(n - 2):
        print(a + b)
        a, b = b, a + b

# write a python function to return the number of whitespace separated tokens

def tokenise(string):
    return len(string.split())

# write a python function to return the cube of a number

def cube(num)
    return num * num * num

# write a python function to return the area of a circle with given radius
import math
def area_circle(radius):
    return math.pi * radius * radius

# write a python function to calculate age given date of birth

from datetime import date 

def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year - 
         ((today.month, today.day) < 
         (birthDate.month, birthDate.day)) 
  
    return age

# write a python function to calculate simple interest given principal , rate and time

def simpleIntereset(principal, rate, time):
    return principal * rate * time / 100

# write a function to calculate the frequency of a number in a list

def frequency(list, num):
    count = 0
    for item in list:
        if item == num:
            count = count + 1
    return count

# write a program to print ascii code of a character

x = '5'
print(ord(x))

# write a function to calculate factorial of number

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

# write a function to print if a number is even or odd

def oddeven(num):
    if num % 2 == 0:
        print('even')
    else:
        print('odd')

# write a python program to accept username and print hello along with the username

name = input()
print('Hello ' + name)

# write a python program to print current datetime
from datetime import datetime

now = datetime.now()
print(now)

# write a python function to convert from Celcius to fahrenhiet

def cel_to_fah(celcius):
    return 9 * celcius / 5 + 32

# write a python program to delete an element from a list

list = ['a', 'bc', 'd', 'e']
element = 'bc'
list.remove(element)

# Write a program to print the union of two sets

Set1 = {"1","2","3"}
Set2 = {"a","b","c"}
Set = Set1.union(Set2)

print(Set)

#write a program to remove common element between two sets

s1 = {"apple", "banana", "cherry"}
s2 = {"google", "microsoft", "apple"}

s1.difference_update(s2)
print(s1)

# write a program to find a given character in a string and print its position
a= "Hello World"
x= a.find("r")
print(x)

# write a program to print logrithmic values of any number 

import math
x = 100
base = 5
print(math.log(x,base))

# write a program to join two lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# write a function to check a valid email id

import re 

def check(email):    
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)):  
        print("Valid Email")            
    else:  
        print("Invalid Email")

# write a program to print difference in between today and given date

import datetime
dd = int(input("date: "))
mm = int(input("month: "))
yy = int(input("year: "))
a = datetime.date(yy,mm,dd)
x = date.today()
print(x-a)

# write a program to check if year is a leap year or not

year = int(input("Year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

# write a function to replace vowels with a specific character K

def replacewith_K(test_str, K): 

    vowels = 'AEIOUaeiou'
    for ele in vowels: 
        test_str = test_str.replace(ele, K) 
  
    return test_str

# write a python function to return mean of a list of numbers

def mean(list):
    sum = 0
    for num in list:
        sum += num
    return sum / len(list)

# write a python class named complex with constructor accepting real and imaginary parts
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

# write a program to convert key-values list to flat dictionary and print it

from itertools import product 
test_dict = {'month' : [1, 2, 3], 
             'name' : ['Jan', 'Feb', 'March']} 
 
print("The original dictionary is : " + str(test_dict)) 
  
 

res = dict(zip(test_dict['month'], test_dict['name'])) 

print("Flattened dictionary : " + str(res))

# write a program to remove duplicate elements in a list and print the list

test_list = [1, 3, 5, 6, 3, 5, 6, 1] 
print ("The original list is : " +  str(test_list)) 
  
res = [] 
for i in test_list: 
    if i not in res: 
        res.append(i) 
  
print ("The list after removing duplicates : " + str(res))

# write a program to print sum of all even numbers in a list

ls = [1,2,3,4,5,6,7,8,10,22]
sum = 0
for i in ls:
    if i % 2 == 0:
        sum += i
print(sum)

# write a program to write a string in a file

filename = 'file1.txt'
string = "programming in \n python"
f1 = open(filename,'w')
f1.write(string)
f1.close()

# write a function to check weather a number is prime or not

def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# write a program to print binary of a decimal number n

binaryNum = [0] * n; 
i = 0; 
while (n > 0):  
    binaryNum[i] = n % 2; 
    n = int(n / 2); 
    i += 1; 

for j in range(i - 1, -1, -1): 
    print(binaryNum[j], end = "")

# write a function to check if a number is perfect square or not
import math
def checksquare(num):
    x = int(math.sqrt(num))
    if x * x == num:
        return True
    return False

# write a program to print the sine value of a number
import math
num = 3
print(math.sin(num))

# write a function to calculate the hypotenuse of a triangle give base and height

import math
def calc_hypotenuse(base, height):
    return math.sqrt(base * base + height * height)

# write a function to calculate the sum of digits of a number

def sum_of_digits(num):
    sum = 0
    while(num > 0):
        sum += num % 10
        num = num // 10
    return sum

# write a python function to find URLs in a string

import re 
  
def Find(string): 
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)       
    return [x[0] for x in url]

# write a python function to calculate the dot product of two lists
def dot(l1, l2):
    return sum(x*y for x,y in zip(l1, l2))

# write a function to accept input as feet and inches into centimeters
def height_into_cms(feet, inches):
    ininches = feet * 12 + inches
    return ininches * 2.54

# write a python function to convert temperature from celcius to kelvin
def cel_to_kel(celcius):
    return celcius + 273

# write a python program to find difference between elements of two lists and print it

l1 = [1, 2, 3, 4]
l2 = [5, 8, 7, 0]

res = []
for i in range(len(l1)):
    res.append(l1[i] - l2[i])

print(res)

# write a function to calculate BMI given height in meters and weights in kgs

def bmi(height, weight):
    return weight / (height * height)

# write a function to calculate area of a triangle given height and base

def area_triangle(base, height):
    return 0.5 * base * height

# write a program to print the bitwise OR of two numbers

num1 = 5
num2 = 10
print(num1 | num2)

# write a function to convert weight from kgs to pounds

def kgs_to_pounds(weight_kg):
    return weight_kg * 2.2

# write a function to convert miles to kilometers

def miles_to_kms(dist):
    return dist * 1.609

# write a function to calculate speed given distance covered and time taken

def calspeed(dist, time):
    return dist / time
