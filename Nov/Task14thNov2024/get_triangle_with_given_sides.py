#Find the type of triangle with given sides

#Get user input
aValue = int(input("Enter side a: "))
bValue = int(input("Enter side b: "))
cValue = int(input("Enter side c: "))

aPow = pow(aValue, 2)
bPow = pow(bValue, 2)
cPow = pow(cValue, 2)

if aPow == cPow + bPow or bPow == aPow+cPow or cPow == aPow+bPow:
        print("Triangle is Right angled ")

elif aPow > cPow + bPow or bPow > aPow+cPow or cPow > aPow+bPow:
        print("Triangle is Obtuse angled")
else:
        print("Triangle is Acute angled ")