import json
from objscrapper import ObjectScrapper

import tkinter as tk
from tkinter import StringVar, ttk


URL = "https://statusinvest.com.br/fundos-imobiliarios/recr11"

def main():

    scrape = ObjectScrapper()

    scrape.scrape(URL)

def __load_json():
    FILE = 'teste.json'
    file = open(FILE, 'w') 
    return json.loads(file)


def open_gui():
    root = tk.Tk()

    root.geometry("640x420")
    root.title("Assets control")
    root.resizable(False, False)

    lf = tk.LabelFrame(root, text='Assets')

    

    root.mainloop()


if __name__ == "__main__":
    main()