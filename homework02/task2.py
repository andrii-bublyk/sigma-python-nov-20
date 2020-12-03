user_string = input("enter string: ")

temperature_string = "".join(c for c in user_string if c.isdigit())

if not temperature_string:
    raise ValueError("there is no number")

if len(temperature_string) != len(user_string) - 1:
    raise ValueError("incorrect units of measurement")

if user_string.endswith("C"):
    temperature_celsius = int(temperature_string)
    temperature_fahrenheit = round(temperature_celsius * 9/5 + 32)
    print(f"{temperature_celsius}C is {temperature_fahrenheit}F")
elif user_string.endswith("F"):
    temperature_fahrenheit = int(temperature_string)
    temperature_celsius = round((temperature_fahrenheit - 32) * 5 / 9)
    print(f"{temperature_fahrenheit}F is {temperature_celsius}C")
else:
    raise ValueError("incorrect units of measurement")
