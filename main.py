x = "y"
while x == "y":
  print("Podaj pierwsza liczbe:")
  number1 = int(input())
  print("Podaj druga liczbe:")
  number2 = int(input())
  print("Wybierz: 1 +, 2 -, 3 *, 4 /, 5-/ calkowite, 6-reszta z /, 7-potega")
  checker = input()
  if checker == "1":
      print(number1 + number2)
  elif checker == "2":
     print(number1 - number2)
  elif checker == "3":
     print(number1 * number2)
  elif checker == "4":
    if number2 == 0:
       print("Liczby sa nie podzielne przez 0")
    else: 
      print(number1 / number2)
  elif checker == "5":
    if number2 == 0:
      print("Liczby sa nie podzielne przez 0")
    else:
      print(number1 // number2)
  elif checker == "6":
    print(number1 % number2)
  elif checker == "7":
    print(number1 ** number2)
  else:
   print("Wrong input")
  print("Powtorzyc? y/n")
  x = input().lower()