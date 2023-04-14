from ws2812 import WS2812 # Importation de la bibliothèque WS2812 pour gérer les LED RGB
from machine import I2C, Pin, ADC # Importation de la bibliothèque machine pour utiliser les broches d'E/S et ADC pour le capteur de lumière et de son
from utime import sleep # Importation de la bibliothèque utime pour la gestion du temps

led = WS2812(18, 1) # Création d'une instance de WS2812 pour contrôler une LED RGB unique branchée sur la broche 18
LIGHT_SENSOR = ADC(0) # Configuration d'un objet ADC pour lire la valeur de la luminosité depuis la broche ADC 0
SOUND_SENSOR = ADC(1) # Configuration d'un objet ADC pour lire la valeur sonore depuis la broche ADC 1

while True: # Boucle principale
    average = 0 # Initialisation de la variable pour calculer la moyenne des valeurs sonores lues
    light = LIGHT_SENSOR.read_u16() / 256 # Lecture de la valeur de la lumière et conversion en valeurs entre 0 et 255
    for i in range(1000): # Lecture des valeurs sonores pendant 1000 fois et calcul de la moyenne
        noise = SOUND_SENSOR.read_u16() / 256 # Lecture de la valeur sonore et conversion en valeurs entre 0 et 255
        average += noise # Ajout de la valeur de bruit actuelle à la somme totale des valeurs sonores
    noise = average / 1000 # Calcul de la moyenne des valeurs sonores
    print(noise) # Affichage de la valeur sonore moyenne sur la console
    
    if light < 80: # Si la lumière est faible (seuil de 80)
        led.pixels_fill((255, 255, 255)) # Allume la LED en blanc
        led.pixels_show() # Met à jour la LED
        sleep(0.2) # Attend 0,2 seconde
    else: # Sinon (lumière suffisante)
        if noise < 25: # Si le bruit est faible (seuil de 25)
            led.pixels_fill((0, 255, 0)) # Allume la LED en vert
            led.pixels_show() # Met à jour la LED
            sleep(1) # Attend 1 seconde
        if noise >= 25 and noise < 50: # Si le bruit est moyen (seuil de 25 à 50)
            led.pixels_fill((255, 255, 0)) # Allume la LED en jaune
            led.pixels_show() # Met à jour la LED
            sleep(1) # Attend 1 seconde
        if noise >= 50: # Si le bruit est élevé (seuil de 50 et plus)
            led.pixels_fill((255, 0, 0)) # Allume la LED en rouge
            led.pixels_show() # Met à jour la LED
            sleep(1) # Attend 1 seconde
