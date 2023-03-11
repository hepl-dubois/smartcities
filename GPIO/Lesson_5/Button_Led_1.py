# Importation de la bibliothèque "machine"
import machine

# Initialisation de la broche 16 en tant qu'entrée et de la broche 18 en tant que sortie
BUTTON = machine.Pin(16, machine.Pin.IN)
LED = machine.Pin(18, machine.Pin.OUT)

# Boucle infinie 
while True:
    # Lecture de la valeur du bouton et stockage dans la variable "val"
    val = BUTTON.value()
    # Si la valeur du bouton est de 1 (c'est-à-dire si le bouton est enfoncé), allume la LED en mettant la valeur de la broche à 1
    if val == 1:
        LED.value(1)
    # Sinon (c'est-à-dire si le bouton n'est pas enfoncé), éteint la LED en mettant la valeur de la broche à 0
    else:
        LED.value(0)
