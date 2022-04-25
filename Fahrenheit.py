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

    #@abc.abstractmethod
    def convert_to_Fahrenheit(self):
        return Fahrenheit(self._temperature)

    #@abc.abstractmethod
    def convert_to_Celsius(self):
        temp = 0.556 * (self._temperature - 32.0)
        return Celsius(temp)
    

    #@abc.abstractmethod
    def convert_to_Kelvin(self):
        temp = temp = 0.556 * (self._temperature - 32.0) + 273.16
        return Kelvin(temp)
    




