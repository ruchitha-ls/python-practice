string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

words1 = set(string1.lower().split())
words2 = set(string2.lower().split())
common= set()
c=0

for i in words1:
    for j in words2:
        if i==j:
            common.add(i)
            c+=1

if c>0:
    print(f"The {c} common words are: {common}")
else:
    print("No common words found")