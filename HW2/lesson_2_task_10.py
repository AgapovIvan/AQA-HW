def bank(X, Y):
    interest_rate = 0.10  
    total_amount = X  

    for _ in range(Y):
        total_amount += total_amount * interest_rate  

    return total_amount

initial_deposit = 1000  
years = 5  
result = bank(initial_deposit, years)

print(f"Сумма на счету после {years} лет: {result:.2f} рублей")
