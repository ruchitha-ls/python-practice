d={'roshan': {'math':100,'phy':90,'chem':90}, 'dhruv': {'math':90,'phy':89,'chem':95}, 'alisha': {'math':95,'phy':95,'chem':93}, 'naveen':{'math':98,'phy':91,'chem':92} }
name = input("Enter the name of the student whose marks you want to know: ")
if name in d:
    for sub in d[name]:
        print("Student has scored",d[name][sub], "in",sub)
else:
    print("Student data not available")
  
math = []
phy = []
chem = []
avg_marks = {}
for name in d:
    math.append(d[name]['math'])
    phy.append(d[name]['phy'])
    chem.append(d[name]['chem'])
avg_marks['math'] = sum(math)/len(math)
avg_marks['phy'] = sum(phy)/len(phy)
avg_marks['chem'] = sum(chem)/len(chem)

for i in avg_marks:
    print(i,"average --->",avg_marks[i] )