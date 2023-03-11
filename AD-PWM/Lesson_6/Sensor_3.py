# Importation des bibliothèques "ADC" et "Pin" pour accéder aux broches analogiques et numériques
# Importation de la fonction "sleep" pour mettre le programme en pause
from machine import ADC, Pin
from time import sleep

# définition de la broche de la LED
LED = Pin(16, Pin.OUT)

# création d'une variable de l'ADC pour la broche 1
ROTARY_ANGLE_SENSOR = ADC(1)

while True:
    # lecture de la valeur analogique du capteur d'angle rotatif
    sensor_value = ROTARY_ANGLE_SENSOR.read_u16()
    print(sensor_value)
    
    # si la valeur est comprise entre 20000 et 40000, allumer la LED
    if 20000 < sensor_value < 40000:
        LED.value(1)
        sleep(1)
    # sinon, éteindre la LED
    else:
        LED.value(0)
        sleep(1)
