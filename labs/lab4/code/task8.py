sp = int(input("Введите сумму покупки: "))
if sp < 1000:
  s = 0
elif 1000 <= sp < 5000:
  s = 5
elif 5000 <= sp < 10000:
  s = 10
else:
  s = 15
op = sp - sp*(s/100)
print(f"Ваша скидка: {s}%")
print(f"К оплате:{op}")