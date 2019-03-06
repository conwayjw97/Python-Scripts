from datetime import datetime

def getTimeChoice():
    print("\n1 - Days between...")
    print("2 - Weeks between...")
    print("Other - Exit")
    choice = input("Insert choice: ")
    return choice

def getPeriodChoice():
    print("\n1 - Between today and...")
    print("2 - Between ... and ...")
    choice = input("Insert choice: ")
    return choice

now = datetime.now()
print("Date today: %s/%s/%s" % (now.day, now.month, now.year) )

timeChoice = getTimeChoice()
while((timeChoice == "1") or (timeChoice == "2")):
    periodChoice = getPeriodChoice()
    
    if(periodChoice == "1"):
        day = int(input("\nOther day: "))
        month = int(input("Other month: "))
        year = int(input("Other year: "))
        then = datetime(year, month, day)
        
        if(then > now):
            delta = then - now
        else:
            delta = now - then
        
        if (timeChoice == "1"):
            print("\nTime between then and now: %d days" % delta.days)

        if (timeChoice == "2"):
            weaks = delta.days/7
            weaksDecimal = weaks % 1
            days = round(7*weaksDecimal)
            print("\nTime between then and now: %.0f weeks and %d days" % (weaks, days))

    elif(periodChoice == "2"):
        dayA = int(input("\nFirst date day: "))
        monthA = int(input("First date month: "))
        yearA = int(input("First date year: "))
        dateA = datetime(yearA, monthA, dayA)
        
        dayB = int(input("\nSecond date day: "))
        monthB = int(input("Second date month: "))
        yearB = int(input("Second date year: "))
        dateB = datetime(yearB, monthB, dayB)
        
        if(dateA > dateB):
            delta = dateA - dateB
        else:
            delta = dateB - dateA
        
        if (timeChoice == "1"):
            print("\nTime between the first and second date: %d days" % delta.days)

        if (timeChoice == "2"):
            weaks = delta.days/7
            weaksDecimal = weaks % 1
            days = round(7*weaksDecimal)
            print("\nTime between the first and second date: %.0f weeks and %d days" % (weaks, days))

    timeChoice = getTimeChoice()
       
