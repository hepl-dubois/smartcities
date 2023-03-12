# Importation de la bibliothèque "time"
import utime
# Importation des bibliothèques "Pin" de la bibliothèque "machine"
from machine import Pin, PWM

# définition de la broche pour la PWM et création d'une variable PWM
LED_PWM = PWM(Pin(18))

# initialisation de la valeur du rapport cyclique à 0
val = 0

# fixer la fréquence de la PWM à 500 Hz
LED_PWM.freq(500)

while True:
    # augmenter progressivement la valeur du rapport cyclique jusqu'à 65535
    while val < 65535:
        val = val + 50
        utime.sleep_ms(1)
        LED_PWM.duty_u16(val)
    
    # diminuer progressivement la valeur du rapport cyclique jusqu'à 0
    while val > 0:
        val = val - 50
        utime.sleep_ms(1)
        LED_PWM.duty_u16(val)
