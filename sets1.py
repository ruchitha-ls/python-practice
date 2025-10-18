'''Create two empty sets. Take m and n as the input from the user
as the number of elements to be added to both the sets respectively.
Add m integers to set1 and add n integers to set2. Find the 
Cartesian product of two sets and display it.
'''

s1= set()
s2= set()
m=int(input("Enter number of elements in set 1: "))
n=int(input("Enter number of elements in set 2: "))

print("\nEnter elements for the first set")
for i in range(m):
    element = int(input(f"Element {i + 1}: "))
    s1.add(element)

print("\nEnter elements for the fsecond set")
for i in range(n):
    element = int(input(f"Element {i + 1}: "))
    s2.add(element)

cartesian_product = {(x, y) for x in s1 for y in s2}
print(f"Cartesian Product: {cartesian_product}")