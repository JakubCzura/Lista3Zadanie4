import Temperature
import Celsius
import Kelvin

class Fahrenheit(Temperature.Temperature):
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    def __str__(self):
        return str(self.temperature) + " stopni w skali Fahrenheit"

    def __repr__(self):
        return self.__class__.__name__

    def above_freezing(self):
        if self.temperature > 32:
            return True
        else:
            return False 

    def convert_to_Fahrenheit(self):
        return Fahrenheit(self._temperature)

    def convert_to_Celsius(self):
        temp = 0.556 * (self._temperature - 32.0)
        return Celsius(temp)
    
    def convert_to_Kelvin(self):
        temp = temp = 0.556 * (self._temperature - 32.0) + 273.16
        return Kelvin(temp)