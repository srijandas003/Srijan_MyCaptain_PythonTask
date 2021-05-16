#Fibonacci_Series Program by Srijan
print("Fibonacci Series")
n = int(input("Enter the limit of the Series : "))
a , b = 0,1
count = 0
if n <= 0:
    print("Please Enter a positive integer ")
elif n == 1:
    print("Fibonacci Series upto ",n)
    print(a)
else:
    print("Fibonacci Series : ")
    while count < n:
        print(a)
        c = a+b
        a = b
        b = c
        count += 1
