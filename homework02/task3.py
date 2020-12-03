number = int(input("enter number: "))

if number < 1:
    raise ValueError("input number is less than 1")

symbol = "*"

for n in range(1, number + 1):
    print(symbol * n)
