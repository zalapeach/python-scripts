year = int(input("Gime a year: "))
if (year < 1582):
  print("Not within the Gregorian calendar period")
elif (year % 4 == 0):
  if (year % 100 == 0):
    if (year % 400 == 0):
      print("Leap year")
    else:
      print("Common year")
  else:
    print("Leap year")
else:
  print("Common year")
