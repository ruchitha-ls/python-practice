'''Create a list of three rows as sh
# 0th row should have numbers from 1 to n.
# 1st row should have squares of numbers from 1 to n.
# 2nd row should have cubes of numbers from 1 to n'''

list1 = []
list2 = []
list3 = []
nest_list = []
n = int(input("Enter the number of elements in each list: "))
print("Enter the integers:")
for i in range(n):
    num = int(input())
    list1.append(num)
    list2.append(num*num)
    list3.append(num * num * num)
nest_list.extend([list1,list2,list3])
print(nest_list)