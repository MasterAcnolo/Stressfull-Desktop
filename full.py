import os
import sys
import pygame
from random import choice, uniform
from threading import Timer
import tkinter as tk
from tkinter import ttk

# Pygame ignition
pygame.mixer.init()

# Dynamic gestion of song path
if getattr(sys, 'frozen', False):
    resource_path = os.path.join(sys._MEIPASS, "song.mp3")
else:
    resource_path = "song.mp3"

pygame.mixer.music.load(resource_path)

#Feel Free to modify this type of messages, just follow the way i did it
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

windows = []


popup_timer = None

def spawn_window():
    global popup_timer
    window = tk.Toplevel(main_window)  # Main Layer
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

    windows.append(window)  

    Timer(10, window.destroy).start()  # Change the value with an float number to close window (here it's 10 seconds)

    if popup_timer:  # If timer exist, it will popup another window every 0.1s. You can change this value to any float number. 
        popup_timer = Timer(0.1, spawn_window)
        popup_timer.start()

def start_script():
    global popup_timer
    start_button.config(state=tk.DISABLED)  # Disable "Startup" button
    stop_button.config(state=tk.NORMAL)  # Activate the "Stop" Button
    pygame.mixer.music.play(loops=-1)  # Replay the song if end
    spawn_window()  # Start First window
    popup_timer = Timer(0.3, spawn_window)  # Make another pop up every 0.3s 
    popup_timer.start()

def stop_script():
    global popup_timer
    pygame.mixer.music.stop()  # Stop Music
    close_all_windows()  # Shut every pop up
    start_button.config(state=tk.NORMAL)  # Re activate "Start" Button
    stop_button.config(state=tk.DISABLED)  # Shut the "Stop" Button
    
    if popup_timer:
        popup_timer.cancel()  # Stop the timer 
        popup_timer = None  # Reset the timer

def close_all_windows():
    for window in windows:
        window.destroy()  # Close all pop up
    windows.clear()  # Clear window queue

# Main Window
main_window = tk.Tk()
main_window.title("Stressful Office Simulator")

# Start button
start_button = tk.Button(main_window, text="Démarrer", command=start_script)
start_button.pack(pady=10)

# Stop Button
stop_button = tk.Button(main_window, text="Arrêter", command=stop_script, state=tk.DISABLED)
stop_button.pack(pady=10)

# Start the Tkinter loop
main_window.mainloop()
