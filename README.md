# EZ4ENCE PopUp  

## 📝 Description  

EZ4ENCE PopUp est un projet Python conçu pour afficher des fenêtres pop-up à intervalles réguliers, avec des messages amusants et une barre de chargement infinie. Une musique est également jouée en arrière-plan pour ajouter un effet supplémentaire.  

Ce projet a été créé dans un but purement ludique et éducatif afin d'explorer l'utilisation de **Tkinter**, **Pygame** et la compilation en `.exe`.  

## 🎯 Fonctionnalités  

- ✅ Génération automatique de plusieurs fenêtres pop-up à intervalles très courts (~0.1s).  
- 🎵 Lecture d'une musique en boucle via **Pygame**.  
- ❌ Un bouton "Stop" pour arrêter totalement le programme.  
- 🏴‍☠️ Une version `.exe` pour exécuter l'application sans installation de Python.  

## 🛠️ Outils utilisés  

Ce projet a été développé avec :  

- **Python** 🐍  
- **Tkinter** (pour la gestion des fenêtres)  
- **Pygame** (pour jouer la musique de fond)  
- **PyInstaller** (pour créer un `.exe` portable)  

## 🚀 Installation et Exécution  

### 🔹 1. Exécuter depuis le code source  

Si vous avez Python installé sur votre machine :  

1. **Clonez le dépôt** :  

   ```bash
   git clone https://github.com/ton-github/EZ4ENCE-PopUp.git
   cd EZ4ENCE-PopUp


2. **Installez les dépendances :** : 

    ```bash
    pip install pygame


3. **Lancez le script:** :

    ```bash
    python script.py


## 🚀 2. Exécuter la version `.exe` (Windows)  

### 🔹 Exécuter l'exécutable `.exe`  

Si vous ne voulez pas installer Python, utilisez l'exécutable compilé :  

1. **Téléchargez** `EZ4ENCE.exe` depuis la section **Releases** du dépôt.  
2. **Placez** `EZ4ENCE.exe` et `song.mp3` dans le même dossier.  
3. **Double-cliquez** sur `EZ4ENCE.exe` pour démarrer l’application.  

⚠ **Important** :  
- `song.mp3` **doit être dans le même dossier** que l’exécutable, sinon la musique ne fonctionnera pas.  
- L’antivirus peut détecter le `.exe` comme une menace en raison de la génération automatique de fenêtres. Ajoutez une exception si nécessaire.  

---

### 🔹 Compilation en `.exe`  

Si vous souhaitez compiler vous-même le projet en `.exe`, suivez ces étapes :  

1. **Installez PyInstaller** (si ce n'est pas déjà fait) :  

   ```bash
   pip install pyinstaller

2. **Compilez le script en .exe avec la commande suivante :**:
    
    ```bash
    pyinstaller --onefile --windowed --add-data "song.mp3;." script.py

    ss
