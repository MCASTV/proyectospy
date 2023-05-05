#-*- coding : utf-8 -*-

"""References
    Power / Potencia V*i, V^2 / R, R*i^2
    Current / Intensidad  V/R, P/V, 
    Resistor / Resistencia V/I, 
    Voltage / Voltaje R*I, P/I
"""

class Serie():
    def __clear__(self):
        self._Resistor.clear()
        self._Sum = 0

    def __init__(self):
        self._Resistor = []
        self._Sum = 0
    def __add__(self, resistor):
        self._Resistor.append(resistor)

    def __RT__(self):
        for i in self._Resistor:
            self._Sum += i
        #Total resistance
        print(f"\nThe total resistance is:\n{self._Sum}Ω")


class Parallel():
    def __clear__(self):
        self._Resistor.clear()
        self._Sum = 0

    def __init__(self):
        self._Resistor = []
        self._Sum = 0

    def __add__(self, resistor):
        self._Resistor.append(resistor)

    def __RT__(self):
        for i in self._Resistor:
            self._Sum += 1/i
            total_sum = 1/self._Sum
        #Total resistance
        print(f"\nThe total resistance is {total_sum}Ω")