




##QUESTION1-1. What are the key features of Python?
##ANSWER-Simple and easy to run
##       open source
##       High level Programing languge
##       Dynamic typed
##       Python is case sensitive languge
##       Support both Procedural & object orianted langue
##       Extensive laibrary


##Question-2. What are the Data Types in Python?
##Answer      Numerical -int flot,complex
##            Sequence-list,tuple,range
##            Text-str
##            mapping-dict
##            set-Frozen set,set
##            bool-True & False

##QUESTION 3. What are local variables and global variables in Python?
##Answer-Global variables are those which are not defined inside any function and have a global scope
# whereas local variables are those which are defined inside a function and its scope is limited to that function only


##QUESTION-4. How do you write comments in python? And Why Comments are important?
## Answer -# is use the cooment in Python
##Comments in Python is the inclusion of short descriptions along with the code to increase its readability.

##Question-5. How to comment on multiple lines in python?
##Answer-     #Triple Quotation (''') used to comment on multiple lines in python.

##Question-6. What do you mean by Python literals?
##Answer-Literals in Python is defined as the raw data assigned to variables or constants while programming.

##QUSSTION 7. What are different ways to assign value to variables?
##Answer-  There are two ways to assign the the values to variables,
# Direct Initialisation Method -
# In this method, we directly declare the variable and assign a value using the = sign.
# If the variable is declare multiple times, then the last declaration’s value will be used by the program.
# Example,
# - x = 5
# - x = 5
# - print(a)
# output = 10
# By using conditional operator -
# We can initialize value of a variable using some conditions.
# The evaluation of the result of the condition will become the value of the variable.
# Example,
# x = 10
# y = 16 if x > 8 else 0
# print("Value of z is: " + str(y))
# output = Value of z is: 16

##Question-8.What are the Escape Characters in python?
##ANSWER-In Python strings, the backslash "\" is a special character, also called the "escape"


##question-9.Which are the different ways to perform string formatting? Explain with example
##Answer-There are four different ways to perform string formatting:-
          # Formatting with % Operator.
          # Formatting with format() string method.
          # Formatting with string literals, called f-strings.
          # Formatting with String Template Class

##question-10Write a program to print every character of a string entered by the user in a new line using a loop
##ANSWER-
# a=input("Enter the string:-\n")
# for i in a:
#     print(i)


##Question-11 Write a program to find the length of the string "machine learning" with and without using len function.
# str1="machine learning"
# print(len(str1))

# string = "machine learning"
# last_letter = string[-1]
# string.index(last_letter) + 1

##12. Write a program to check if the word 'orange' is present in the "This is orange juice".
# string1="This is orange juice"
# print("orange " in "This is orange juice")

# word="This is orange juice"
# if("orange" in  word):
#     print("word is present")
# else:
#     print("word is not present")

##13. Write a program to find the number of vowels, consonants, digits, and white space characters in a string.
# str1=input("Enter tne string:-").lower()
# vovel=['a','e','i','o''u']
# Digits = ["0","1","2","3","4","5","6","7","8","9"]
# Consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
# v=0
# d=0
# c=0
# w=0
# for i in str1:
#     if(i in vovel):
#         v+=1
#     elif(i in Digits):
#         d+=1
#     elif(i in Consonants):
#         c+=1
#     elif(w==" " ):
#         w+=1
# print(v)
# print(d)
# print(c)
# print(w)

##Question 14. Write a Python program to count Uppercase, Lowercase, special character,and numeric values in a given string.
# str1=input("Enter the String:-")
# u=0
# l=0
# s=0
# n=0
# for i in str1:
#     if(i.islower()):
#         l+=1
#     elif(i.isupper()):
#         u+=1
#     elif(i.isnumeric()):
#         n+=1
#     else:
#         s+=1
# print(l)
# print(u)
# print(n)
# print(s)

##15. Write a program to make a new string with all the consonants deleted from the string "Hello, have a good day".
# str1="Hello, have a good day"
# vovel=['a','e','i','o','u']
# #print(f"string without consonants:")
# for i in str1:
#     if(i in vovel):
#         print(i,end=" ")

##16. Write a Python program to remove the nth index character from a non-empty string.
# String = input("Enter string here: ")
# n = 8
# str1 = String[0:n]
# print(str1)
# str2 = String[n+1:]
# print("\nModified string after removing ", n, "th character ")
#print(str1+str2)

##17. Write a Python program to change a given string to a new string where the first and last characters have been exchanged.
# string="Hello Python"
# new_string=string
# print(new_string[::-1])



##18. Write a Python program to count the occurrences of each word in a given sentence.

# String = input("Enter string here: ")
# List = String.split()
# words = []
# for i in List:
#     if i not in words:
#         words.append(i)
# for i in range(0, len(words)):
#     print('Count of', words[i], 'is :', List.count(words[i]))

##19. How do you count the occurrence of a given character in a string?
# Use the count() Function to Count the Number of a Characters Occuring in a String in Python. ###Example,
# string = "python python"
#print( string.count("p"))
# Output - 2

##20. Write a program to find last 10 characters of a string?
# str1="python & data science"
# print(str1[-10:])

##21. WAP to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters
# str1="PyThon"
# print(str1.upper())

##22. Write a Python program to remove a newline in Python.
# str1="Python & Data \n Science"
# print(str1)
# print(str1.replace("\n",""))

##23. Write a Python program to swap commas and dots in a string
#○ Sample string: "32.054,23"
#○ Expected Output: "32,054.23"
# Str1 = "32.054,23"
# comma = ","
# dot = "."
# print(Str1.replace(comma,dot).replace(dot,comma,1))

##24. Write a Python program to find the first repeated character in a given string
# str="data science and python"
#
# a=0
#
# for i in range(0 , len(str) ):  #traversing through the entire string
#     if a==1:
#         break
#     for j in range(i+1 , len(str)): #traversing characters after the current one
#         if str[i]==str[j]:
#             print(str[i])
#             a=1              #this character is the first repeating character
#             break
#
# if a==0:
#     print(-1)

# Q.25 Write a Python program to find the second most repeated word in a given string.
# string = input("Enter a string :-")
# str1 = string.split()
# a = 0
# for i in str1:
#     if str1.count(i) > a :
#         a = str1.count(i)
# print(i)

# ##Q.26 Python program to Count Even and Odd numbers in a string.

# str1="0123456789"
# even_no=0
# odd_no=0
# for i in str1:
#     if(int(i)%2==0):
#         even_no+=1
#         print(f"Even_no:-{i}",end="\n")
#     else:
#         odd_no+=1
#         print(f"odd_no:-{i}",end="\n")
# print(f"Total Even no count is:-{even_no}")
# print(f"Total Odd no count is:-{odd_no}")

##Q.27 How do you check if a string contains only digits?
# string = input("Enter string here: ")
# string.isdigit()

##Q.28 How do you remove a given character/word from String?
#string = "Rahul Chamute"
#string.replace("R","")

##Q,29 Write a Python program to remove the characters which have odd index values of a given string
# string = "Gaurav Gunjal"
# for i in string:
#     if string.index(i) % 2 == 0:
#         print(i)

##Q.30 Write a Python function to reverses a string if its length is a multiple of 5
# string = "DataS"
# length = len(string)
# print(length)
# if len(string) % 5 == 0:
#     b = string[::-1]
#     print(b)
# else:
#     print(string)

##Q.32 Write a Python program to reverse words in a string

# String = "Data Science and python"
# b = String.split()
# a = b[::-1]
# " ".join(a)

##Q.33 Write a Python program to swap cases of a given string
# string = input("Enter string here: ")
# string.swapcase()

##Q.34 Write a Python program to remove spaces from a given string

# String = input("Enter string here: ")
# String.replace(" ","")

##Q.36 Write a Python Program to find the area of a circle.

# r=float(input("Enter the radius of cirle"))
# a=3.14*r*r
# print(a)

##Q.37 Python Program to find Sum of squares of first n natural numbers

# n = int(input("Enter value of n: "))
# Sum = 0
# for i in range(1, n+1):
#     Sum += (i**2)
#
# print("Sum of squares = ", Sum)

##Q.38 Python Program to find cube sum of first n natural numbers
# n = int(input("Enter value of n: "))
# Sum = 0
# for i in range(1, n+1):
#     Sum += (i**3)
#
# print("Sum of squares = ", Sum)

##Q.39 Python Program to find simple interest and compound interest
# principal = float(input('Enter amount: '))
# time = float(input('Enter time: '))
# rate = float(input('Enter rate: '))
#
# simple_interest = (principal*time*rate)/100
# compound_interest = principal * ( (1+rate/100)**time - 1)
#
# print('Simple interest is: %f' % (simple_interest))
# print('Compound interest is: %f' %(compound_interest))


##Q.40 Python program to check whether a number is Prime or not
# n = int(input("Enter value of n: "))
# for i in range(2, n):
#     if n % i != 0:
#         print(f"{n} is prime")
#         break
#     else:
#         print(f"{n} is not a prime")
#






