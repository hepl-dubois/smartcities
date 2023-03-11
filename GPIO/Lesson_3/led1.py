# Importation de la bibliothèque "machine"
import machine

# Initialisation de la broche 16 en tant que sortie
LED = machine.Pin(16, machine.Pin.OUT)

# Allume la LED en mettant la valeur de la broche à 1
LED.value(1)