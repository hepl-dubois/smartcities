# Importation de la bibliothèque "machine" pour accéder aux fonctionnalités matérielles de la carte
import machine
import utime

# Initialisation de la broche 16 en tant qu'entrée et de la broche 18 en tant que sortie
BUTTON = machine.Pin(16, machine.Pin.IN)
LED = machine.Pin(18, machine.Pin.OUT)

# Initialisation de la variable "val" à 0
val = 0

# Boucle infinie
while True:
    # Si la valeur du bouton est de 1 (c'est-à-dire si le bouton est enfoncé), incrémenter la variable "val" de 1 et attendre 1 seconde avant de continuer
    if BUTTON.value() == 1:
        val = val + 1
        utime.sleep(1)
    # Si la variable "val" est égale à 2, la réinitialiser à 0 et attendre 1 seconde avant de continuer
    elif val == 2:
        val = 0
        utime.sleep(1)
    # Allumer/éteindre la LED en fonction de la valeur de "val"
    LED.value(val)
