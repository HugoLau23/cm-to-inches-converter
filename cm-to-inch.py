length = float(input("How long is it? "))
unit = input("inch or cm? ")

if unit == "inch" or "INCH" or "in" or "IN":
    print(str(float(length)*2.54) + " cm")
elif unit == "cm" or "CM":
    print(str((length)*0.39370079) + " inches")
else:
    print("Please enter correct unit")