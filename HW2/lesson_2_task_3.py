import math

def square(side):
    if not isinstance(side, int):
        side = math.ceil(side)
    
    return side * side

side_length = 4.3  
result = square(side_length)

print(f"Площадь квадрата со стороной {side_length}: {result}")
