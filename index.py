from random import choice, uniform
from threading import Timer
import tkinter as tk
from tkinter import ttk
import pygame

# Initialiser pygame pour la musique
pygame.mixer.init()
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play(loops=-1)

messages = [
    "Erreur inconnue. Relancer votre PC",
    "Mise à jour Critique: Redémarrage dans 5 min",
    "Kernel System Error",
    "Votre Ordinateur va exploser",
    "Votre Carte Graphique est à +200°C, Vous pouvez y griller un oeuf si vous le désirez"
]

def spawn_window():
    window = tk.Toplevel(root)
    window.geometry(f"300x150+{choice(range(100, 800))}+{choice(range(100, 500))}")

    label = tk.Label(window, text=choice(messages), fg='red', font=("Helvetica", 12))
    label.pack(pady=10)

    progress = ttk.Progressbar(window, orient="horizontal", length=250, mode="indeterminate")
    progress.pack(pady=5)
    progress.start(25)

    Timer(3, window.destroy).start()
    Timer(uniform(0.05, 0.2), spawn_window).start()

root = tk.Tk()
root.withdraw()
spawn_window()
root.mainloop()
