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

    #@abc.abstractmethod
    def convert_to_Fahrenheit(self):
        temp = self._temperature/0.556 + 32.0
        return Fahrenheit.Fahrenheit

    #@abc.abstractmethod
    def convert_to_Celsius(self):
        return Celsius(self._temperature)
    
    #@abc.abstractmethod
    def convert_to_Kelvin(self):
        temp = self._temperature + 273.16
        return Kelvin.Kelvin(temp)




