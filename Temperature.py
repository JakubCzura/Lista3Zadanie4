#klasa Kuby

import abc

class Temperature(abc.ABC):

    @abc.abstractmethod
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    @abc.abstractmethod
    def temperature(self):
        raise NotImplementedError

    @temperature.setter
    @abc.abstractmethod
    def temperature(self, value):
        raise NotImplementedError

    @classmethod
    def __str__(self):
        return self.temperature + " stopni w skali Celsjusz"

    @classmethod
    def __repr__(self):
         return self.__class__.__name__

    @classmethod
    def above_freezing(self):
        if self._temperature > 0:
            return True
        else:
            return False

    @abc.abstractmethod
    def convert_to_Fahrenheit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def convert_to_Celsius(self):
        raise NotImplementedError

    @abc.abstractmethod
    def convert_to_Kelvin(self):
        raise NotImplementedError



