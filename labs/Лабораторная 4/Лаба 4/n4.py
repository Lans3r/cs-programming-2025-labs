n = int(input("Введите число: "))
if n % 2 == 0 and sum(int(i) for i in str(n)) % 3 == 0:
    print("Число делится на 6")
else:
    print("Число не делится на 6")