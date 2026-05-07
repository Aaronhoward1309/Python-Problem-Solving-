
#Q1) A user tries to withdraw money from an ATM.
#Rules:
#Minimum withdrawal = 500
#Maximum withdrawal = 50,000
#Must be multiple of 500
#Task:
#Write a function atm_withdraw(amount) that returns:
#"Transaction successful"
#or "Invalid amount"

Maximum_withdrawal = 50000
Minimum_withdrawal = 500
def atm_withdraw(amount):
    if amount >= Minimum_withdrawal and amount <= Maximum_withdrawal and amount %500==0:
        return "Transaction successful"
    else:
        return "Invalid amount"
amount1=atm_withdraw(5000)
print(amount1)

    




#Q2) Scenario:
#Billing system.
#Rules:
#Units ≤ 100 → 5 per unit
#Units ≤ 300 → 8 per unit
#Above → 10 per unit

def bill_amount(units):
    if units <=100:
        units=units*5
        return units
    elif units <=300:
        units=((units-100)*5)+ ((units-100)*8)
        return units
    else:
        units=((units-100)*5)+ ((units-200)*8) + ((units-300)*10)
        return units
total=bill_amount(300)
print(total)
    

#Q3) Scenario:
#Basic calculator using condition.
#Task:
#Function calculate(a, b, op) where op can be +, -, *, /

def caluclator(a,b,operator):
  if operator=="+":
        total=a+b
        return total
  elif operator=="-":
        total=a-b
        return total
  elif operator=="*":
        total=a*b
        return total
  elif operator =="/":
        total=a/b
        return total
  else:
      return "Invalid response"
total=caluclator(2,4,"+")
print(total)


#Q4) Scenario:
#Check if a year is leap year.
#Rules:
#Divisible by 4 AND not by 100
#OR divisible by 400
#def leap_year(year):
    #if (year %4==0 and year %100!=0) or (year %400==0):
        #return ("Leap Year ")
    #else:
        #return "No leap year ")
#total=leap_year(2006)
#print(total)
        
    
#hours=int(input("please enter hours parked "))
#day=str(input("please enter weekday or Weekend "))
#price=0
#if hours <=0:
    #print("Invalid input")
#else:
    #if hours <=2:
        #price=price+(50*hours)
        
    #elif hours >2:
        # price=price+(50*2) + ((hours-2)*30)
    #if hours>5:
        #price=price-50

    #if day== "weekend" or day =="Weekend":
             # price=price+100
    #if price>300:
        #print("Long parking ")
    #else:
   #     print("short parking ")
        
    

#age= int(input("please enter the age of the person "))
#day=str(input("please enter day of booking weekday or weekend "))
#price=0
#if age <=0:
    #print("Invalid input")
#else:
    #if age <12:
       # price=price+200
    
   # elif age >=12 and age <=59:
        #price=price+500
    #elif age>60:
       # price=price+300
   
    #if day == "weekend" or day =="Weekend":
       # price=price+100
    #if age<12 and day=="weekday" or day =="Weekday":
        #price=price-50
    #if price >550:
        #print("Expensive ticket")
    #elif price<550:
       # print("Affordable ticket")


   

    
    






