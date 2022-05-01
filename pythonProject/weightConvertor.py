### this program is based on if statement

weight = int(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")

if 'k' == unit.lower():
    # weight = float(weight) * 0.45
    converted = weight * 0.45
    print(f"you are {converted} kgs")
elif 'l' == unit.lower():
    # weight = float(weight) * 2.2
    converted = weight / 0.45
    print(f"you are {converted}  pounds")
else:
    print("enter correct unit")
