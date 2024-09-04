import math
import random

positive = 0
negative = 0
index = 0
solutions_list = []

# Finding real solutions of quadratic equations using the quadratic formula
while index <= 10**20:
    try:
        a = random.randint(-10**20, 10**20); b = random.randint(-10**20, 10**20); c = random.randint(-10**20, 10**20) # Generating random coefficients 
        
        positive = (-b+math.sqrt((b**2)-(4*a*c))) # Calculating the positive solution
        negative = (-b-math.sqrt((b**2)-(4*a*c))) # Calculating the negative solution
        
        index += 1

        solutions_list.append([positive, negative]) # Adding the roots to a solutions list

        print(f"Equation #{index}")
        print("Coefficients:")
        print(a, b, c, sep=" | ")
        print("Solutions:")
        print(positive); print(negative, end="\n\n")

    except ValueError: # Invalid (imaginary or complex solutions)
        print("Not in range", end="\n\n")