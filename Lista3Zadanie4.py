import abc

class Temperature(abc.ABC):

    @abc.abstractclassmethod
    def __init__(self, temperature):
        self.temperature = temperature

    @classmethod
    def __str__(self):
        return f"{self.temperature} stopni w skali Celsjusz"

    @classmethod
    def __repr__(self):
         return self.__class__.__name__
   
    @property
    def temperature(self):
        return self.temperature

    @temperature.setter
    def temperature(self, value):
        self.temperature = value
        #self.__dict__['temperature'] = value


    @classmethod
    def above_freezing(self):
        if self.temperature > 0:
            return True
        else:
            return False

    @abc.abstractclassmethod
    def convert_to_Fahrenheit(self):
        raise NotImplementedError


    @abc.abstractclassmethod
    def convert_to_Celsius(self):
        raise NotImplementedError


    @abc.abstractclassmethod
    def convert_to_Kelvin(self):
        raise NotImplementedError





