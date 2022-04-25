import Temperature

class Kelvin(Temperature.Temperature):
    def __init__(self):
        super().__init__(temperature)

    @property
    def temperature(self):
        return self.temperature

    @temperature.setter
    def temperature(self, value):
        self.temperature = value

    #@abc.abstractmethod
    def convert_to_Fahrenheit(self):
        temp = 1.8*(self.temperature-273) + 32
        return Fahrenheit(self, temp)

    #@abc.abstractmethod
    def convert_to_Celsius(self):
        temp = self.temperature - 273.16
        return Celsius(self, temp)
    
    #@abc.abstractmethod
    def convert_to_Kelvin(self):
        return Kelvin(self, self.temperature)



