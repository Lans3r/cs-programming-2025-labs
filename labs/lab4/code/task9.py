ch = int(input("Введите время (0–23): "))
if 0<= ch <= 5:
  print("Сейчас ночь")
elif 6 <= ch <= 11:
  print("Сейчас утро")
elif 12 <= ch <= 17:
  print("Сейчас день")
elif 18 <= ch <= 23:
  print("Сейчас вечер")