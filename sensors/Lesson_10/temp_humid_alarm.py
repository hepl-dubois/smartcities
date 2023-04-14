from lcd1602 import LCD1602
from dht11 import *
from machine import I2C, Pin, ADC, PWM
from utime import sleep

# Configuration des broches I2C et initialisation de l'écran LCD
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16)
d.display()

# Configuration du capteur de température et d'humidité et du buzzer
dht2 = DHT(18)
buzzer = PWM(Pin(16))

while True:
    # Lecture de la température et de l'humidité
    temp, humid = dht2.readTempHumid()
    sleep(1)

    # Affichage de la température et de l'humidité sur l'écran LCD
    d.clear()
    d.setCursor(0, 0)
    d.print("Temp : " + str(temp))
    d.write(0b11011111) # Affiche le symbole "°"
    d.print("C") # Affiche le "C"
    d.setCursor(0, 1)
    d.print("Humid : " + str(humid))
    sleep(1)
    
    # Si la température est supérieure à 23°C ou l'humidité est inférieure à 80%, le buzzer sonne
    if temp > 25 or humid < 30:
        buzzer.freq(1000)
        buzzer.duty_u16(1000)
    else:
        buzzer.duty_u16(0) # Ferme le buzzer
