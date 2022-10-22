import json
from bs4 import BeautifulSoup
import requests
import re

class ObjectScrapper:
	def __init__(self):
		self.filename = 'teste.json'
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
		
		return [{
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
		}]

	def scrape(self, assets: list[str]) -> None:
		try:
			test = {
				"Assets": {

				}
			}
			for asset in assets:
				self.__checkurl(asset)
				test["Assets"] = self.__get_data(asset)
			with open(self.filename, "w") as w:
				w.write(json.dumps(test,indent=4))
		except Exception as url_error:
			print(url_error)
		
