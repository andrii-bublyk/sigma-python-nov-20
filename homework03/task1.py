div_lambda = lambda x, y: x / y if y != 0 else None


print(div_lambda(1, 1))
print(div_lambda(1, 2))
print(div_lambda(2, 1))
print(div_lambda(1, 0))
