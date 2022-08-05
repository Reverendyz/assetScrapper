import json
import multiprocessing
import os
from re import L
from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool


class ObjectScrapper:
	def __init__(self):
		self.filename = 'teste.json'
		pass

	def __get_content(self, link_to_scrape):
		r = requests.get(link_to_scrape)
		return BeautifulSoup(r.content, 'html.parser')

	def __get_content_list(self, URL_List):
		contents = list(map(lambda site: BeautifulSoup(requests.get(site).content, 'html.parser'), URL_List))
		objList = []
		for html in contents:
			value = html.find_all('strong', class_="fs-5")
			assets = html.find_all('b', class_="sub-value")
			asset_name = html.find("h1", class_="lh-4")
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
			# print(stocks)
			objList.append(stocks)
		return objList

	def __append_json(self, object_list):
		if not os.path.isfile(self.filename):
				raise FileNotFoundError

		json_file = open(self.filename)
		a = json.load(json_file)

		for asset in object_list:
			a["Assets"].append(asset[0])

		with open('newtest.json', 'w+') as json_out:
				json.dump(a, json_out, indent=2)
		


	def scrape(self, scrape_this):
		if scrape_this == '':
				return		
		if type(scrape_this) == list:
			contents = self.__get_content_list(scrape_this)
			self.__append_json(contents)
			return
		else: #If has one single object to scrape
			soup = self.__get_content(scrape_this)
				
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

			

