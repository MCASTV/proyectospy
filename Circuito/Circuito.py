#-*- coding : utf-8 -*-

#Coded ----------: Python3.9.0
#Author --------: Stephano Bravo
#Git Repository : https://github.com/Superlasek/Circuit-Calc--OHM-LAW-

"""References
    Power / Potencia | V*i, V^2 / R, R*i^2
    Current / Intensidad | V/R, P/V, 
    Resistor / Resistencia | V/I, 
    Voltage / Voltaje | R*I, P/I
"""

import time, os
from Calcsimple import *
import Calcsimple as s
from Law import *
import Law as lw

_Parallel = s.Parallel()
_Serie = s.Serie()
circuit = 0

# Function to sum the resistors in a circuit
def sum_resistors(type):
    if  type == 1:
        circuit = _Serie
    else:
        circuit = _Parallel
    
    #Clear value in case of a new calculation
    circuit.__clear__()
    added_resistors = int(input("Resistors to add: "))
    #Limit to 10 resistors
    if added_resistors > 10:
        added_resistors = 10
        print("\nYou can only add 10 resistors at a time")
        print("\nResistors added: 10")
    for i in range(added_resistors):
        #Validate if the input is a number get_number()
        # if input("\nEnter resistor value: ").isdigit():
        #     circuit.__add__(int(input("\nEnter resistor value: ")))
        while True:
            try:
                circuit.__add__(int(input("\nEnter resistor value number {}: ".format(i+1))))
                break
            except ValueError:
                print("\nPlease enter a number")
                continue
    #Total resistance
    #print("\nTotal Resistance: {}".format(circuit.__RT__()))
    circuit.__RT__()

    #print(circuit.__RT__()) #This thing returns none bc two statements of the function lol

    #Back to last menu
    simple()


# Simple calc
def simple():
    print("\n_________________")
    print("   Simple Calc")
    print("_________________")
    while True:
        print("\nType of circuit: ")
        print("1 | Series")
        print("2 | Parallel")
        print("\n0 | Back to Main Menu")
        choice = get_number("\nEnter your choice: ")
        if choice == 1:
            print("\n_________________")
            print("   Series")
            print("_________________")
            sum_resistors(choice)
            print("\n...")
            #Clear terminal screen
            #os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif choice == 2:
            print("\n_________________")
            print("   Parallel")
            print("_________________")
            sum_resistors(choice)
            print("\n...")
            #Clear terminal screen
            #os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif choice == 0:
            print("\nBack to Main Menu...")
            time.sleep(0.5)
            print("\n...")
            #Clear terminal screen
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
            break
        else:
            print("\nPlease enter a valid option")
            continue


#!TESTING
# Get the user input for validate that the input is a number
def get_number(prompt):
    while True:
        try:
            # Return the input as an integer
            return int(input(prompt))
        except ValueError:
            print("Please enter a number")


# Main function...
def main():
    print("""\n
 ██████╗ ██╗  ██╗███╗   ███╗█╗ ███████╗   ██████╗ █████╗ ██╗      ██████╗
██╔═══██╗██║  ██║████╗ ████║╚╝ ██╔════╝  ██╔════╝██╔══██╗██║     ██╔════╝
██║   ██║███████║██╔████╔██║   ███████╗  ██║     ███████║██║     ██║     
██║   ██║██╔══██║██║╚██╔╝██║   ╚════██║  ██║     ██╔══██║██║     ██║     
╚██████╔╝██║  ██║██║ ╚═╝ ██║   ███████║  ╚██████╗██║  ██║███████╗╚██████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝   ╚══════╝   ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝                                                     
    \n""")

    while True:
        print("\n_________________")
        print("   Type of Calc")
        print("_________________")

        print("1 | Simple Calculations")
        print("2 | Advanced Calculations")
        print("\n0 | Exit")

        choice = get_number("\nEnter your choice: ")
        if choice == 1:
            print("\nEntering Simple Calculations mode...")
            time.sleep(0.5)
            print("\n...")
            #Clear terminal screen
            os.system('cls' if os.name == 'nt' else 'clear')
            simple()
            break
        elif choice == 2:
            print("\nEntering Advanced Calculations mode...")
            time.sleep(0.5)
            print("\n...")
            #Clear terminal screen
            os.system('cls' if os.name == 'nt' else 'clear')
            lw.Law()
            break
        elif choice == 0:
            print("\nExiting...")
            time.sleep(0.5)
            print("\n...")
            #Clear terminal screen
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()
        else:
            print("\nPlease enter a valid option")
            continue

if __name__ == '__main__':
    main()