#Python program to calculate factorial of given number....

inp = int(input("Enter the number"))
fact = 1
if inp >= 1:
    for i in range(1,inp+1):
        fact=fact*i
print("factorial of given number is",fact)