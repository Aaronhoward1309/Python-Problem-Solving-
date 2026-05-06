numbers=[2,8,12,16,22,30]
greater_than10=[]
for i in numbers:
    if i>10:
        greater_than10.append(i)
print(greater_than10)

def language(name):
    
    favourite_programming=input("what is your favorite programming language? ")
    print(f"hello {name},its it's cool that you enjoy coding in { favourite_programming}!")
language("aaron")
