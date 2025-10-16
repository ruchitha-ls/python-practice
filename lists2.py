'''Given a list of heterogenous elements, create different lists 
based on the type of elements in the list.'''

l1=[2, 9.8, "Hello", "Bye", 3, 7, 8.5, 2+5j, True, False]
l_int= []
l_float= []
l_bool= []
l_string= []
l_complex= []
for item in l1:
    if type(item) == int:
        l_int.append(item)
    elif type(item) == float:
        l_float.append(item)
    elif type(item) == bool:
        l_bool.append(item)
    elif type(item) == complex:
        l_complex.append(item)
    elif type(item) == str:
        l_string.append(item)    
print(l_int)
print(l_float)
print(l_complex)
print(l_bool)
print(l_string)