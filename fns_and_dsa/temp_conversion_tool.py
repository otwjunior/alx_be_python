FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR =9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR) + 32 

temperature = int(input('Enter the temperature to convert: '))
conversion = input('Is this temperature in Celsius or Fahrenheit? (C/F): ')
if conversion == 'C':
    T=convert_to_fahrenheit(temperature)
    print(f"{temperture:.1f}°C is {T:.1f}°F")
else:
    T=convert_to_celsius(temperature)
    print(f"{temperature:.1f}°F is {T:.1f}°C")