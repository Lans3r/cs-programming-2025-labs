numbers = input("Введите три числа через запятую: ")
num1, num2, num3 = map(int, numbers.split(','))
result = (num1 + num3) // num2
print(f"Результат вычисления: {result}")