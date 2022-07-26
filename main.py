from objscrapper import ObjectScrapper

URL = "https://statusinvest.com.br/fundos-imobiliarios/recr11"

def main():

    scrape = ObjectScrapper()

    scrape.scrape(URL)


if __name__ == "__main__":
    main()