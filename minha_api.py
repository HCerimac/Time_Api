import tkinter as tk
from tkinter import scrolledtext

# Dados dos times
times = [
    {"nome": "Santos", "titulos": 3, "anos": [1962, 1963, 2011]},
    {"nome": "São Paulo", "titulos": 3, "anos": [1992, 1993, 2005]},
    {"nome": "Palmeiras", "titulos": 2, "anos": [1999, 2020]},
    {"nome": "Grêmio", "titulos": 3, "anos": [1983, 1995, 2017]},
    {"nome": "Internacional", "titulos": 2, "anos": [2006, 2010]},
    {"nome": "Flamengo", "titulos": 2, "anos": [1981, 2019]},
    {"nome": "Cruzeiro", "titulos": 2, "anos": [1976, 1997]},
    {"nome": "Corinthians", "titulos": 1, "anos": [2012]},
]

def exibir_times():
    root = tk.Tk()
    root.title("Lista de Times")

    text_area = scrolledtext.ScrolledText(root, width=80, height=40, wrap=tk.WORD)
    text_area.pack(padx=10, pady=10)

    for time in times:
        nome = time['nome']
        titulos = time['titulos']
        anos = ', '.join(map(str, time['anos']))
        text_area.insert(tk.END, f"{nome} - {titulos} título(s) ({anos})\n\n")

    root.mainloop()

exibir_times()
