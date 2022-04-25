import Temperature
import Celsius
import Kelvin

class Fahrenheit(Temperature.Temperature):
    def __init__(self, temperature):
        super().__init__(self.temperature)
        self.temperature = temperature

    temperature = 0.0
    @property
    def temperature(self):
        return self.temperature

    @temperature.setter
    def temperature(self, value):
        self.temperature = value

    #@abc.abstractmethod
    def convert_to_Fahrenheit(self):
        return Fahrenheit(self, self.temperature)

    #@abc.abstractmethod
    def convert_to_Celsius(self):
        temp = 0.556 * (self.temperature - 32.0)
        return Celsius(self, temp)
    

    #@abc.abstractmethod
    def convert_to_Kelvin(self):
        temp = temp = 0.556 * (self.temperature - 32.0) + 273.16
        return Kelvin(self, temp)
    




