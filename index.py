from datetime import date
import datetime

print("Please enter current bank balance:")
bank_balance = int(input())
print("Bank balance:", bank_balance, "CZK")
expense_input = input("Are all expenses paid?: ")

expenses_sum = []

if expense_input == "no":
    expenses = [["rent", 12000, 0], ["vzp", 2187, 0], ["o2_home", 517.99, 0], ["o2_mobile", 350, 0], ["litacka", 550, 0]]
    for a in expenses:
     print("Is", a[0], "paid?") 
     answer = input("A: ")
     if answer == "no":
           a = a[1]
           expenses_sum.append(a)
    else: 
     a = a[2]
     expenses_sum.append(a)

#Date data
#payday is always assumed to be the 14th of each month
todays_date = date.today()
def delta_days(today):
    global days_remaining
    global payday
    days_remaining = today.day
    payday = 14
    if payday != days_remaining:
        days_remaining = payday - days_remaining
        return days_remaining
    else: days_remaining = 0

delta_days(todays_date)

#add days to final cacluation if payday falls on a weekend
day_of_week = todays_date + datetime.timedelta(payday-1)
weekend = day_of_week.isoweekday()
if weekend == 7:
 days_remaining = days_remaining + 1
elif weekend == 6:
 days_remaining = days_remaining + 2
else: pass

#Final results
def daily_budget(bank_balance):
    print("Days remaining:", days_remaining)
    print("Allowance per day:",(round((bank_balance - sum(expenses_sum)) / days_remaining, 2)))
    
daily_budget(bank_balance)