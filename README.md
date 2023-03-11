# Projet Smartcities

Dans le cadre du cours de MicroPython de [Mr. Camus](https://github.com/hepl-camus) & du projet "SmartCorridor" voici le Github de Dubois Antoine, élève de passerelle en ingénieur industriel - Orientation électronique - Option système embarqués à l'HEPL.

Nous travaillons ici sur le RPi Pico W qui est une carte de développement de petite taille qui est conçue pour faciliter la création de projets électroniques et informatiques. Elle est basée sur le microcontrôleur RP2040 de Raspberry Pi et intègre une connectivité sans fil Wi-Fi et Bluetooth.

Le RP2040 est un microcontrôleur à double cœur basé sur l'architecture ARM Cortex-M0+, qui offre une puissance de traitement suffisante pour des applications telles que l'IoT, la robotique, l'automatisation et les systèmes embarqués. La carte dispose de 264 Ko de mémoire flash pour le stockage de programmes et de données, ainsi que de 26 Ko de mémoire vive (RAM) pour le traitement des données.

La carte Raspberry Pi Pico W est équipée d'un connecteur GPIO de 40 broches (voir photo ci-dessous), qui permet de connecter facilement des capteurs, des moteurs et d'autres composants électroniques. Elle dispose également de plusieurs interfaces, notamment des ports USB, des interfaces UART, SPI et I2C.

Le Wi-Fi et le Bluetooth intégrés permettent à la carte de se connecter à d'autres appareils sans fil, tels que des ordinateurs, des smartphones et des tablettes. Cette connectivité sans fil facilite la communication entre différents appareils et peut être utilisée pour la transmission de données, la commande à distance et la surveillance.

![RPi_Pico_W](https://user-images.githubusercontent.com/125505805/220986057-d315d175-f1a6-40c2-9e81-835da921c5e4.png)

Les travaux d'école que j'effectue sont réalisés à l'aide du pack "Groove Starter Kit" pour Raspberry Pi Pico. Ce kit contient tous les composants nécessaires pour créer différents projets électroniques, tels que des capteurs de température, des écrans LCD et des modules de communication. Avec ce kit, je peux facilement apprendre à utiliser le microcontrôleur Raspberry Pi Pico et à créer des projets électroniques amusants et éducatifs pour mes cours.

![image](https://user-images.githubusercontent.com/125505805/224513038-80169a9b-650f-497e-b9b0-5ce23e3e218f.png)

Pour faciliter la création de mes programmes, j'utilise l'IDE "Thonny" qui offre une interface claire et simple à comprendre, ainsi que des outils de débogage pour m'aider à corriger les erreurs dans mon code.

Pour installer Thonny, vous pouvez télécharger le logiciel sur le site officiel de Thonny (https://thonny.org/). Une fois le fichier téléchargé, il vous suffit de l'installer sur votre ordinateur en suivant les instructions à l'écran. Cela ne prendra que quelques minutes. Après l'installation, vous pouvez commencer à utiliser Thonny pour développer vos programmes en micro-python sur le Raspberry Pi Pico.

Il est important de noter que pour utiliser toutes les fonctionnalités du "kit Grove", vous devrez ajouter les bibliothèques nécessaires à votre code. Vous pouvez trouver les bibliothèques [ICI](pico-micropython-grove-master.zip). Ces bibliothèques vous permettront d'accéder à toutes les fonctionnalités du kit Grove et de faciliter la création de vos programmes.

Si vous êtes intéressé(e), vous pouvez trouver tous mes rapports sur ces travaux ici. Ces rapports détaillent les étapes de chaque projet, les difficultés rencontrées et les résultats obtenus. N'hésitez pas à les consulter si vous souhaitez en savoir plus sur mes travaux d'école.

Chaque répertoire contiendra un fichier
descriptif README.md et les ressources liées aux sujetx traités : code, datasheets, photos,
explications diverses...

Cependant vous trouverez directement toute les ressources, code, explication dans le PDF de SeedStudio pour Groove Kit [ICI](https://files.seeedstudio.com/wiki/Grove_Shield_for_Pi_Pico_V1.0/Begiinner's-Guide-for-Raspberry-Pi-Pico.pdf)

## Répertoire :

- [GPIO](GPIO) : LED simple, bouton-poussoir, interruption.
- [AD-PWM](AD-PWM) : lecture du potentiomètre, PWM (LED, musique, servo).
- [LCD](LCD) : documentation des fonctions de la librairie, affichage de la valeur du potentiomètre.
- [LED_neo](LED_neo) : utilisation des LEDs néopixel, documentation des fonctions de la librairie, arc-en-ciel.
- [sensors](sensors) : température et humidité, luminosité, PIR.
- [network](network) : Accès réseau avec le RPi Pico.



