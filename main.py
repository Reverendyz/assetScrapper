
from objscrapper import ObjectScrapper

import tkinter as tk
from tkinter import StringVar, ttk


URL = ["https://statusinvest.com.br/fundos-imobiliarios/rztr11", "https://statusinvest.com.br/fundos-imobiliarios/tord11"]

def main():

    scrape = ObjectScrapper()

    scrape.scrape(URL)


def open_gui():
    root = tk.Tk()

    root.geometry("640x420")
    root.title("Assets control")
    root.resizable(False, False)

    lf = tk.LabelFrame(root, text='Assets')

    

    root.mainloop()


if __name__ == "__main__":
    main()