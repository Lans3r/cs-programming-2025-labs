year = int(input("Введите год: "))
if year % 4 == 0 and year % 400 != 0:
  print(f"{year} — високосный год" )
elif year % 400 == 0:
  print(f"{year} — високосный год")
else:
  print(f"{year} — не високосный год")