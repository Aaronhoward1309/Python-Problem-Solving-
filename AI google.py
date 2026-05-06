fruits = ["apple", "banana", "cherry"]
fruits[1]="blueberry"
fruits.append("orange")

pet = {"type": "dog", "name": "Rosco", "age": 5}
pet["age"]+=1
print(pet["name"])

for i in range(1,11,1):
    if i %2==0:
        print(f" this number is even {i} ")

def calculate_area(length,width):
    area=length*width
    return area
area=(calculate_area(10,4))
