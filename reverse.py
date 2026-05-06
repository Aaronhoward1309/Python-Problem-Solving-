num=[1,2,3,4,5,6]
num1=[]
for i in num:
    num1.insert(0,i)
print(num1)

num=[2,4,6,8,10,12]
largest=num[0]
second_largest=num[0]
for i in num:
    if i > largest:
        second_largest=largest
        largest=i
    elif i> second_largest:
        second_largest=i
        
print(second_largest)
    
