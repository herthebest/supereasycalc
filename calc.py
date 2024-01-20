def calc(operator, value1, value2):
    return eval(f'{value1}{operator}{value2}')

operator = input()
value1 = input()
value2 = input()
result = calc(operator, value1, value2)
print(result)
