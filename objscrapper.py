from cgitb import text
import json
from bs4 import BeautifulSoup as bs
import requests

class ObjectScrapper:
    def __init__(self):
        pass

    def scrape(self, link_to_scrape):
        if type(link_to_scrape) == list:
            return
        else:    
            if link_to_scrape == '':
                return
            r = requests.get(link_to_scrape)

            soup = bs(r.content, 'html.parser')

            with open("teste.json", "w") as f:
                assets = soup.find_all('b', class_="sub-value")
                asset_name = soup.find("h1", class_="lh-4")
                print(asset_name.text)
                constructor = {
                    "Assets":{

                    }
                }
                stocks = [{
                    f'{asset_name.text.split("-")[0].strip()}': {
                        "Previous": {
                            "Yeld": assets[0].text,
                            "Price": assets[1].text,
                            "BaseDate" : assets[2].text,
                            "PaymentDate": assets[3].text
                        },
                        "Next": {
                            "Yeld": assets[4].text,
                            "Price": assets[5].text,
                            "BaseDate" : assets[6].text,
                            "PaymentDate": assets[7].text
                        }
                    }
                }]
                constructor["Assets"] = stocks
                f.write(json.dumps(constructor, indent=2))
            
            f.close()

        

