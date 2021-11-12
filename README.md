# Présentation

Projet EpheCom

Ce logiciel a été développé dans le cadre scolaire.
EpheCom est un logiciel de communications - vocale et écrite - en temps réel.
Il a pour but d'améliorer la communication au sein de l'établissement scolaire.

Version de Python : 3.9

Système d'exploitation : Windows, OSX, Linux

Type : Application de bureau

Langue utilisée pour coder : Anglais

Langue utilisée pour documenter : Français 

Base de données utlisée : MongoDB Atlas https://www.mongodb.com/fr-fr/cloud/atlas
(Vous devrez demander votre certificat d'authentification temporaire à votre professeur)

Documentation Framework : https://kivy.org/doc/stable/api-kivy.html

Source unique des icons : https://remixicon.com/

Convention de nommage :
    https://www.python.org/dev/peps/pep-0008/


# Déroulement

Chaque groupe de projet (4/groupe) se verra assigné un module.

Vous devrez créer un repository github pour votre module. Dans celui-ci devra se trouver :
- Le code source,
- La documentation technique,
- La documentation sur la manière d'installer et utiliser votre module,
- La documentation demandé par les enseignants.

Lors des deux dernières semaines du quadrimeste, il vous sera demandé d'adapter le projet noyau afin d'y intégrer votre module.
Évidemment, si vous vous sentez prêt plus tôt, n'hésitez pas à l'intégrer directement.

## Planning

Voici un tableau représentant les étapes et deadlines :

| Tâche | Description | Deadline
|---|---|---
| Description du MVP | Vous devez décrire, en quelques lignes, ce a quoi ressemblera votre module dans une version minimaliste | [ S5 ] 
| Cahier des charges | Vous définirez un cahier des charges complet de votre module. | [ S6 ]
| Implémentation du MVP | C'est qu'à cette étape que les premières lignes de code sont implémentées. Nous devons comprendre via un projet minimaliste le but de votre module. Cela doit se faire en ligne de commandes. | [ S8 ]
| Diagrammes et schémas d'architecture | Mise en place du diagramme UML et du schéma d'architecture en fonction de la description de votre module dans votre cahier des charges. Cela implique ce celui-ci soit le plus complet possible. | [ S9 ]
| Implémentaiton complète | Toutes les fonctionnalités décrites dans votre cahier des charges seront implémentées | [ S10 - Sx ]
| Validation | Vous démontrez, via des tests unitaires ou tout autre tests, la fiabilité de votre code. | [ S11 ]
| Finalisation | Le module doit être inclu dans le projet noyau | [ S10 - Sx]

# Outils

Vous devrez maîtriser et utiliser les outils listés ci-dessous afin de vous organiser au mieux.
- Git/Github - https://github.com/
- [Github Project]
- Pycharm (License éducative) - https://www.jetbrains.com/fr-fr/pycharm/
- Python 3.8+ - https://www.python.org/downloads/
- Environnements virtuels - https://docs.python.org/3/library/venv.html
- [ Clockify ] - https://clockify.me/

# Modules

## Système de discussion

### L'utilisateur doit pouvoir communiquer par écrit avec une ou plusieurs personnes.

    - Possibilité de discuter avec un seul membre (conversation privée)
    - Possibilité de créer une groupe de discussion.
    - Le créateur peut ajouter/supprimer des participants.
    - Les messages écrits doivent être traçables.
    - Les messages doivent être en temps réel si les deux utilisateurs ou plus sont connectés en même temps.
    - Les discussions doivent revenir au dernier état après reconnexion.
    - [ Possibilité d'envoyer des documents, images, etc. dans une discussion ]
    
## Système de vidéo-conférence en temps réel
    - Possibilité de communiquer oralement et par vidéo avec un ou plusieurs participants.
    - Un bouton permet d'enregistrer les communications.
    - Un bouton permet de cacher l'entrée vidéo d'un utilisateur.
    - [ Partage d'écran ]

## Système de boutons interactionnels
    - Possibilité de lever la main pendant une vidéo conférence.
    - Possibilité de prendre une capture d'écran instantanée enregistrée sur le pc.
    - Possibilité d'envoyer des documents, images, etc. dans une discussion à deux ou groupée.


## Gestionnaire d'utilisateurs
    - Inscription
    - Connexion
    - Gestion de rôles utilisateurs lié au logiciel (Administrateur | utilisateur | visiteur).
    - Gestion de rôles utilisateurs lié aux discussions groupées (Admin d'un groupe, etc.)
    - Les droits des utilisateurs peuvent être modifiés par un administrateur.
    - Interface d'administration pour les administrateurs du logiciel.


## Bot permettant l'accès à diverses nouvelles (Météo, news, etc.)
    - Messages automatisés pour un channel grâce à des commandes spécifiques.
    - Automatiser les informations en liant le bot à des news qui sont régulièrement affichées dans les groupes concernés.


## Bot aidant dans la gestion de EpheCom
    - Statut du réseau
    - Statistiques sur différents critères comme : Nombre d'utilisateurs, de groupes etc.
    - Graphiques représentant l'évolution des inscriptions, quantités d'inscrits, quantité de messages envoyés, etc.
    - Ajout/Suppression de rôles.
    - Ajout de team, groupes et channels de manière automatisée.
    - Ajout automatique dans des groupes grâce à des commandes spécifiques.

# Challenges

- Si je souhaites changer la couleur principale du projet, ou dois-je faire ma modification ?
- Quid d'un code pas optimal ?
- 

# Attention !

Lors de votre implémentation, il vous est demandé de suivre à la lettre les bonnes pratiques de programmation.

C'est-à-dire :
- Votre code doit être documenté/commenté,
- Vous suivez la PEP08 !,
- Vos noms de variables, fonction, classes etc. sont significatifs,
- Vous travaillerez de manière agile, cela signifie que vous DEVEZ vous diviser les tâches de manière organisée, triées par priorités et grâce aux outils ci-dessus.