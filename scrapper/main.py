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
		r = requests.get(f"https://statusinvest.com.br/fundos-imobiliarios/{asset}", headers={'User-Agent': 'Mozilla/5.0'})

		links = re.findall(r"link.href.*\b", r.text)

		for link in links:
			if(link.__contains__("error") or link.__contains__("Error Code")):
				raise Exception(f"This asset '{asset}' was not found in Statusinvest/fundos-imobiliarios")

	def __parse_to_object (self, asset: str, position: Optional[int] = None) ->  dict:
		r = requests.get(f"https://statusinvest.com.br/fundos-imobiliarios/{asset}",headers={'User-Agent': 'Mozilla/5.0'})
		soup = BeautifulSoup(r.text, "html.parser")
		div = soup.find("div", attrs={"class": "mt-5 d-flex flex-wrap flex-lg-nowrap justify-between"})
		asset_name = soup.find("h1", attrs={"class": "lh-4"}).text[:6]
		yelds = div.find_all("strong")
		fields = div.find_all("b", attrs={"class": "sub-value fs-4 lh-3"})
		
		return {
				f"Asset":asset_name,
				"Position": position,
				"Previous": {
					"Value": float(yelds[0].text.replace(",", ".")),
					"BaseDate": fields[2].text,
					"PaymentDate": fields[3].text
				},
				"Next": {
					"Value": float(yelds[1].text.replace(",", ".")) if yelds[1].text != "-" else 0,
					"BaseDate": fields[6].text,
					"PaymentDate": fields[7].text
				}
			}

	def scrape(self, assets: list[str], positions: list[int], filename: Optional[str] = None) -> None:
		try:
			structure = {
				"Assets": {

				}
			}
			asset_list=[]
			for index, asset in enumerate(assets):
				self.__checkurl(asset)
				asset_list.append(self.__parse_to_object(asset, positions[index]))

			structure["Assets"] = asset_list
			if(filename):
				filename = filename.split(".")[0]+".json"
				with open(filename, "w") as destinaion:
						destinaion.write(json.dumps(structure, indent=4))
			else:
				print(json.dumps(structure, indent=4))
				
		except Exception as url_error:
			print(url_error)

def main():
	parser = argparse.ArgumentParser(description="Take assets inside StatusInvest and outputs inside a json file where is located")
	parser.add_argument("-a","--assets", nargs="+" ,type=str, metavar="asset_list", help="One or many assets to scrape", required=True)
	parser.add_argument("-f", "--filename", type=str, metavar="filename", help="Outputs the data to a .json File")
	parser.add_argument("-p", "--positions", nargs="+", type=int, help="List of the owned asset position. This must be related with <assets> position", required=True)

	args = parser.parse_args()

	if len(args.assets) != len(args.positions):
		raise Exception(f"Make sure that assets and position have the same amount of elements Assets:{len(args.assets)} Positions:{len(args.positions)}")
	
	scraper = ObjectScrapper()
	if(not args.output):
		scraper.scrape(args.assets, args.positions)
		return
	scraper.scrape(args.assets, args.positions, args.output)

if __name__ == "__main__":
	main()