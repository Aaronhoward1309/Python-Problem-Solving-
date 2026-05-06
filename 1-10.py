
def even_or_odd(num):
    if num %2==0:
        return "even"
    else:
        return "odd"
total=even_or_odd(10)
print(total)

        
    

































hours=int(input("please enter hours parked "))
day=str(input("please enter weekday or Weekend "))
price=0
if hours <=0:
    print("Invalid input")
else:
    if hours <=2:
        price=price+(50*hours)
        
    elif hours >2:
         price=price+(50*2) + ((hours-2)*30)
    if hours>5:
        price=price-50

    if day== "weekend" or day =="Weekend":
              price=price+100
    if price>300:
        print("Long parking ")
    else:
        print("short parking ")
        
    
































age= int(input("please enter the age of the person "))
day=str(input("please enter day of booking weekday or weekend "))
price=0
if age <=0:
    print("Invalid input")
else:
    if age <12:
        price=price+200
    
    elif age >=12 and age <=59:
        price=price+500
    elif age>60:
        price=price+300
   
    if day == "weekend" or day =="Weekend":
        price=price+100
    if age<12 and day=="weekday" or day =="Weekday":
        price=price-50
    if price >550:
        print("Expensive ticket")
    elif price<550:
        print("Affordable ticket")


   

    
    






