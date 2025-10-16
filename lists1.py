'''Program to find the absolute difference between successive 
elements of a given list and this difference must be stored in the 
new list. Display the new list'''

li = [9,4,10,25,33,3,21]
diff_li = list()   
print("Original list is:",li)
for i in range(0,len(li)-1):
        diff = li[i+1] - li[i]
        diff_li.append(abs(diff))
print("new list is:", diff_li)