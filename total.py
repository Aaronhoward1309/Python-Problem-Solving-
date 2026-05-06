scores=[25,50,35,67,77,88,90,35,90,56]
high_scores=[]
for i in scores:
    if i>50:
        high_scores.append(i)
print(high_scores)

for i in range(1,31,1):
    if i%3==0 and i%5==0:
        print("Full house")
    elif i%3==0:
        print("Triad")
    elif i%5==0:
        print("pentad")
    else:
        print(i)
fruits={
    "apples":5,
    "Bannas":12
    }
fruit=input("please enter a fruit ")
if fruit in fruits:
    fruits[fruit]+=10
else:
    fruits[fruit]=1
print(fruits)

def smart_divide(a,b):
    if b==0:
            return("divison by zero is not allowed")
            
    result=a/b
    return result
result=print(smart_divide(10,5))
