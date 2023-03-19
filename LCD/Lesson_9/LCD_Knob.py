from lcd1602 import LCD1602  # importer la classe LCD1602
from machine import I2C, Pin, ADC  # importer les bibliothèques I2C, Pin, ADC
from utime import sleep  # importer la fonction sleep

# créer une instance de la classe ADC avec la broche 0
ROTARY_ANGLE_SENSOR = ADC(0)

# créer une instance de la classe I2C pour communiquer avec l'écran LCD
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)

# créer une instance de la classe LCD1602 pour contrôler l'écran LCD
d = LCD1602(i2c, 2, 16)

# activer l'affichage de l'écran LCD
d.display()

while True:
    sleep(1)  # attendre 1 seconde
    d.clear()  # effacer l'écran LCD
    d.setCursor(0, 0)  # déplacer le curseur en haut à gauche
    d.print(str(ROTARY_ANGLE_SENSOR.read_u16()))  # afficher la valeur lue du capteur de rotation
    d.write(0b11011111) #affiche le symbole "°"
    d.print("C") #affiche le "C"
    sleep(1)  # attendre 1 seconde avant de recommencer
