#klasa Maćka

import Temperature
import Celsius
import Fahrenheit

class Kelvin(Temperature.Temperature):
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    def __str__(self):
        return str(self.temperature) + " stopni w skali Kelvin"

    def __repr__(self):
        return self.__class__.__name__

    def above_freezing(self):
        if self._temperature > 273:
            return True
        else:
            return False

    def convert_to_Fahrenheit(self):
        temp = 1.8*(self._temperature-273) + 32
        return Fahrenheit.Fahrenheit(temp)

    def convert_to_Celsius(self):
        temp = self._temperature - 273.16
        return Celsius.Celsius(temp)
    
    def convert_to_Kelvin(self):
        return Kelvin(self._temperature)

    

