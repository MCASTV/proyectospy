# -*- coding : utf-8 -*-

"""References
    Power / Potencia V*i, V^2 / R, R*i^2
    Current / Intensidad  V/R, P/V, 
    Resistor / Resistencia V/I, 
    Voltage / Voltaje R*I, P/I
"""

import Circuito as cr

# INPUT FUNCTIONS
# VOLTAGE
def involt():
    try:
        dblv = float(input("Enter the value of Volts: "))
        return dblv
    except ValueError:
        print("\nPlease enter a number")
        Law()

# CURRENT
def incur():
    try:
        dbli = float(input("Enter the value of Current: "))
        return dbli
    except ValueError:
        print("\nPlease enter a number")
        Law()

# RESISTANCE
def inresist():
    try:
        dblr = float(input("Enter the value of Resistance: "))
        return dblr
    except ValueError:
        print("\nPlease enter a number")
        Law()

# POWER
def inpower():
    try:
        dblp = float(input("Enter the value of Power: "))
        return dblp
    except ValueError:
        print("\nPlease enter a number")
        Law()


# PROCESS FUNCTIONS
# VOLTAGE
def calcvol(dblr, dblc):
    dblvol = dblr * dblc
    return dblvol

# CURRENT
def calccur(dblv, dblr):
    dblcur = dblv/dblr
    return dblcur

# RESISTANCE
def calcres(dblc, dblvo):
    dblres = dblvo/dblc
    return dblres

# POWER
def calcpower(dblc, dblv):
    dblpow = dblc * dblv
    return dblpow


# OUTPUT FUNCTIONS
# VOLTAGE
def outvol(dblv,):
    print("The Volts are ", format(dblv, ".2f"), " Volts")

# CURRENT
def outcur(dblc):
    print("The Current is ", format(dblc, ".2f"), " Amps")

# RESISTANCE
def outrest(dblr):
    print("The Resistance is ", format(dblr, ".2f"), " Ohms")

# POWER
def outpower(dblp):
    print("The Power is of ", format(dblp, ".2f"), " Watts")


# MAIN()
def Law():
    strloop = "Y"
    while(strloop == "Y"):
        print("\n____________________")
        print("   Advanced Calc")
        print("____________________")
        print("\n1 | Find Volts",
              "\n2 | Find Current ",
              "\n3 | Find Resistance",
              "\n4 | Find Power",
              "\n\n0 | Back to Main Menu")
        strask = input("\nEnter your choice: ")
        dblx = 0
        dbly = 0
        if(strask == "1"):
            print("\n____________________")
            print("--------Volts-------\n")
            # calculate voltage
            dblx = inresist()
            dbly = incur()
            dblx = calcvol(dblx, dbly)
            outvol(dblx)
        elif(strask == "2"):
            print("\n____________________")
            print("-------Current------\n")
            # calculate current
            dblx = involt()
            dbly = inresist()
            dblx = calccur(dblx, dbly)
            outcur(dblx)

        elif(strask == "3"):
            print("\n____________________")
            print("-----Resistance-----\n")
            # calculate resistance
            dblx = incur()
            dbly = involt()
            dblx = calcres(dblx, dbly)
            outrest(dblx)

        elif(strask == "4"):
            print("\n____________________")
            print("--------Power-------\n")
            # calculate power
            dblx = involt()
            dbly = incur()
            dblx = calcpower(dblx, dbly)
            outpower(dblx)

        elif(strask == "0"):
            cr.main()
        else:
            print("\nPlease enter a valid option")
