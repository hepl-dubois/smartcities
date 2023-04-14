from lcd1602 import LCD1602   # Importe la bibliothèque pour l'écran LCD
from dht11 import *           # Importe la bibliothèque pour le capteur DHT11
from machine import I2C,Pin,ADC  # Importe la bibliothèque pour les ports d'entrée/sortie
from utime import sleep       # Importe la fonction sleep pour la pause entre chaque lecture

i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)  # Configure le port I2C pour la communication avec l'écran LCD
d = LCD1602(i2c, 2, 16)      # Initialise l'objet LCD avec une ligne de 2 caractères et 16 colonnes
d.display()                  # Active l'écran LCD
dht2 = DHT(16)               # Initialise l'objet DHT pour la broche 16 (où le capteur est connecté)
miniFan = machine.Pin(18,machine.Pin.OUT)  # Initialise la broche 18 pour contrôler le mini ventilateur (sortie)

while True:                  # Boucle infinie pour la lecture continue des données
    temp = dht2.readTemperature()   # Lit la température à partir du capteur DHT11
    sleep(1)                 # Pause de 1 seconde avant la lecture suivante
    d.clear()                # Efface l'écran LCD
    d.setCursor(0,0)         # Déplace le curseur en haut à gauche de l'écran LCD
    d.print("Temp:"+str(temp))   # Affiche la température sur l'écran LCD
    sleep(1)                 # Pause de 1 seconde avant la lecture suivante

    if temp > 26:            # Si la température est supérieure à 26°C
        miniFan.value(1)     # Active le mini ventilateur
    else:
        miniFan.value(0)     # Désactive le mini ventilateur
