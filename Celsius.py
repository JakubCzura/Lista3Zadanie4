#klasa Kuby

import Temperature
import Kelvin
import Fahrenheit

class Celsius(Temperature.Temperature):
    def __init__(self, temperature):
        self._temperature = temperature
    
    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    def __str__(self):
        return str(self.temperature) + " stopni w skali Celsius"

    def __repr__(self):
        return self.__class__.__name__

    def above_freezing(self):
        if self._temperature > 0:
            return True
        else:
            return False

    def convert_to_Fahrenheit(self):
        temp = self._temperature/0.556 + 32.0
        return Fahrenheit.Fahrenheit(temp)

    def convert_to_Celsius(self):
        return Celsius(self._temperature)
    
    def convert_to_Kelvin(self):
        temp = self._temperature + 273.16
        return Kelvin.Kelvin(temp)




