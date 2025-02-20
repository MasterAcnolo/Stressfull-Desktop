import os
import sys
import pygame
from random import choice, uniform
from threading import Timer
import tkinter as tk
from tkinter import ttk

# Initialisation de Pygame pour la musique
pygame.mixer.init()

# Gestion dynamique du chemin pour le fichier audio
if getattr(sys, 'frozen', False):
    # Si l'application est gelée dans un .exe, utilise le chemin du répertoire temporaire
    resource_path = os.path.join(sys._MEIPASS, "song.mp3")
else:
    # Si tu es en mode développement, le fichier song.mp3 est au même endroit que le script
    resource_path = "song.mp3"

pygame.mixer.music.load(resource_path)

# Liste des messages à afficher dans les fenêtres pop-up
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

# Liste pour stocker toutes les fenêtres pop-up
windows = []

# Timer pour gérer les pop-up
popup_timer = None

def spawn_window():
    global popup_timer
    window = tk.Toplevel(main_window)  # Utilise la fenêtre principale
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

    windows.append(window)  # Ajouter la fenêtre à la liste pour pouvoir la fermer plus tard

    Timer(10, window.destroy).start()  # Détruire la fenêtre après 10 secondes

    if popup_timer:  # Si le timer existe, relance spawn_window après 0.1 seconde
        popup_timer = Timer(0.1, spawn_window)
        popup_timer.start()

def start_script():
    global popup_timer
    start_button.config(state=tk.DISABLED)  # Désactive le bouton "Démarrer"
    stop_button.config(state=tk.NORMAL)  # Active le bouton "Arrêter"
    pygame.mixer.music.play(loops=-1)  # Redémarre la musique si elle a été arrêtée
    spawn_window()  # Lance la première fenêtre
    popup_timer = Timer(0.3, spawn_window)  # Crée la première fenêtre pop-up avec un délai de 0.1 seconde
    popup_timer.start()

def stop_script():
    global popup_timer
    pygame.mixer.music.stop()  # Arrête la musique
    close_all_windows()  # Ferme toutes les fenêtres pop-up
    start_button.config(state=tk.NORMAL)  # Réactive le bouton "Démarrer"
    stop_button.config(state=tk.DISABLED)  # Désactive le bouton "Arrêter"
    
    if popup_timer:
        popup_timer.cancel()  # Arrête le timer pour la génération de fenêtres pop-up
        popup_timer = None  # Réinitialise le timer

def close_all_windows():
    for window in windows:
        window.destroy()  # Ferme chaque fenêtre pop-up
    windows.clear()  # Vide la liste des fenêtres

# Fenêtre principale
main_window = tk.Tk()
main_window.title("Stressful Office Simulator")

# Bouton Démarrer
start_button = tk.Button(main_window, text="Démarrer", command=start_script)
start_button.pack(pady=10)

# Bouton Arrêter
stop_button = tk.Button(main_window, text="Arrêter", command=stop_script, state=tk.DISABLED)
stop_button.pack(pady=10)

# Lancer la boucle principale de Tkinter
main_window.mainloop()
