'''
NOTE: THIS IS PYTHON3 NOT PYTHON2
How to run python3 austin_mccalley_hw1.py
It will prompt you for a year to input
'''

yearStr = input("Please enter a year: ")

year = int(yearStr)

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(yearStr + " is a leap year")
    else:
      print(yearStr + " is not a leap year")
  else:
    print(yearStr + " is a leap year")
else:
  print(yearStr + " is not a leap year")

