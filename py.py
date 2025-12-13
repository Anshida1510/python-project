#adding and multiplying two numbers
a=int(input('Enter first number'))
b=int(input('Enter second number'))
sum=a+b
product=a*b
print('Sum:',sum)
print('Product:',product)
#end of the code

#to check  the given number is even or odd
num=int(input('Enter a number to check even or odd'))
if num%2==0:
    print(num,'is even')
else:
    print(num,'is odd')
#end of the code


#to find the largest of three numbers
x=int(input('Enter first number'))
y=int(input('Enter second number'))
if x>y:
    print(x,'is larger')    
else:
    print(y,'is larger')
#end of the code

#to print multiplication table of a number
n=int(input('Enter a number to print its multiplication table'))
for i in range(1,11):
    print(n,'x',i,'=',n*i)
#end of the code

#to find the factorial of a number
num=int(input('Enter a number to find its factorial'))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print('Factorial of',num,'is',factorial)
#end of the code

#to check if a number is prime or not
n=int(input('Enter a number to check if it is prime or not'))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print(n,'is not a prime number')
            break
    else:
        print(n,'is a prime number')        
else:
    print(n,'is not a prime number')
#end of the code 


#to print Fibonacci series up to n terms
terms=int(input('Enter number of terms for Fibonacci series'))
a, b = 0, 1
count = 0
