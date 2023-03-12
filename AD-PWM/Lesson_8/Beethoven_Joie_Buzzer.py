# Importation des bibliothèques
from machine import Pin, PWM
from time import sleep

# Initialisation de la broche 27 pour le buzzer et définition du volume
buzzer = PWM(Pin(27))
vol = 1000

# Fonction pour jouer la note SOL pendant un temps donné
def SOL(time):
    buzzer.freq(392)  
    buzzer.duty_u16(vol)
    sleep(time)
    
# Fonction pour jouer la note FA pendant un temps donné
def FA(time):
    buzzer.freq(349)  
    buzzer.duty_u16(vol)
    sleep(time)
    
# Fonction pour jouer la note MI pendant un temps donné
def MI(time):
    buzzer.freq(329)  
    buzzer.duty_u16(vol)
    sleep(time)
    
# Fonction pour jouer la note RE pendant un temps donné
def RE(time):
    buzzer.freq(294)  
    buzzer.duty_u16(vol)
    sleep(time)

# Fonction pour arrêter la sortie du buzzer pendant un temps donné
def N(time):
    buzzer.duty_u16(0)  
    sleep(time)

# Boucle infinie pour jouer les qutre premières mesures
while True:
    
    # Jouer les quatre premières mesures de la chanson
    G(0.25)
    N(0.01)
    G(0.25)
    N(0.01)
    F(0.25)
    N(0.01)
    F(0.25)
    N(0.01)
    E(0.25)
    N(0.01)
    E(0.25)
    N(0.01)
    D(0.5)
    N(0.01)
