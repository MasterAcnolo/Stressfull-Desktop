import tkinter as tk
from tkinter import ttk
from random import choice, uniform
import pygame
import sys

# Initialisation de pygame pour la musique
pygame.mixer.init()
pygame.mixer.music.load("song.mp3")  # Charger la musique mais ne pas la jouer immédiatement

# Liste de messages à afficher dans les fenêtres pop-up
messages = [
    "Erreur inconnue. Relancer votre PC",
    "Mise à jour Critique: Redémarrage dans 5 min",
    "Kernel System Error",
    "Votre Ordinateur va exploser",
    "Votre Carte Graphique est à +200°C, Vous pouvez y griller un oeuf si vous le désirez",
    "Le fond d'écran est trop pixelisé, votre ordinateur ne peut plus le supporter.",
    "Votre ordinateur a décidé de faire une pause. Retour dans 10 minutes.",
    "Le système d'exploitation a pris une sieste imprévu... Redémarrage dans 3… 2… 1…",
    "Vous êtes sur le point de devenir une légende... dans la file d'attente pour un support technique.",
    "Votre ordinateur a demandé à prendre des vacances. Il reviendra après un redémarrage.",
    "Qui lit ça?"
]

# Liste pour garder une trace des fenêtres ouvertes
windows = []

# Variable globale pour vérifier si la musique est en cours de lecture
is_music_playing = False

# Fonction pour créer une fenêtre pop-up avec un message aléatoire
def spawn_window():
    """Création des fenêtres pop-up avec les messages."""
    window = tk.Toplevel(main_window)  # Créer la fenêtre pop-up indépendamment de main_window
    windows.append(window)  # Ajouter la nouvelle fenêtre à la liste
    message = choice(messages)
    
    width = 300
    height = 150
    window.geometry(f"{width}x{height}+{choice(range(100, 800))}+{choice(range(100, 500))}")

    label = tk.Label(window, text=message, fg='red', font=("Helvetica", 12), wraplength=width-20)
    label.pack(pady=10)

    progress = ttk.Progressbar(window, orient="horizontal", length=250, mode="indeterminate")
    progress.pack(pady=5)
    progress.start(25)

    window.update_idletasks()  
    window.geometry(f"{max(width, label.winfo_width()+20)}x{max(height, label.winfo_height()+40)}")

    window.after(10000, window.destroy)  # Ferme la fenêtre après 10 secondes

    # Appel de spawn_window à intervalles réguliers
    window.after(1, spawn_window)  # Créer une nouvelle fenêtre après 500ms

# Fonction pour fermer toutes les fenêtres ouvertes et arrêter la musique
def close_all_windows():
    """Fermer toutes les fenêtres ouvertes et arrêter la musique si toutes les fenêtres sont fermées."""
    global is_music_playing  # Déclarer global ici pour pouvoir modifier la variable
    for window in windows:
        window.destroy()
    windows.clear()  # Vider la liste des fenêtres

    # Si toutes les fenêtres sont fermées et que la musique est en cours, l'arrêter
    if is_music_playing:
        pygame.mixer.music.stop()  # Arrêter la musique
        is_music_playing = False

# Fonction pour démarrer le script des fenêtres
def start_script():
    """Démarre le script des fenêtres."""
    global is_music_playing  # Déclarer global ici pour pouvoir modifier la variable
    if not is_music_playing:  # Si la musique n'est pas encore en cours, la démarrer
        pygame.mixer.music.play(loops=-1)  # Démarrer la musique lorsque le script commence
        is_music_playing = True

    spawn_window()  # Lance le script et crée les fenêtres pop-up

# Fonction pour fermer le programme lorsque la fenêtre principale est fermée
def on_main_window_close():
    """Ferme tout si la fenêtre principale est fermée."""
    print("Fenêtre principale fermée. Arrêt du programme.")
    close_all_windows()  # Fermer toutes les fenêtres et arrêter la musique
    sys.exit()  # Quitter le programme

# Fenêtre principale (avant le lancement du script)
main_window = tk.Tk()
main_window.title("Contrôle du Script")

# Lier la fermeture de la fenêtre principale pour arrêter tout
main_window.protocol("WM_DELETE_WINDOW", on_main_window_close)

# Bouton pour démarrer le script
start_button = tk.Button(main_window, text="Lancer le script", command=start_script)
start_button.pack(pady=20)

# Ouvrir la fenêtre principale
main_window.mainloop()
