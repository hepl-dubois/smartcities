import machine # Importation de la bibliothèque machine
import utime # Importation de la bibliothèque utime

button = machine.Pin(18, machine.Pin.IN) # Définition de la broche 18 en entrée
miniFan = machine.Pin(16, machine.Pin.OUT) # Définition de la broche 16 en sortie
val = 0 # Initialisation de la variable val à 0

while True: # Boucle infinie
    val = button.value() # Lecture de la valeur de la broche 18
    if val == 1: # Si la valeur est à 1 (le bouton est enfoncé)
        miniFan.toggle() # Inversion de l'état de la broche 16
        utime.sleep_ms(1000) # Pause de 1 seconde pour éviter les rebonds du bouton
