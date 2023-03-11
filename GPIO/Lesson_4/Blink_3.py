# Importation des bibliothèques "machine" et "utime"
import machine
import utime

# Initialisation de la broche 16 en tant que sortie
LED = machine.Pin(16, machine.Pin.OUT)

# Boucle infinie pour allumer et éteindre la LED
while True:
    # Allume la LED en mettant la valeur de la broche à 1
    LED.value(1)
    # Attend 1 seconde avant d'éteindre la LED
    utime.sleep(1)
    # Éteint la LED en mettant la valeur de la broche à 0
    LED.value(0)
    # Attend 1 seconde avant de rallumer la LED
    utime.sleep(1)
