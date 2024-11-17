#Write a program that prints numbers from 1 to 100.
# However, for multiples of 3, print "Fizz" instead of the number, and for multiples of 5,
# print "Buzz." For numbers that are multiples of both 3 and 5, print "FizzBuzz." ( for, if)
#

for nValue in range(1, 100):
    if nValue % 15 == 0:
        print("FizzBuzz")
    elif nValue % 3 == 0:
        print("Fizz")
    elif nValue % 5 == 0:
        print("Buzz")
    else:
        print(nValue)