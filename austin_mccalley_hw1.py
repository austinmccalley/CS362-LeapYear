'''
NOTE: THIS IS PYTHON3 NOT PYTHON2
How to run python3 austin_mccalley_hw1.py
It will prompt you for a year to input
'''


def isInt(s):
    for c in s:
        if not(c >= '0' and c <= '9'):
            return False
    return True


yearStr = input("Please enter a year: ")

if not isInt(yearStr):
  print('The year in which you provided was not a valid integer')
  exit(1)

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
