
uu = int(input("Type in numbers how many units you have consumed"))

if uu <= 50 :

    total= uu*2.6 + 25
    print(total)

elif uu <= 100 :

    total= uu*3.25 + 35
    print(total)

elif uu <= 200 :

    total= uu*5.26 + 45
    print(total)

else:

    total= uu*8.45 + 75
    print(total)