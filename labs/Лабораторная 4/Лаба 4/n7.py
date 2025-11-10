n1, n2, n3 = map(int, input("Введите 3 числа: ").split())

if n1 <= n2 and n1 <= n3:
    print(f"Наименьшее число: {n1}")
elif n2 <= n1 and n2 <= n3:
    print(f"Наименьшее число: {n2}")
else:
    print(f"Наименьшее число: {n3}")