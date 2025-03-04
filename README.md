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
   git clone https://github.com/MasterAcnolo/Stressfull-Desktop
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
    ```

    **Explication des options utilisés:**

- `--onefile` : genère un seul fichier `.exe` au lieu de plusieurs fichiers
- `--windowed` : Cache la console pour un affichage propre.
- `--add-data "song.mp3;.` : Ajoute le fichier audio dans l’exécutable pour éviter les erreurs.

3. **Récupérez l’exécutable : Une fois la compilation terminée, l’exécutable sera disponible dans le dossier `dist/`**

### 🔹 Remarque:

- Ce projet a été réalisé pour le fun et l'apprentissage.
- Ne pas utiliser à des fins malveillantes.
- Si vous avez des questions ou suggestions, n’hésitez pas à contribuer ! 🚀

## ⚖️ Conditions légales

Ce projet utilise la musique de **EZ4ENCE** dans le cadre de son fonctionnement. Veuillez respecter les droits d'auteur et les conditions d'utilisation liées à cette musique. Vous devez vous assurer que vous avez l'autorisation appropriée pour utiliser cette musique dans vos projets, notamment si vous prévoyez de distribuer ou de commercialiser l'application.

La musique utilisée dans ce projet est **[EZ4ENCE](https://open.spotify.com/intl-fr/track/4qHdhSUkmDh6r7Ea4NzAvM)**. Vous pouvez écouter la chanson sur Spotify à partir du lien ci-dessus.

### Avertissement
L'utilisation de la musique **EZ4ENCE** dans ce projet ne constitue pas un accord commercial ou une licence de la part de **EZ4ENCE**. Veuillez consulter les licences et les conditions d'utilisation avant d'utiliser cette musique à des fins autres que celles spécifiées dans ce projet.

