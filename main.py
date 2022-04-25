import Temperature
import Celsius
import Kelvin
import Fahrenheit


if __name__ == '__main__':

    F = Fahrenheit.Fahrenheit(2)
    F.temperature = 32
    print(F.temperature)

    K = Kelvin.Kelvin(10)
    K.temperature = 40
    print(K.temperature)

    C = Celsius.Celsius(50)
    C.temperature = 51
    print(C.temperature)

    K2 = C.convert_to_Kelvin()
    print(K2.temperature)

    C2 = K2.convert_to_Celsius()
    print(C2)

    F = F.convert_to_Fahrenheit()
    print(repr(F))
