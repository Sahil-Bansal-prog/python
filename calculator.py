print("Enter 1 for Addtion of n numbers")
print("Enter 2 for Subtraction of two numbers")
print("Enter 3 for Multiplication of two numbers")
print("Enter 4 for Division of two numbers")
print("Enter 5 for getting the remainder while dividing first number by second one")

a=int(input("Enter Your Choice:--"))
d = 0;

if a==1:
    n = int(input("Enter the numbers to be added"))
    print("Enter n numbers:--")
    for i in range(n):
        d += int(input())
elif a==2:
    b=int(input("Enter 1st Number:--"))
    c=int(input("Enter 2nd Number:--"))
    d=b-c
elif a==3:
    b=int(input("Enter 1st Number:--"))
    c=int(input("Enter 2nd Number:--"))
    d=b*c
elif a==4:
    b=int(input("Enter 1st Number:--"))
    c=int(input("Enter 2nd Number:--"))
    d=b/c
elif a==5:
    b=int(input("Enter 1st Number:--"))
    c=int(input("Enter 2nd Number:--"))
    d=b%c
else:
    print(" Wrong Choice Entered")


print("Your Answer is :-")
print(d)


print("Thanks for using this simple calculator and we will modify it for better performance")
