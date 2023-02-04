#Python program to check given number is prime or not..?

n = int(input("Enter the number:"))
if n > 1:
    for i in range(2,int(n/2)+1):
        if(n % i)==0:
            print(n,"is Non prime")
            break
    else:
         print(n,"is prime" )
