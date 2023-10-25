x = "y"
while x == "y":
  print("Podaj pierwsza liczbe:")
  number1 = int(input())
  print("Podaj druga liczbe:")
  number2 = int(input())
  print("Wybierz: 1 dodawanie, 2 odejmowanie, 3 mnozenie, 4 dzielienie,")
  print(" 5 - dzielienie calkowite, 6 - reszta z dzielienia, 7 - potega")
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
#Chyba nie dziala ze wszystkim liczbami minusowym,  5 / 10 = 0 przy calkowitych i 2.0 przy zwyklym dzielieniu