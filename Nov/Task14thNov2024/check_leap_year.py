#define variable and assign value
year = 2024

#Or take user input
#year = int(input("Enter a year: "))

# Is it is a centenary year ?
# If value is divisible by 100 with no remainder than
# year is a leap year divided by 400
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

#If it is not divisible by 100 then it is not.
#A year divisible by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year.".format(year))

#else Year is not a leap year
else:
    print("{0} is not a leap year.".format(year))