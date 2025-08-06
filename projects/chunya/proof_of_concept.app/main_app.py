import requests
import psycopg2
from bs4 import BeautifulSoup


"""
Tengo App:

"""

# INPUT VALIDATION
# url = input("Input product url: ")

# also accept SKU
sku = "AI234HA565EGENAFAMZ"

def getProductDetails(url):

	# HTML PARSING
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
	# print(soup.prettify()) # better formatted HTML

	# identifying specific details to extract
	price, name, sku = None, None, None # initialize variables needed 

	# price details class: '-b -ubpt -tal -fs24 -prxs'
	price_group = soup.find_all('span', class_ = '-b -ubpt -tal -fs24 -prxs')
	for price_item in price_group:
		if price_item:
			raw_price = price_item.text.split(" ")[-1]
			price = int(raw_price.replace(",","")) # coverts this '<span class="-b -ubpt -tal -fs24 -prxs">KSh 8,099</span> to usable integer
			
	# product name class: -fs20 -pts -pbxs
	name_group = soup.find_all('h1', class_='-fs20 -pts -pbxs')
	for name_item in name_group:
		if name_item:
			name = name_item.text

	# product sku class: '-b'
	sku_group = soup.find_all('li', class_='-pvxs')
	for sku_item in sku_group:
		# trying to work with this '<li class="-pvxs"><span class="-b">SKU</span>: AI234HA565EGENAFAMZ</li>'
		if 'SKU' in sku_item.text:
			sku = sku_item.text.split(": ")[-1]
			break
	# print(price, name, sku, url)

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

	cur.execute("""CREATE TABLE IF NOT EXISTS products (
	    product_sku VARCHAR(255) PRIMARY KEY,
	    product_name VARCHAR(255) NOT NULL,
	    product_url TEXT
	    );
	""")

	cur.execute("""CREATE TABLE IF NOT EXISTS prices (
	    price_id SERIAL PRIMARY KEY,
	    sku VARCHAR(255) NOT NULL REFERENCES products(product_sku),
	    current_price DECIMAL(10, 2) NOT NULL,
	    timestamp BIGINT DEFAULT (EXTRACT(EPOCH FROM NOW()))
	    );
	""")


	# insert into table
	cur = conn.cursor()

	# Insert product (skip if already exists)
	cur.execute("""
	    INSERT INTO products (product_sku, product_name, product_url)
	    VALUES (%s, %s, %s)
	    ON CONFLICT (product_sku) DO NOTHING;
	""", (sku, name, url))

	# get last price, if exists
	cur.execute("""
		SELECT current_price
		FROM prices
		WHERE sku = %s
		ORDER BY timestamp DESC
		LIMIT 1;
	""", (sku,))

	result = cur.fetchone()

	# try insert new price

	if result != None:
		if price != float(result[0]):
			cur.execute("""
			    INSERT INTO prices (sku, current_price)
			    VALUES (%s, %s);
			""", (sku, price))
			print("Price change has been recorded.")
		else:
			print("No price changes yet.")
	else:
		cur.execute("""
		    INSERT INTO prices (sku, current_price)
		    VALUES (%s, %s);
		""", (sku, price))	
		print("New price record has been added.")

	conn.commit()
	cur.close()
	conn.close()

print("Input product url/sku: ")
getProductDetails(url)
# while True:
# 	url = input("Input product url: ")
# 	getProductDetails(url)
# 	print()