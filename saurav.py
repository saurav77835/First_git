#Write a Python program to declare two variables, a and b, where a is a float number 3.5, and b is a string "Hello World". Print the type of both variables.
'''
a = float(3.5)
b = "hello world"

print(type(a))
print(type(b))
'''

#Create a string variable containing "Python" and use slicing to print only "yth" from it.
'''
a = "python"
print(a[1:4])
'''

#Given two integer variables x = 10 and y = 4, write a Python script to perform and print the results of addition, subtraction, multiplication, division, and modulus operations.
'''
x= 10
y= 4

print("the result is add",x+y)
print("the result is sub",x-y)
print("the result is div",x/y)
print("the result is mul",x*y)
print("the result is mod",x%y)
'''

#Create a list named fruits with elements "apple", "banana", and "cherry". Add "orange" at the end and "grape" at the second position. Then remove "banana" from the list.
'''
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
fruits.insert(1, 'grape')
print(fruits)
'''

#Write a Python program to create a tuple with different data types and print each item along with its type.
'''
tup = ( 1,3,'three',4,5.5,6,'seven')
for i in tup:
	print(i, type(i))
'''

#Create a Python set called my_set with numbers from 1 to 5. Then add 6 to the set and remove 2. Check if 4 is in the set.
'''
a_set = {1,2,3,4,5}	
a_set.add(6)
a_set.remove(2)
print(a_set)
if 4 in a_set:
	print("yes")
	
'''

#Write a Python script to create a dictionary where the keys are numbers between 1 and 5 (both included) and the values are their squares. Example: {1: 1, 2: 4, 3: 9, ...}

'''
dict = { }
for i in range(1,6):
	dict[i] = i*i
	
print(dict)	

dict.update({1:5})
print(dict)
'''

#Write a Python program that takes an integer from the user and prints "Even" if the number is even and "Odd" if the number is odd.
'''
a = int(input("enter the integer number"))
print("your number is :",a)
if a%2 == 0:
	print("the number is even")
else:
	print("the number is odd")
'''

#Write a Python script to display all prime numbers within the range of 1 to 50 using a while loop.
'''
num = 1
while num <= 50:
    isPrime = True
    
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            isPrime = False
            break
            
    if isPrime:
        print(num)
        
    num += 1
'''

#    10. Use a for loop to iterate over the fruits list created in question 4 and print each item.

'''
fruits = ['apple', 'banana', 'cherry']
for i in fruits:
	print(i)

'''

#Define a Python function named sum_numbers that takes two parameters and returns their sum. Test this function with different pairs of numbers.

'''
def sum_numbers(a,b):
	sum = a+b
	return sum 
	
x = input("enter first number ")
y = input("enter second number")

print(sum_numbers(x,y))

'''	

#Write a recursive function named factorial to compute the factorial of a given number. Test this function with different numbers.
'''
def factorial(a):
	if a == 0 or a == 1:
		return 1
	else:
		return a * factorial(a - 1)

x =  int(input("enter number"))
ans = factorial(x)
print(ans)
'''

#Write a Python program with a try-except block. In the try block, divide two numbers provided by the user. Handle the ZeroDivisionError in the except block by printing a custom error message.

'''
a = int(input("num1"))
b = int(input("num2"))

try:
	c = a/b
	print(c)
except:
	print("ZeroDivisionError")	

'''

###  FILE HANDLING   ###

#    14. Write a Python program to create a file named example.txt, write "Hello, Python!" to it, and then read and print the contents of the file.
'''
file_1 = open("example.txt", "x")

file_1.write("Hello python!")
file_1.close()
'''
'''
file_1 = open(r"example.txt")
print(file_1.read())
'''

 #   15. Write a Python program to write a list content to a file. Write this list color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] to a file name color.txt.
'''
color =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

f = open("example.txt", 'w')

for i in color:
	
	f.write(i)	
f.close()
'''

###   Regular Expressions   ####

#    16. Write a Python program that uses regular expressions to check if a string contains the word 'Python'. Test this with the string "I am learning Python programming".
'''
import re
st = "I am learning Python programming"
x = re.search("Python", st)
if x:
	print("yes")
else:
	print("no")

'''

 #   17. Use regular expressions in Python to find all occurrences of dates in the format dd-mm-yyyy in a given string. Test it with the string "My important dates are 12-05-2022, 23-10-2021, and 01-01-2023."
'''
import re
st = "My important dates are 12-05-2022, 23-10-2021, and 01-01-2023."
x = re.findall("[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]", st)

if x:
	print(x)
else:
	print(x)
'''

 #   18. Create a Python script using regular expressions to replace all occurrences of the word "is" with "was" in a given string. Test it with the string "This island is beautiful."
'''
import re
st = "This island is beautiful"
x = re.sub(" is ", " was " ,st ,1 )
print(x)
'''	
