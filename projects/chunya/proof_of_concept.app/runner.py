
import requests, psycopg2
from bs4 import BeautifulSoup

# HTML PARSING
def getSoup(url):
	# check url with requests module
	response =  requests.get(url) # returns status code
	# print(response.text)

	# add browser user agent if 403 is returned
	headers = {
		'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
	} # this has to be a dictionary with key/value elements

	response = requests.get(url, headers=headers).text
	# print(response)

	# making soup, aka parsing the HTML content
	soup = BeautifulSoup(response, 'html.parser') # other parser options include: lxml, html5lib
	
	return soup

# DATABASE STORAGE
conn = psycopg2.connect(
	database = "db_tengo", 
	user = "postgres", 
    host= 'localhost',
    password = "HRu1NFmQ18nJs49KoxR9p8f7QS33y3S",
    port = 5432
)

# Open a cursor to perform database operations
cur = conn.cursor()

# get all products
cur.execute("SELECT * FROM products")
prods_table = cur.fetchall()

cur.execute("SELECT * FROM prices WHERE sku='AI234HA565EGENAFAMZ'")
prices_table = cur.fetchone()

counter = 0

print(prices_table)

# while counter < len(prods_table):
# 	db_sku = prods_table[counter][0]
# 	db_url = prods_table[counter][-1]
	

# 	# get current price with soup
# 	soup = getSoup(url)
# 	price_class_group = soup.find_all('span', class_ = '-b -ubpt -tal -fs24 -prxs')
# 	for price_item in price_class_group:
# 		if price_item:
# 			raw_price = price_item.text.split(" ")[-1]
# 			price = int(raw_price.replace(",","")) # coverts this '<span class="-b -ubpt -tal -fs24 -prxs">KSh 8,099</span> to usable integer
# 			print(price)
	


# 	counter += 1

# get last price, if exists

# # HTML PARSING
# # check url with requests module
# response =  requests.get(url) # returns status code
# # print(response.text)

# # add browser user agent if 403 is returned
# headers = {
# 	'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
# } # this has to be a dictionary with key/value elements

# response = requests.get(url, headers=headers).text
# # print(response)

# # making soup, aka parsing the HTML content
# soup = BeautifulSoup(response, 'html.parser') # other parser options include: lxml, html5lib
# # print(soup.prettify()) # better formatted HTML

# # identifying specific details to extract
# price, name, sku = None, None, None # initialize variables needed 

# # price details class: '-b -ubpt -tal -fs24 -prxs'
# price_group = soup.find_all('span', class_ = '-b -ubpt -tal -fs24 -prxs')
# for price_item in price_group:
# 	if price_item:
# 		raw_price = price_item.text.split(" ")[-1]
# 		price = int(raw_price.replace(",","")) # coverts this '<span class="-b -ubpt -tal -fs24 -prxs">KSh 8,099</span> to usable integer
		
# # product name class: -fs20 -pts -pbxs
# name_group = soup.find_all('h1', class_='-fs20 -pts -pbxs')
# for name_item in name_group:
# 	if name_item:
# 		name = name_item.text

# # product sku class: '-b'
# sku_group = soup.find_all('li', class_='-pvxs')
# for sku_item in sku_group:
# 	# trying to work with this '<li class="-pvxs"><span class="-b">SKU</span>: AI234HA565EGENAFAMZ</li>'
# 	if 'SKU' in sku_item.text:
# 		sku = sku_item.text.split(": ")[-1]
# 		break
# # print(price, name, sku, url)

conn.commit()
cur.close()
conn.close()