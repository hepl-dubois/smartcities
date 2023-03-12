# Importation des bibliothèques
from machine import Pin, I2C, ADC, PWM
from time import sleep

# Initialisation de la broche 27 pour le buzzer et définition du volume
buzzer = PWM(Pin(27))
vol = 1000

# Fonction pour jouer la note DO pendant un temps donné
def DO(time):
    buzzer.freq(1046)
    buzzer.duty_u16(vol)
    sleep(time)

# Fonction pour jouer la note RE pendant un temps donné
def RE(time):    
    buzzer.freq(1175) 
    buzzer.duty_u16(vol)
    sleep(time)

# Fonction pour jouer la note MI pendant un temps donné
def MI(time):          
    buzzer.freq(1318) 
    buzzer.duty_u16(vol)
    sleep(time)

# Fonction pour jouer la note FA pendant un temps donné
def FA(time):     
    buzzer.freq(1397) 
    buzzer.duty_u16(vol)
    sleep(time)

# Fonction pour jouer la note SO pendant un temps donné
def SO(time):    
    buzzer.freq(1568) 
    buzzer.duty_u16(vol)
    sleep(time)

# Fonction pour jouer la note LA pendant un temps donné
def LA(time):    
    buzzer.freq(1760) 
    buzzer.duty_u16(vol)
    sleep(time)

# Fonction pour jouer la note SI pendant un temps donné
def SI(time):    
    buzzer.freq(1967) 
    buzzer.duty_u16(vol)
    sleep(time)

# Fonction pour arrêter la sortie du buzzer pendant un temps donné
def N(time):
    buzzer.duty_u16(0) 
    sleep(time)

# Boucle infinie pour jouer la mélodie
while True:
    
    # Jouer la première partie de la mélodie
    DO(0.25)
    N(0.01)
    DO(0.25)
    N(0.01)
    SO(0.25)
    N(0.01)
    SO(0.25)
    N(0.01)
    LA(0.25)
    N(0.01)
    LA(0.25)
    N(0.01)
    SO(0.5)
    N(0.01)
    
    # Jouer la deuxième partie de la mélodie
    FA(0.25)
    N(0.01)
    FA(0.25)
    N(0.01)
    MI(0.25)
    N(0.01)
    MI(0.25)
    N(0.01)
    
    # Jouer la troisième partie de la mélodie
    RE(0.25)
    N(0.01)
    RE(0.25)
    N(0.01)
    DO(0.5)
    N(0.01)
