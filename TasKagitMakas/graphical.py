import random
import time
import tkinter as tk
from tkinter import messagebox

def play_game(player_choice):
    choices = ['T', 'K', 'M']
    computer_choice = random.choice(choices)

    result = determine_winner(player_choice, computer_choice)

    result_label.config(text="Bilgisayar: " + computer_choice + "\nSonuç: " + result)
    
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Berabere"
    elif (player_choice == "T" and computer_choice == "M") or (player_choice == "K" and computer_choice == "T") or (player_choice == "M" and computer_choice == "K"):
        return "Kazandınız!"
    else:
        return "Kaybettiniz!"

def on_exit():
    if messagebox.askyesno("Çıkış", "Oyundan çıkmak istediğinize emin misiniz?"):
        root.destroy()

def countdown(seconds):
    tkm = ["TAŞ...", "KAĞIT...", "MAKAS..."]
    
    for i in range(0, 3):
        countdown_label.config(text=tkm[i])
        root.update()
        time.sleep(1)
    countdown_label.config(text="")
    play_game(player_choice_var.get())

root = tk.Tk()
root.title("Taş Kağıt Makas Oyunu")

player_choice_var = tk.StringVar()

button_frame = tk.Frame(root)
button_frame.pack()

taş_button = tk.Button(button_frame, text="Taş", command=lambda: start_countdown("T"))
taş_button.pack(side=tk.LEFT, padx=10)

kağıt_button = tk.Button(button_frame, text="Kağıt", command=lambda: start_countdown("K"))
kağıt_button.pack(side=tk.LEFT, padx=10)

makas_button = tk.Button(button_frame, text="Makas", command=lambda: start_countdown("M"))
makas_button.pack(side=tk.LEFT, padx=10)

countdown_label = tk.Label(root, text="", font=("Helvetica", 16))
countdown_label.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack()

exit_button = tk.Button(root, text="Çıkış", command=on_exit)
exit_button.pack()

root.protocol("WM_DELETE_WINDOW", on_exit)

def start_countdown(choice):
    countdown(3)  # 3 saniye geri sayım yapacak

root.mainloop()
