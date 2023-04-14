from lcd1602 import LCD1602
from dht11 import *
from machine import I2C, Pin, ADC
from utime import sleep

# Initialisation de l'I2C pour l'écran LCD
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16)
d.display()

# Initialisation du capteur de température et d'humidité DHT11
dht = DHT(18)

while True:
    # Lecture de la température et de l'humidité
    temp, humid = dht.readTempHumid()
    sleep(1)

    # Effacement de l'écran et positionnement du curseur en haut à gauche
    d.clear()
    d.setCursor(0, 0)

    # Affichage de la température en degrés Celsius
    d.print("Temp:"+str(temp))
    d.write(0b11011111) # Affiche le symbole "°"
    d.print("C") # Affiche le "C"

    # Positionnement du curseur en bas à gauche et affichage de l'humidité
    d.setCursor(0, 1)
    d.print("Humid:"+str(humid))

    # Attente d'une seconde avant la prochaine lecture
    sleep(1)