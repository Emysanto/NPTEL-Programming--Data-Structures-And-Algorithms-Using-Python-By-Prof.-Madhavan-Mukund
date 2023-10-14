A positive integer m is a prime product if it can be written as p×q, where p and q are both primes. .

Write a Python function primeproduct(m) that takes an integer m as input and returns True if m is a prime product and False otherwise. (If m is not positive, your function should return False.)

Here are some examples of how your function should work.

>>> primeproduct(6)
True

>>> primeproduct(188)
False

>>> primeproduct(202)
True
*********************************CODE**********************************
def checkprime(n):
    p=0
    for i in range (1,n+1):
        if n%i==0:
           p=p+1
    if p<=2 :
       return(True)
    else:
       return(False)

def primeproduct(m):
    if m<0:
        return(False)
    factors = []
    for i in range(1,m+1):
        if m%i ==0:
            factors.append(i)
    for i in factors:
      quotient = m//i
      if checkprime(quotient)==True and checkprime(i)==True:
         return(True) 
    return(False) 