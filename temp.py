#temparature conversion program
#Fahrenheit to Celsius
#Celsius to Fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9.0/5.0) + 32
    return fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
print("Temperature in Celsius: ", fahrenheit_to_celsius(fahrenheit))
celsius = float(input("Enter temperature in Celsius: "))
print("Temperature in Fahrenheit: ", celsius_to_fahrenheit(celsius))
