print("Function")
print("Task 1:Factorial")
num=int(input('enter a no:'))
def factorial(num):
    if num < 0:
        print("Factorial is not defined for negative numbers")
    elif num == 0 or num == 1:
        print("Factorial of 0 or 1 is 1")
    else:
        result = 1
        for i in range(1, num + 1):
            result=result*i
        print("Factorial of", num, "is:", result)
factorial(num)
print()
print("Task 2:PrimeNumber")
num = int(input("Enter a number:"))
def primeNumber(num):
    factor=0
    if num==0 or num==1:
        print('Not a Prime')
    else:
        for i in range(2,num):
            if(num%i==0):
                factor=factor+1
        if factor>0:
            print('Not a Prime')
        else:
            print('It is a Prime Number')
primeNumber(num)
print()
print("Task 3:GCD")
def gcd(a, b):
    while b:
         a, b = b, a % b
    print("GCD is", a)
gcd(2,4)
print()
print("Task 4:Reverse a String")
def reverseString(a):
   string = a[::-1]
   print(string)
reverseString('Thiyagu')
print()
print("Task 5:pallindrome")        
def pallindrome(string):
    newstring=string[::-1]
    if(string==newstring):
        print("Given String is Pallindrome")
    else:
        print("Give string is not a pallindrome")
pallindrome('raj')
print()
print("Task 6:Sum of elements in list")                 
List=[11,22,33,44,55]
a,b,c,d,e=List
def sumoflist(List):
    print(a+b+c+d+e)
sumoflist(List)
print()
print("Task 7:count element in list")
def countOccurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    print(f"The element {element} occurs {count} times in the list.")
mylist = [1, 2, 3, 4, 2, 2, 3, 2]
elementtocount = 2
countOccurrences(mylist, elementtocount)
print()
print("Task 8:list ascending order")
def listascending(List):
    List.sort()
    print(List)
mylist=[2,5,4,1,7,6,9]
listascending(mylist)
print()
print("Task 9:Fibonocii series")
def generatefibonacci(n):
    fibonaccisequence = [0, 1] 
    while len(fibonaccisequence) < n:
        nextterm = fibonaccisequence[-1] + fibonaccisequence[-2]  
        fibonaccisequence.append(nextterm)  
    print("Fibonacci sequence up to", n, "terms:", fibonaccisequence)
numterms = 10
generatefibonacci(numterms)



        
    
     

    
            
