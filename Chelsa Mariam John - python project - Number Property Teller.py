# NUMBER PROPERTY TELLER:
def even_odd(n):
    if n%2==0:
        print ("It is an even number")
    else:
        print ("It is an odd number")


def prime(n):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                print(n,"is a composite number, because", end=" ")
                print(i,"times",n//i,"is",n)
                break
        else:
                print(n,"is a prime number")
    else:
        print(n,"is neither prime nor composite")


def palindrome(n):
    s=str(n)
    if s==s[: :-1]:
        print("The given number is a palindrome number")
    else:
        print("The given number is not a palindrome number")
        
    
def factors(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    print("The given number has", len(l),"factors, which are", l)


def sum_natural(n):
    s=0
    for i in range (1,n+1):
        s+=i
    print("sum of all natural numbers till",n,"is",s)


def factorial(n):
    fact=1
    if n < 0:
        print("factorial does not exist for negative numbers")
    elif n == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,n + 1):
            fact = fact*i
        print("The factorial of",n,"is",fact)

def fibo(n):
    n1, n2 = 0, 1
    count = 0
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print("Fibonacci sequence upto",n,":")
        print(n1)
    else:
        print("Fibonacci sequence:")
    while count < n:
       print(n1, end=" ")
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

n=int(input('Enter any integer: '))
print('The number you have entered is:',n)
print('Some of the properties of the number',n,'are:')
even_odd(n)
prime(n)
palindrome(n)
factors(n)
sum_natural(n)
factorial(n)
fibo(n)