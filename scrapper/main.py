import json
from typing import Optional
from bs4 import BeautifulSoup
import requests
import re
import argparse


class ObjectScrapper:
	def __init__(self) -> None:
		pass

	def __checkurl(self, asset: str):
		r = requests.get(f"https://statusinvest.com.br/fundos-imobiliarios/{asset}")

		links = re.findall(r"link.href.*\b", r.text)

		for link in links:
			if(link.__contains__("error")):
				raise Exception(f"This asset '{asset}' was not found in Statusinvest/fundos-imobiliarios")

	def __get_data(self, asset: str):
		r = requests.get(f"https://statusinvest.com.br/fundos-imobiliarios/{asset}")
		soup = BeautifulSoup(r.text, "html.parser")

		div = soup.find("div", class_="mt-5 d-flex flex-wrap flex-lg-nowrap justify-between")
		asset_name = soup.find("h1", class_="lh-4").text[:6]
		yelds = div.find_all("strong")
		fields = div.find_all("b", class_="sub-value fs-4 lh-3")
		
		return {
			f"{asset_name}":{
				"Previous": {
					"Value": yelds[0].text,
					"BaseDate": fields[2].text,
					"PaymentDate": fields[3].text
				},
				"Next": {
					"Value": yelds[1].text,
					"BaseDate": fields[6].text,
					"PaymentDate": fields[7].text
				}
			}
		}

	def scrape(self, assets: list[str], filename: Optional[str] = None) -> None:
		try:
			structure = {
				"Assets": {

				}
			}
			li=[]
			for asset in assets:
				self.__checkurl(asset)
				li.append(self.__get_data(asset))

			structure["Assets"] = li
			if(filename):
				filename = filename.split(".")[0]+".json"
				with open(filename, "w") as w:
						w.write(json.dumps(structure, indent=4))
			else:
				print(json.dumps(structure, indent=4))
				
		except Exception as url_error:
			print(url_error)
			
def main():
	parser = argparse.ArgumentParser(description="Take assets inside StatusInvest and outputs inside a json file where is located")
	parser.add_argument("-a","--assets", nargs="+" ,type=str, metavar="asset_list", help="One or many assets to scrape", required=True)
	parser.add_argument("-o", "--output", type=str, metavar="filename", help="Outputs the data to a .json File")

	args = parser.parse_args()
	
	scraper = ObjectScrapper()
	if(not args.output):
		scraper.scrape(args.assets)
		return
	scraper.scrape(args.assets, args.output)

if __name__ == "__main__":
	main()