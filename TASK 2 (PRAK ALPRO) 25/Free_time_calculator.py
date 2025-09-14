#Simple free time in a week
sleeep = float(input("enter your sleep time in a day = "))
work = float(input("Enter your working time in a day = "))
relaxing_weekday = float(input("Enter your relaxing time in a weekday = "))
relaxing_weekend = float(input("Enter your relaxing time in a weekend = "))

#use operator
time_weekday = 24 - sleeep - work - relaxing_weekday
time_weekend = 24 - sleeep - relaxing_weekend
total_time = 5 * time_weekday + 2 * time_weekend

#pint all the program
print(f"Your free time in a weekday is ", time_weekday)
print(f"Your free time in a weekend is ", time_weekend)
print(f"Your total free time in a week is ", total_time)


