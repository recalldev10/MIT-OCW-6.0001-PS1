#annual salary and monthly salary 
annual_salary = float(input("starting annual salary:"))
monthly_salary = annual_salary/12

#portion_saved = percent of monthly salary
portion_saved = float(input("portion of your salary to be saved:"))
#monthly_portion_saved = portion saved of monthly salary 
monthly_portion_saved = portion_saved*monthly_salary

#dream home cost
total_cost = float(input("cost of your dream home:"))

#total down payment
portion_down_payment = 0.25*total_cost

current_savings = 0

#monthly returns
monthly_r = 0.04/12

month = 0


while current_savings < portion_down_payment:
    current_savings += monthly_portion_saved + (current_savings*monthly_r)
    month += 1

print("needed downpayment: ", portion_down_payment)
print("total savings: ", current_savings)
print(f"number of months: {month}")
