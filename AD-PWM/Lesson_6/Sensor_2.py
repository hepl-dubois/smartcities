# Importation des bibliothèques "ADC" et "Pin" pour accéder aux broches analogiques et numériques
# Importation de la fonction "sleep" pour mettre le programme en pause
from machine import ADC, Pin
from time import sleep

# Initialisation de la broche numérique 16 pour contrôler la LED
LED = Pin(16, Pin.OUT)

# Initialisation de la broche analogique 1 pour le capteur de position rotatif
ROTARY_ANGLE_SENSOR = ADC(1)

# Boucle infinie pour lire la valeur de la broche analogique
while True:
    # Lecture de la valeur de la broche analogique et affichage de celle-ci
    rotary_value = ROTARY_ANGLE_SENSOR.read_u16()
    print(rotary_value)
    # Si la valeur de la broche est supérieure à 30000, allume la LED pendant 1 seconde
    if rotary_value > 30000:
        LED.value(1)
        sleep(1)
    # Sinon, éteint la LED pendant 1 seconde
    else:
        LED.value(0)
        sleep(1)
