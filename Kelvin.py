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

    #@abc.abstractmethod
    def convert_to_Fahrenheit(self):
        temp = 1.8*(self._temperature-273) + 32
        return Fahrenheit.Fahrenheit(temp)

    #@abc.abstractmethod
    def convert_to_Celsius(self):
        temp = self._temperature - 273.16
        return Celsius.Celsius(temp)
    
    #@abc.abstractmethod
    def convert_to_Kelvin(self):
        return Kelvin(self._temperature)



