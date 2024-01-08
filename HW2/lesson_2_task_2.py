def is_year_leap(year):
    return year % 4 == 0

chosen_year = int(input("Введите год: ")) 
result = is_year_leap(chosen_year)

print(f"Год {chosen_year}: {result}")