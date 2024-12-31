UserTemp = int(input("Please enter the temperature in Celsius: "))

if UserTemp >= 30:
    print("You should wear light clothe.!")
elif UserTemp >= 20 and UserTemp < 30:
    print("You should wear a T-shirt.")
elif UserTemp >= 10 and UserTemp < 20:
    print("You should wear warm clothes")
elif UserTemp >= 0 and UserTemp < 10:
    print("You should wear a jacket.")
else:
    print("You should wear lots of warm coats and sweaters.")