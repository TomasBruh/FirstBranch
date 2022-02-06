nr = int(input("Insert even or odd number: "))
return_conclusion = 0
if nr % 2 == 0:
    return_conclusion = "even"
else:
    return_conclusion = "odd"
print(f"The number inserted was {return_conclusion}")
