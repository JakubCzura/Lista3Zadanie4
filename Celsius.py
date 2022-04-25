import Temperature

class Celsius(Temperature.Temperature):
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
        temp = self.temperature/0.556 + 32.0
        return Fahrenheit(self, temp)

    #@abc.abstractmethod
    def convert_to_Celsius(self):
        return Celsius(self, self.temperature)
    
    #@abc.abstractmethod
    def convert_to_Kelvin(self):
        temp = self.temperature + 273.16
        return Kelvin(self, temp)




