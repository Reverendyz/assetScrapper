
import json
from objscrapper import ObjectScrapper

import tkinter as tk
from tkinter import StringVar, ttk


URL = [
    "https://statusinvest.com.br/fundos-imobiliarios/rztr11",
    "https://statusinvest.com.br/fundos-imobiliarios/tord11",
    "https://statusinvest.com.br/fundos-imobiliarios/hctr11",
    "https://statusinvest.com.br/fundos-imobiliarios/vilg11",
    "https://statusinvest.com.br/fundos-imobiliarios/vghf11",
    "https://statusinvest.com.br/fundos-imobiliarios/recr11",
    "https://statusinvest.com.br/fundos-imobiliarios/mxrf11",
    "https://statusinvest.com.br/fundos-imobiliarios/rectas11"
    ]

def main():
    scrape = ObjectScrapper()
    scrape.scrape(URL)

def read_assets():
    try:
        with open('teste.json', 'r') as json_file:
            print(json.load(json_file))
    except:
        raise FileNotFoundError

if __name__ == "__main__":
    while(True):
        main()
        option = input('Do you like to list the assets in it? (y/n): ')
        if option == 'y':
            read_assets()
        var = input('Would you like to continue? (y/n): ')
        if var == 'n':
            break