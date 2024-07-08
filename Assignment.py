# write a program to reverse a string 
str='Apple'
print(str[::-1])
#write a program to check if a string is a palindrome
def ispalindrome(s):
    return s==s[::-1]
s=input("Enter a string to check string is palindrome or not  ")
ans=ispalindrome(s)
if ans:
    print("Yes")
else:
    print("No")

#write a string to checkn if a string  contain only digit 
dig='123'
print(dig.isdigit())
#write a program to find the length of the last word in the sentance
def length(sent):
    words=sent.split()
    last_word=words[-1]
    return len(last_word)
sent=input("Enter a string  ")
print(length(sent))
#write a program to replace all occurrence of a substring with another substring
sentance='''i love nature'''
print(sentance.replace('nature','pakistan'))
#write a program to remove all leading and trailing whitespace from a string
strr="i love pakistan"
def remove(strr):
    return strr.replace(" ","")
print(remove(strr))
#use string formating mathod for perform and display the fllowing operation with two input number
num1=int(input('Enter first number '))
num2=int(input("Enter second number "))
sum=num1+num2
sub=num1-num2
multi=num1*num2
formated='Sum of two number: {}\n Subtraction of two number: {}\n Multiplication of two number: {}'.format(sum,sub,multi)
print(formated)