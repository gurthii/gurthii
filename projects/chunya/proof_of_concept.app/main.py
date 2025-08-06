import requests
import psycopg2
from bs4 import BeautifulSoup

user_input = input("Weka kitu hapa: ") # expecting url or sku

# User Input validation
# - TODO: validate whether input is a SKU (e.g., AI234HA565EGENAFAMZ) or url (e.g., https://www.jumia.co.ke/ailyons-an-3006a-electric-dry-iron-box-non-stick-sole-plate-1000w-1yr-wrty-309506621.html)
# - Regex would be ideal for url/sku validation but to make it simpler i will go with len() and if contain "jumia" then proceed to check db

url = None
sku = None
price = None

def user_input_validation(user_input):
	global url, sku # global keyword ensures global variable is changed inside a function
	if "jumia" in user_input:		
		url = user_input
	elif len(user_input) == 19:
		sku = user_input
	else:
		print("invalid user data")
		user_input = input("try again: ")

def prod_to_db_validation():

	# Checks if url/sku exists in database

	# Adds product details (sku, name, url, timestamp) to db
	pass

def price_runner_applet():
	# runs periodically to update prices of specific skus in db
	pass

def getSoup(url_): # just url after validation
	global price, sku, url
	# making soup with sku or url

	# add browser user agent if 403 is returned
	headers = {
	'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
	} # this has to be a dictionary with key/value elements

	if url_ != None:
		print("Getting soup for user input url...")
		
		response = requests.get(url_, headers=headers).text

		# making soup, aka parsing the HTML content
		soup = BeautifulSoup(response, 'html.parser') # other parser options include: lxml, html5lib
		print("url soup done...")

		price_group = soup.find_all('span', class_='-b -ubpt -tal -fs24 -prxs')
		for price_item in price_group:
			if price_item:
				price = int(price_item.text.split(" ")[-1].replace(",", ""))
		
		sku_group = soup.find_all('li', class_='-pvxs')
		for sku_item in sku_group:
		# trying to work with this '<li class="-pvxs"><span class="-b">SKU</span>: AI234HA565EGENAFAMZ</li>'
			if 'SKU' in sku_item.text:
				sku = sku_item.text.split(": ")[-1]
			break
	

		return soup
	else:
		print(sku)
		url_soup = f"https://www.jumia.co.ke/catalog/?q={sku}"
		
		print("Getting soup for user input sku...")

		pre_response = requests.get(url_soup, headers=headers).text
		pre_soup = BeautifulSoup(pre_response, 'html.parser')

		pre_prod_url_class = pre_soup.find_all('article', class_ = 'prd _fb col c-prd')
	
		for prod_details in pre_prod_url_class:
			url = "https://www.jumia.co.ke" + prod_details.find('a', class_ = 'core')['href']
		
		response = requests.get(url, headers=headers).text

		soup = BeautifulSoup(response, 'html.parser') # other parser options include: lxml, html5lib
		price_group = soup.find_all('span', class_='-b -ubpt -tal -fs24 -prxs')
		for price_item in price_group:
			if price_item:
				price = int(price_item.text.split(" ")[-1].replace(",", ""))
		print("sku soup done...")
		return soup

user_input_validation(user_input)
getSoup(url)
print(f"{url}, {price}, {sku}")
