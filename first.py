#constants
AL = 26.29815
O = 15.9994
CH3 = 15.0235
ALOCH3 = AL + O + CH3

#function
def getFormulas(m):
    formulas = []

    max_value = int(max(m/AL, m/O, m/CH3))
    for al in range(1, max_value + 1):
        for o in range(1, max_value + 1):
            for ch3 in range(1, max_value + 1):
                if 0 <= m - (AL*al + O*o + CH3*ch3) <= AL*al and 0 <= m - (AL*al + O*o + CH3*ch3) <= O*o and 0 <= m - (AL*al + O*o + CH3*ch3) <= CH3*ch3:
                    formulas.append({"al": al, "o": o, "ch3": ch3})

    return formulas

def checkIfOne(n):
    return str(n) if n != 1 else ""

#main

#input
loop = True
while loop == True:
    try:
        a = float(input("a = "))
        b = float(input("b = "))
    except ValueError:
        print("Error. Value must be a number")
    else:
        loop = False

#function call
upper = getFormulas(a + b)
lower = getFormulas(a - b)

#merge both results
formulas = upper + lower

#output
if len(formulas) == 0:
    print("There are no possible formulas")
else:
    for f in formulas:
        print("Al", checkIfOne(f["al"]), "O", checkIfOne(f["o"]), "(CH3)", checkIfOne(f["ch3"]), sep="")