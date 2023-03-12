# Importation des bibliothèques "ADC" et "Pin" et PWM de la bibliothèque "machine"
from machine import Pin, ADC, PWM

# définition de la broche du capteur d'angle rotatif et initialisation de l'ADC
ROTARY_ANGLE_SENSOR = ADC(0)

# définition de la broche de la LED et initialisation de la PWM
LED_PWM = PWM(Pin(18))
LED_PWM.freq(500)

while True:
    # lecture de la valeur du capteur d'angle rotatif
    val = ROTARY_ANGLE_SENSOR.read_u16()

    # utilisation de la PWM pour contrôler la luminosité de la LED en fonction de la valeur lue
    LED_PWM.duty_u16(val)
