from machine import Pin, PWM  # Importation des bibliothèques "PWM" et "Pin" de la bibliothèque "machine"
from time import sleep  # importation de la fonction "sleep" de la bibliothèque "time"

buzzer = PWM(Pin(27))  # initialisation du broche 27 en tant que PWM pour le buzzer

# boucle infinie
while True:
    buzzer.freq(1046) # émission du son DO
    buzzer.duty_u16(1000)  # modulation de l'intensité du son
    sleep(1)   # pause de 1 seconde
    buzzer.freq(1175) # émission du son RE
    buzzer.duty_u16(1000) # modulation de l'intensité du son
    sleep(1)        # pause de 1 seconde
    buzzer.freq(1318) # émission du son MI
    buzzer.duty_u16(1000) # modulation de l'intensité du son
    sleep(1) # pause de 1 seconde
    buzzer.freq(1397) # émission du son FA
    buzzer.duty_u16(1000) # modulation de l'intensité du son
    sleep(1) # pause de 1 seconde
    buzzer.freq(1568) # émission du son SO
    buzzer.duty_u16(1000) # modulation de l'intensité du son
    sleep(1)    # pause de 1 seconde
    buzzer.freq(1760) # émission du son LA
    buzzer.duty_u16(1000)   # modulation de l'intensité du son
    sleep(1)  # pause de 1 seconde
    buzzer.freq(1967) # émission du son SI
    buzzer.duty_u16(1000) # modulation de l'intensité du son
    sleep(1) # pause de 1 seconde
