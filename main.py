import Temperature
import Celsius
import Kelvin
import Fahrenheit


if __name__ == '__main__':

    Fahrenheit1 = Fahrenheit.Fahrenheit(32) #0 Celsjusza
    Fahrenheit2 = Fahrenheit.Fahrenheit(212) # 100 Celsjusza
    Fahrenheit3 = Fahrenheit.Fahrenheit(250)
    Fahrenheit4 = Fahrenheit.Fahrenheit(20)

    Kelvin1 = Kelvin.Kelvin(0) # -273 Celsjusza
    Kelvin2 = Kelvin.Kelvin(273) # 0 Celsjusza
    Kelvin3 = Kelvin.Kelvin(373) # 100 Celsjusza
    Kelvin4 = Kelvin.Kelvin(100)


    Celsius1 = Celsius.Celsius(-250)
    Celsius2 = Celsius.Celsius(0)
    Celsius3 = Celsius.Celsius(140)
    Celsius4 = Celsius.Celsius(100)

    ListOfTemperatures = [Fahrenheit1, Fahrenheit2, Fahrenheit3, Fahrenheit4,
                          Kelvin1, Kelvin2, Kelvin3, Kelvin4,
                          Celsius1, Celsius2, Celsius3, Celsius4]

    for Temperature in ListOfTemperatures:
        print(Temperature)
        if Temperature.above_freezing() == True:
            print("powyzej zera")


    ListOfTemperaturesFahrenheit = [Fahrenheit1, Fahrenheit2, Fahrenheit3, Fahrenheit4,
                                    Kelvin1.convert_to_Fahrenheit(), Kelvin2.convert_to_Fahrenheit(), Kelvin3.convert_to_Fahrenheit(), Kelvin4.convert_to_Fahrenheit(),
                                    Celsius1.convert_to_Fahrenheit(), Celsius2.convert_to_Fahrenheit(), Celsius3.convert_to_Fahrenheit(), Celsius4.convert_to_Fahrenheit()]

    ListOfTemperaturesCelsius = [Fahrenheit1.convert_to_Celsius(), Fahrenheit2.convert_to_Celsius(), Fahrenheit3.convert_to_Celsius(), Fahrenheit4.convert_to_Celsius(),
                                 Kelvin1.convert_to_Celsius(), Kelvin2.convert_to_Celsius(), Kelvin3.convert_to_Celsius(), Kelvin4.convert_to_Celsius(),
                                 Celsius1, Celsius2, Celsius3, Celsius4]

    ListOfTemperaturesKelvin = [Fahrenheit1.convert_to_Kelvin(), Fahrenheit2.convert_to_Kelvin(), Fahrenheit3.convert_to_Kelvin(), Fahrenheit4.convert_to_Kelvin(),
                                Kelvin1.convert_to_Kelvin(), Kelvin2.convert_to_Kelvin(), Kelvin3.convert_to_Kelvin(), Kelvin4.convert_to_Kelvin(),
                                Celsius1, Celsius2, Celsius3, Celsius4]

    for Temperature in ListOfTemperaturesFahrenheit:
        if Temperature.above_freezing() == False:
            print(Temperature)
             
            
    for Temperature in ListOfTemperaturesCelsius:
        if Temperature.above_freezing() == False:
            print(Temperature)

    for Temperature in ListOfTemperaturesKelvin:
        if Temperature.above_freezing() == False:
            print(Temperature)