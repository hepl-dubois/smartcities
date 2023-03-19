from lcd1602 import LCD1602 # importer la bibliothèque LCD1602
from machine import I2C, Pin, ADC, PWM # importer les bibliothèques Pin, ADC, PWM
from utime import sleep # importer la bibliothèque pour la pause

# Initialisation de l'ADC pour mesurer la tension du potentiomètre
ROTARY_ANGLE_SENSOR = ADC(0)

# Initialisation du PWM pour contrôler la LED
LED_PWM = PWM(Pin(18))

# Initialisation de la communication I2C pour l'afficheur LCD
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)

# Configuration du PWM pour la LED
LED_PWM.freq(500)

# Initialisation de l'afficheur LCD
d = LCD1602(i2c, 2, 16)
d.display()

# Boucle infinie
while True:
    # Lecture de la valeur du potentiomètre
    val = ROTARY_ANGLE_SENSOR.read_u16()
    
    # Mise à jour de la luminosité de la LED en fonction de la valeur lue
    LED_PWM.duty_u16(val)
    
    # Affichage de la valeur du potentiomètre sur l'afficheur LCD
    d.clear() # effacer l'écran LCD
    d.setCursor(0, 0) # déplacer le curseur en haut à gauche
    d.print(str(val)) # afficher la valeur lue du capteur de rotation
    d.write(0b11011111) #affiche le symbole "°"
    d.print("C") #affiche le "C"
    
    # Attente d'une seconde avant la prochaine mesure
    sleep(1)
