# Network

## Introduction

## Répertoire de programme lié au Network

  ==> [Meteo_Heure_Date.py](Meteo_Heure_Date.py) est un programme qui se connecte au wifi pour afficher l'heure et la date ainsi que la méteo du lieu choissi.
  
  
  
## Fonctionnement

Le programme utilise la connectivité Wi-Fi pour se connecter à un réseau spécifié à l'aide des informations de connexion fournies. Une fois connecté, le programme utilise le protocole NTP pour synchroniser l'horloge interne du microcontrôleur avec.

L'écran LCD 1602, connecté au Raspberry Pi Pico via le bus I2C, est utilisé comme afficheur. Il affiche la date et l'heure locales obtenues à partir de l'horloge interne du microcontrôleur.

De plus, le programme intègre l'API OpenWeatherMap, qui fournit des données météorologiques en temps réel. Les informations météorologiques, telles que la température en degrés Celsius et l'humidité en pourcentage, sont extraites de la réponse JSON de l'API. Ces données sont ensuite affichées sur l'écran LCD, permettant à  de suivre les conditions météorologiques actuelles de la ville souhaité.

Le programme se met à jour toutes les 3 secondes. Cela permet d'afficher en continu les dernières informations météorologiques sur l'écran LCD, 

Une explication détaillée se trouve directement dans le code de chaque programme.

#### Démonstration [Meteo_Heure_Date.py](Meteo_Heure_Date.py)

![IMG_3716](https://user-images.githubusercontent.com/125505805/236703665-6928a439-93ed-411d-9475-ea9b245c757f.gif)


## Description des fonctions utilisées

### - Read_u16()

La fonction read_u16() permet de 


