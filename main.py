
import argparse
from objscrapper import ObjectScrapper

def main():
    parser = argparse.ArgumentParser(description="Take assets inside StatusInvest and outputs inside a json file where is located")
    parser.add_argument("-a","--assets", nargs="+" ,type=str, metavar="asset_list", help="One or many assets to scrape", required=True)

    args = parser.parse_args()

    scraper = ObjectScrapper()
    scraper.scrape(args.assets)

if __name__ == "__main__":
    main()