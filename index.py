from datetime import date

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
def delta_days(today):
    days_remaining = today.day
    payday = 14
    if payday != days_remaining:
        days_remaining = payday - days_remaining
        return days_remaining

target_date = date(2022, 12, 14)
todays_date = date.today()

delta_days(todays_date)

#returns days as int
def days_remaining(target_date, todays_date):
    i = target_date - todays_date
    return i.days
    
days_remaining_int = days_remaining(target_date, todays_date)

#add days to final cacluation if payday falls on a weekend
weekend = target_date.isoweekday()
if weekend == 7:
 days_remaining_int = days_remaining_int + 1
elif weekend == 6:
 days_remaining_int = days_remaining_int + 2
else: pass

#Final results
def daily_budget(bank_balance):
    print("Days remaining:", days_remaining_int)
    print("Allowance per day:",(round((bank_balance - sum(expenses_sum)) / days_remaining_int, 2)))
    
daily_budget(bank_balance)
