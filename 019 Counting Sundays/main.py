#!/usr/bin/python3.5

months = ["january", "february", "mars", "april", "may", "june", "july", "august", "septemer", "oktober", "november", "december"]
days = ["monday" , "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

START_YEAR 			= 1900
YEARS_PER_CENTURY 	= 100
MONTHS_PER_YEAR 	= 12
DAYS_PER_MONTH		= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS_PER_WEEK 		= 7

def isLeapYear(year):
	return ((year%4==0) and (year%100!=0) or (year%400==0))


sundays = 0
current_day = 0
for year in range(START_YEAR, START_YEAR+YEARS_PER_CENTURY+1):
	for month in range(MONTHS_PER_YEAR):
		print(str(year) + ": "+ str(months[month]) + ": " + (str(DAYS_PER_MONTH[month]) if not (month == 1 and isLeapYear(year)) else str(DAYS_PER_MONTH[month]+1)))
		for day in range(DAYS_PER_MONTH[month] if not (month == 1 and isLeapYear(year)) else DAYS_PER_MONTH[month]+1): #Maybe i shouldn't have used ternaries here
			if(year > 1900): #past 1900
				if(day == 0): # first day of month
					if(current_day%DAYS_PER_WEEK == 6): #is a sunday
						sundays += 1
			current_day += 1

print(str(sundays))
