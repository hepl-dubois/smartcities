# Importation de la bibliothèque "ADC" pour accéder aux broches analogiques
# Importation de la fonction "sleep" pour mettre le programme en pause
from machine import ADC
from utime import sleep

# Initialisation de la broche analogique 0
ROTARY_ANGLE_SENSOR = ADC(0)

# Boucle infinie pour lire la valeur de la broche analogique & l'afficher
while True:
    print(ROTARY_ANGLE_SENSOR.read_u16())
    sleep(1)
