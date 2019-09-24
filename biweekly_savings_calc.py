# Simple byweekly python calculator
# that determines how long it will take
# you to reach a savings goal


savings_account = 0
monthly_expenses = 0

rent = input("How much do you pay for rent? ")
rent = float(rent)
biweekly_earnings = input("How much do you earn biweekly?")
biweekly_earnings = float(biweekly_earnings) * 2 
saving_goal = input("How much do you want to save? ")
saving_goal = float(saving_goal)
food = input("How much do you spend in food every month? ")
food = float(food)
donation = input("How much do you give away? ")
donation = float(donation)
monthly_expenses = rent + food + donation
savings_account = biweekly_earnings - monthly_expenses
time_to_save = saving_goal / savings_account
time_to_save = float(time_to_save)

print("It will take you", round(time_to_save), "months to save", "$", saving_goal)
