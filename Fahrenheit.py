import Temperature
import Celsius
import Kelvin

class Fahrenheit(Temperature.Temperature):
    def __init__(self, temperature):
        super().__init__(temperature)

    #@abc.abstractmethod
    def convert_to_Fahrenheit(self):
        return Fahrenheit(self, temperature)

    #@abc.abstractmethod
    def convert_to_Celsius(self):
        temp = 0.556 * (self.temperature - 32.0)
        return Celsjusz(self, temp)

    #@abc.abstractmethod
    def convert_to_Kelvin(self):
        temp = temp = 0.556 * (self.temperature - 32.0) + 273.16
        return Kelvin(self, temp)
    




