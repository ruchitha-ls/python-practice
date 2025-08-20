x= int(input("Enter a number: "))

print("Is the number between 1 and 100?")

if x>0 and x<101:
    print('YES')
else:
    print('NO')

#---------------------------------------------------------------------

y= str(input("Enter a sentence: "))
#The is actually no need to wrap with string in the above line

print("Does the sentence contain the letter 'a'?")

if 'a' in y:
    print("Contains a")
else:
    print("Does not contain a")