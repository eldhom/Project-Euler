#!/usr/bin/python3.5

YEARS_PER_CENTURY 	= 100
MONTHS_PER_YEAR 	= 12
DAYS_PER_MONTH		= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS_PER_YEAR 		= 365
DAYS_PER_WEEK 		= 7

firstMonthSundays = 0
current_day = 0
for year in range(YEARS_PER_CENTURY):
	for month in range(MONTHS_PER_YEAR):
		for days in range(DAYS_PER_MONTH[month] if not ((month==2) and (year%4==0) and (year%100!=0) or (year%400==0)) else DAYS_PER_MONTH[month]+1): #Maybe i shouldn't have used ternaries here
			current_day += 1
			if(not current_day%7):
				current_day = 0
				if(month == 0):
					firstMonthSundays +=1

print(str(firstMonthSundays))
