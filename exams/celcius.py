try:
    c = float(input("Enter temperature in Celsius:") )
    f = (c*(9/5))+32
    print("Temperature in Fahrenheit is : ", f)
except:
    print("Enter a valid value for temperature")