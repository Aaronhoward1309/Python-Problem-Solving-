numbers=[5,12,8,15,20]
even_num=0
for i in numbers:
    if i %2==0:
        even_num=even_num+1
print(even_num)

inventory={
    "apple":15,
    "banna":8,
    "orange":20
    }
for i in inventory:
    print(inventory.get("apple","banna","orange"))
   
    
