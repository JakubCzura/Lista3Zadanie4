import Temperature
import Celsius
import Kelvin
import Fahrenheit


if __name__ == '__main__':
    print("Hello wrold")

    F = Fahrenheit.Fahrenheit(20)
    F.temperature = 30
    print(F.temperature)

    K = Kelvin.Kelvin(10)
    K.temperature = 40
    print(K.temperature)

    C = Celsius.Celsius(50)
    C.temperature = 51
    print(C.temperature)

    K2 = C.convert_to_Kelvin()
    print(K2.temperature)