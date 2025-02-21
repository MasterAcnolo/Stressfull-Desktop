from random import choice, uniform
from threading import Timer
import tkinter as tk
from tkinter import ttk
import pygame

pygame.mixer.init()
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play(loops=-1)

messages = [
    "Erreur inconnue. Relancer votre PC",
    "Mise à jour Critique: Redémarrage dans 5 min",
    "Kernel System Error",
    "Votre Ordinateur va exploser",
    "Votre Carte Graphique est à +200°C, Vous pouvez y griller un oeuf si vous le désirez"
    "Le fond d'écran est trop pixelisé, votre ordinateur ne peut plus le supporter."
    "Votre ordinateur a décidé de faire une pause. Retour dans 10 minutes."
    "Le système d'exploitation a pris une sieste imprévu... Redémarrage dans 3… 2… 1…"
    "Vous êtes sur le point de devenir une légende... dans la file d'attente pour un support technique."
    "Votre ordinateur a demandé à prendre des vacances. Il reviendra après un redémarrage."
    "Qui lit ça?"
]

def spawn_window():
    window = tk.Toplevel(root)
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

    #Timer(10, window.destroy).start() <----- Pour que les fenêtres se ferment Xs après ouverture
    Timer(uniform(0.05, 0.2), spawn_window).start()

root = tk.Tk()
root.withdraw()
spawn_window()
root.mainloop()
