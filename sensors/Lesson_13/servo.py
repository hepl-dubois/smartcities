# Importation de la classe Pin depuis le module machine
from machine import Pin

# Importation de la fonction sleep depuis le module utime
from utime import sleep

# Importation de la classe SERVO depuis le module servo
from servo import SERVO

# Instanciation de la classe SERVO avec le Pin 20
servo = SERVO(Pin(20))

# Boucle pour faire tourner le servo 10 fois
for i in range(10):
    # Tourner le servo à l'angle 0
    servo.turn(0)
    # Pause de 1 seconde
    sleep(1)

    # Tourner le servo-moteur à 100 degrés
    servo.turn(100)
    # Pause de 1 seconde
    sleep(1)
