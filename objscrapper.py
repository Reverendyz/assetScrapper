import json
from operator import contains
import os
from bs4 import BeautifulSoup
import requests

class ObjectScrapper:
	def __init__(self):
		self.filename = 'teste.json'
		pass


	def __create_main_file(self):
		"""Creates main file for usage if file is not existent

		"""
		with open(self.filename, 'w') as file:
			constructor = {
				"Assets":{
					}
			}
			constructor["Assets"] = []
			file.write(json.dumps(constructor, indent=2))
			file.close
	def read_outfile(self):
		with open(self.filename, 'r') as file:
			print(file.read())
			file.close()

	def __get_content(self, link_to_scrape):
		r = requests.get(link_to_scrape)
		print(r.status_code)
		return BeautifulSoup(r.content, 'html.parser')
		
			
	

	def __get_content_list(self, URL_List):
		contents = list(map(lambda site: self.__get_content(site), URL_List))
		objList = []
		for html in contents:
			if html.find('span', class_='fw-900').__contains__(f'OPS. . .'):
				print(f'This is not an valid asset')
				continue
			value = html.find_all('strong', class_="fs-5")
			assets = html.find_all('b', class_="sub-value")
			asset_name = html.find('h1', class_="lh-4")
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
				self.__create_main_file()

		json_file = open(self.filename)
		a = json.load(json_file)

		for asset in object_list:
			a["Assets"].append(asset[0])

		with open(self.filename, 'w+') as json_out:
				json.dump(a, json_out, indent=2)
		


	def scrape(self, scrape_this):
		if scrape_this == '':
				print(f'URL is empty')
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

			

