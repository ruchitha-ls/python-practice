x= int(input("Enter an integer: "))
#We are assuming number to be int, coz only int can have odd/even

if x==0:
    print("The number is zero")
elif x>0:
    print("The number is positive")
else:
    print("The number is negative")

if x % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

"""
The below code is extremely correct. But ChatGPT

y= x%10
if y==1 or y==3 or y==5 or y==7 or y==9:
    print("The number is odd")
else:
    print("The number is even")
"""