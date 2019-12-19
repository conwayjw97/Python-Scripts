# Use this script to generate dated lines which you can write daily plans on.

weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

def chooseMonth():
	month = 0
	while(month < 1 or month > 12):
		print()
		for i in range(len(months)):
			print(i+1, "-", months[i])
		month = int(input("Insert month (number from the list above): "))
	return month - 1

def chooseDay(month):
	day = 0
	while(day < 1 or day > 31):
		print()
		day = int(input("Insert day (number between 1 and 31): "))
		if(month in (3, 5, 8, 10) and day == 31):
			day = 0
			print("\n", months[month], "can't have more than 30 days")
		if(month == 1 and day > 29): # Doesn't count leap years, I know
			day = 0
			print("\n", "Can't have more than 29 days for Feb")
	return day

def chooseWeekday():
	weekday = 0
	while(weekday < 1 or weekday > 7):
		print()
		for i in range(len(weekdays)):
			print(i+1, "-", weekdays[i])
		weekday = int(input("Insert weekday (number from the list above): "))
	return weekday - 1

def outputResult(startMonth, startDay, startWeekday, endMonth, endDay):
	currentMonth = startMonth
	currentDay = startDay
	currentWeekDay = startWeekday
	while(currentMonth != endMonth or currentDay != endDay):
		print(weekdays[currentWeekDay], currentDay, months[currentMonth], "- ")
		currentDay += 1
		currentWeekDay = (currentWeekDay + 1) % 7
		if(currentMonth in (3, 5, 8, 10) and currentDay > 30):
			currentDay = 1
			currentMonth = (currentMonth + 1) % 12
		elif(currentMonth == 1 and currentDay > 28): # Doesn't count leap years, I know
			currentDay = 1
			currentMonth = (currentMonth + 1) % 12
		elif(currentDay > 31):
			currentDay = 1
			currentMonth = (currentMonth + 1) % 12

print("Use this script to generate dated lines which you can write daily plans on.")
print("\nINSERT START DATE")
startMonth = chooseMonth()
startDay = chooseDay(startMonth)
startWeekday = chooseWeekday()
print("\nINSERT END DATE")
endMonth = chooseMonth()
endDay = chooseDay(endMonth)
outputResult(startMonth, startDay, startWeekday, endMonth, endDay)
