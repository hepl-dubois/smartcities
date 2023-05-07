import network
import ntptime
import urequests
from lcd1602 import LCD1602 
from machine import I2C, Pin
from utime import sleep, localtime

# Informations de connexion Wi-Fi
ssid = 'WiFi-2.4-CC40' # Mettre votre nom de WiFi ici
password = 'XXXXXXXXX' # Mettre votre code WiFi ici

# Connexion au Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while not wlan.isconnected():
    pass

# Récupérer la date et l'heure à partir du serveur NTP
ntptime.settime()

# Définir l'URL de l'API OpenWeatherMap
api_key = '410656043e3645883d3e6ba29b0f9cba' # Mettre votre clé d'api ici
ville = 'Namur' # Mettre votre ville ici
pays = 'BE' # Mettre le pays ici
url = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}'.format(ville, pays, api_key)

#Récupération les données météorologiques via l'API OpenWeatherMap
def get_weather_data():
    try:
        response = urequests.get(url)
        data = response.json()
        return data
    except:
        return None

# Initialisation de l'écran LCD1602
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
lcd = LCD1602(i2c, 2, 16)

# Boucle de mise à jour en 3 partie
while True:
    
#########################################Partie 1 qui affiche le Pays et la Ville sélectionné##########################################################################################################
    
    # Effacer l'écran LCD
    lcd.clear()
    
    # Afficher le Pays choissis
    lcd.print("Pays: {}".format(pays))
    
    # Déplacer le curseur sur la deuxième ligne
    lcd.setCursor(0, 1)
    
    # Afficher la Ville choissie
    lcd.print("Ville: {}".format(ville))
    
    # Pause de 2,5 secondes avant de passé a l'étape suivante
    sleep(2.5)
    
#########################################Partie 2 qui affiche l'heure GTM+2#################################################################################################################
    
    # Obtenir l'heure locale
    current_time = localtime()

    # Ajouter 2 heures à l'heure locale
    adjusted_hour = (current_time[3] + 2) % 24

    # Effacer l'écran LCD
    lcd.clear()

    # Afficher la date
    lcd.print("Date: {:02d}-{:02d}-{:02d}".format(current_time[2], current_time[1], current_time[0]))

    # Déplacer le curseur sur la deuxième ligne
    lcd.setCursor(0, 1)

    # Afficher l'heure ajustée
    lcd.print("Heure: {:02d}:{:02d}:{:02d}".format(adjusted_hour, current_time[4], current_time[5]))

    # Pause de 2,5 secondes avant de passé a l'étape suivante
    sleep(2.5)
    
#########################################Partie 3 qui affiche la météo de la Ville sélectionné############################################################################################################
    
    # Récupérer les données météorologiques
    weather_data = get_weather_data()

    if weather_data:
        
        # Extraire les informations de la météo
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']

        # Effacer l'écran LCD
        lcd.clear()
        
        # Afficher les informations de la météo sur l'écran LCD
        lcd.print("Temp: {:.1f}".format(temperature - 273.15))
        
        # Afficher le symbole "°"
        lcd.write(0b11011111) 
        
        # Afficher le "C"
        lcd.print("C") 
        
        # Déplacer le curseur sur la deuxième ligne
        lcd.setCursor(0, 1)
        
        # Afficher l'humidité en %
        lcd.print("humidite: {}%".format(humidity))

        # Pause de 2,5 secondes avant de passé a l'étape suivante
        sleep(2.5)

