#python_dates
from datetime import date, timedelta, datetime

today = date.today()
print (today)

f_day = today.strftime("%a %d.%B.%Y")
print(f_day)

date_after_382_days = today + timedelta(days=382)
print(date_after_382_days)

#2025-01-15 1995-09-06
#number of days, number of weeks, number of months
date1 = datetime(2025, 1, 15)
date2 = datetime(1995, 9, 6)

difference = date1 - date2

print("Number of days between the dates:", difference.days)

date1 = datetime(2025, 1, 15)
date2 = datetime(1995, 9, 6)

difference = date1 - date2

# Convert days to weeks
weeks = difference.days / 7

# Print the number of weeks
print("Number of weeks between the dates:",weeks)

date1 = datetime(2025, 1, 15)
date2 = datetime(1995, 9, 6)

# Calculate the number of months
years_difference = date1.year - date2.year
months_difference = date1.month - date2.month

# Total months difference
total_months = years_difference * 12 + months_difference

# Adjust for days (if the end day is before the start day)
if date1.day < date2.day:
    total_months -= 1

# Print the number of months
print("Number of months between the dates:",total_months)