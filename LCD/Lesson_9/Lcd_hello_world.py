from lcd1602 import LCD1602  # importer la bibliothèque pour LCD
from machine import I2C, Pin  # importer les bibliothèques pour I2C et Pin
from utime import sleep  # importer la bibliothèque pour la pause

i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)  # initialiser I2C sur les broches SCL et SDA
d = LCD1602(i2c, 2, 16)  # initialiser l'écran LCD sur le bus I2C, avec 2 lignes et 16 caractères

d.display()  # activer l'affichage
sleep(1)
d.clear()  # effacer l'écran
d.print('Hello')  # afficher "Hello" sur la première ligne

sleep(1)
d.setCursor(0, 1)  # positionner le curseur sur la deuxième ligne
d.print('world')  # afficher "world" sur la deuxième ligne

