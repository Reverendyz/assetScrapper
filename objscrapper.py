import json
from bs4 import BeautifulSoup as bs
import requests


class ObjectScrapper:
    def __init__(self):
        self.filename = 'teste.json'
        pass

    def scrape(self, link_to_scrape):
        if type(link_to_scrape) == list:
            return
        else:    
            if link_to_scrape == '':
                return
            r = requests.get(link_to_scrape)

            soup = bs(r.content, 'html.parser')
            
            with open(self.filename, "w") as f:
                value = soup.find_all('strong', class_="fs-5")
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
                            "Value": value[0].text,
                            "Yeld": assets[0].text,
                            "Price": assets[1].text,
                            "BaseDate" : assets[2].text,
                            "PaymentDate": assets[3].text
                        },
                        "Next": {
                            "Value": value[1].text,
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

        

