#annual salary and monthly salary 
base_annual_salary = float(input("starting annual salary:"))

#fixed data
total_cost = 1000000 #dream home cost
portion_down_payment = 0.25*total_cost #total down payment
semi_annual_raise = 0.07 #semi-annual salary raise 
monthly_r = 0.04/12 #monthly returns
min_months = 36

#epsilon 
e = 100

#bisectional search bounds
initial_high = 10000
high = initial_high
low = 0

#while loop intial data
count = 0 #how many times the loop occured
current_savings = 0
portion_saved = (high+low)//2

while abs(current_savings - portion_down_payment) >= e:
    count += 1 
    current_savings = 0
    annual_salary = base_annual_salary
    monthly_salary = annual_salary/12

    monthly_deposit = monthly_salary * (portion_saved / 10000)

    for month in range(1, min_months+1):
        current_savings += monthly_deposit + (current_savings*monthly_r)

        if month % 6 == 0:
            annual_salary += (annual_salary * semi_annual_raise)
            monthly_salary = annual_salary / 12
            monthly_deposit = monthly_salary * (portion_saved / 10000)

    prev_portion = portion_saved
    if current_savings < portion_down_payment:
        low = portion_saved
    else:
        high = portion_saved

    
    portion_saved = int(round((high + low) / 2))
    if prev_portion == portion_saved:
            break

if portion_saved == initial_high:
    print("Not possible to acquire the house within 36 months.")
else:
    print("Best savings rate: ", (portion_saved / 10000))
    print("Steps in Bisection search: ", count)