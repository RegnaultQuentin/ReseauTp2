# TP 2 - Exploration du réseau d'un point de vue client


## I. Exploration locale en solo
### 1. Affichage d'informations sur la pile TCP/IP locale
#### En ligne de commande
##### Affichez les infos des cartes réseau de votre PC
    Le nom, l'adresse MAC et l'adresse IP de l'interface WiFi:
         Nom: Carte réseau sans fil WiFi
         Adresse MAC: F8-34-41-F8-18-2B
         Adresse Ip:10.33.255.255
    Le nom, l'adresse MAC et l'adresse IP de l'interface Ethernet
        Nom: Carte Ethernet Ethernet
        Pour le reste je ne sais pas je ne suis pas connecté avec elle.
    Déterminer, l'adresse de réseau et l'adresse de broadcast: 
        Adresse réseau: 10.33.0.0
        Adresse de broadcast: 10.33.255.255
##### Affichez votre gateway
Avec la commande précédente (ipconfig /all) on peut voir l'adresse gateway sous le nom de "passerelle par défault" elle est égal à 10.33.3.253
#### En graphique (GUI : Graphical User Interface)
##### Trouvez comment afficher les informations sur une carte IP (change selon l'OS)
Sur windows on peut retrouver les informations dans l'onglet "Centre réseau et partage" de l'onglet "Réseau et internet" du panneau de configuration. 
#### Questions, à quoi sert la gateway dans le réseau d'Ingésup ?
La paserelle d'ingésup sert à connecter le réseau local au réseau internet et il utilise potentiellement des par feu ou/et des proxis
### 2. Modifications des informations
#### A. Modification d'adresse IP - pt. 1
##### Calculez la première et la dernière IP disponibles du réseau 
La première adresse est 10.33.0.1 et la dernière est 10.33.255.252
##### Changez l'adresse IP de votre carte WiFi pour une autre
C'est ici que l'on change une ip sous windows
![](https://github.com/RegnaultQuentin/ReseauTp2/blob/master/changementipwindows.png?raw=true)
#### B. nmap
Avec l'utilisation de la commande donné dans l'énnoncé on obtient toutes les ip utilisés 
![](https://github.com/RegnaultQuentin/ReseauTp2/blob/master/resultatnmap.png?raw=true)

Ensuite on change l'Ip pour en prendre une disponnible et pouvoir aller sur internet 

## II. Exploration locale en duo

### Modification d'adresse IP

Pour modifier l'adresse IP d'une machine sur Windows, il faut aller dans les paramètres réseaux, centre réseaux et partage, puis changer son IPV4 en plaçant les 2 machines sous le meme masque pour qu'elles communiquent entre elles.
    
### Utilisation d'un des deux comme gateway
    
Pour cela, a l'aide d'un cable RJ45, nous allons permettre à la machine qui a desactivé la connexion de pouvoir acceder a internet en passant par la connexion de l'autre machine.
    
### Petit chat privé ?

De même, nous allons utiliser netcat pour permettre aux 2 machines de communiquer entre elles.

Le pc serveur qui fera office de serveur rentrera la commande suivante :

    nc.exe -l -p 8888

Le pc qui fera office de client rentrera la commande :
    
    nc.exe "adresse ip de la machine serveur" 8888

![](https://github.com/RegnaultQuentin/ReseauTp2/blob/master/chat%20incroyable.jpg?raw=true)
    
    
###  Wireshark

Nous allons utiliser l'outil wireshark qui permet d'observer la trame qui circule entre les 2 cartes ethernet,
    
Pendant un ping:

![](https://github.com/antoine33520/CCNA/blob/master/TP2/wireshark_ping.png?raw=true)

Pendant l'utilisation de netcat:

![](https://github.com/RegnaultQuentin/ReseauTp2/blob/master/wireshark_ncat.png?raw=true)


Pendant que le PC1 sert du PC2 comme gateway:

![](https://github.com/RegnaultQuentin/ReseauTp2/blob/master/wireshark_sans_filtrage.png?raw=true)
    
### Firewall

Nous allons faire fonctionner notre Firewall pour permettre de, à la fois l'activer, autoriser le ping et activer le nc sur un port spécifique.

On configure le Firewall pour que l'OS accepte le ping.

![](https://github.com/RegnaultQuentin/ReseauTp2/blob/master/regle_firewall_ping.PNG?raw=true)
    
    
On choisis arbitrairement un port entre 1024 et 20000, afin de communiquer via netcat.

![](https://github.com/RegnaultQuentin/ReseauTp2/blob/master/regle_firewall_netcat.png?raw=true)


## III. Manipulations d'autres outils/protocoles côté client

### DHSP
* Adressse DHCP : 10.33.3.254 
* Bail obtenu : vendredi 4 janvier 2019 12:58:51
* Bail expirant : vendredi 4 janvier 2019 14:58:50

- Fonctionnement DHCP : Un client DHCP (ordinateur) demande une adresse IP à un serveur DHCP. Le client demande ensuite un bail au réseau. Les serveurs DHCP lui propose une adresse IP avec une durée. Le client sélectionne la première adresse IP et demande de l'utilisé. Le serveur DHCP accorde l'adresse et le client peut se connecter au réseau. 

- Pour demander une nouvelle adresse IP : 
    - Ecrire en ligne de commande :
        - ipconfig /release
        - ipconfig /renew

### DNS
* Adresse DNS : 8.8.8.8
* Adresse google.com : 216.58.215.46
* Adresse ynov.com : 217.70.184.38

Après un reverse lookup, on obtient : 

PS C:\Users> nslookup 78.78.21.21
* Serveur :   UnKnown
* Address:  10.33.10.20

* Nom :    host-78-78-21-21.mobileonline.telia.com
* Address:  78.78.21.21

PS C:\Users> nslookup 92.16.54.88
* Serveur :   UnKnown
* Address:  10.33.10.20

* Nom :    host-92-16-54-88.as13285.net
* Address:  92.16.54.88


