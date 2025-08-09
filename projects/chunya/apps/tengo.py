import requests
import psycopg2
from bs4 import BeautifulSoup

def accept_input():
	"""Requests any user input"""
	return input("weka kitu: ").strip()
		
def validate():
	"""Validating input to either return an sku, url, or loop back until achieved."""
	while True:
		user_input = accept_input()

		if not user_input: # catches None or empty strings
			print("Input can't be empty, retry...")
			continue # stops and restarts the loop

		if len(user_input) == 19: # valid sku has 19 characters
			return {"sku" : user_input, "url" : None}
		elif "jumia.co.ke" in user_input: # domain must always contain this
			return {"sku" : None, "url" : user_input}
		else:
			print("Invalid input, try inputing the product SKU or URL again...")

def bone_soup(url_):
	# counter possible 403 errors by ading browser user agents
	headers = {
		'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
	} # this has to be a dictionary with key/value elements

	response = requests.get(url_, headers=headers)
	response.raise_for_status() # Throw error if status != 200
	return BeautifulSoup(response.text, 'html.parser')

def get_product_data(input_data):
	"""Gets all the product details: sku, url, name, price."""
	sku = input_data['sku']
	url =  input_data['url']

	if sku:
		# processing SKU input
		search_url = f"https://www.jumia.co.ke/catalog/?q={sku}"
		try:
			sku_soup = bone_soup(search_url)

			product_cards = sku_soup.find_all('article', class_ = 'prd _fb col c-prd')
		
			for prod_details in product_cards:
				url = "https://www.jumia.co.ke" + prod_details.find('a', class_ = 'core')['href']
			soup = bone_soup(url)
			price = int(soup.find('span', class_='-b -ubpt -tal -fs24 -prxs').text.split(" ")[-1].replace(",", ""))
			name = soup.find_all('h1', class_='-fs20 -pts -pbxs')[0].text.strip()
		except Exception as e:
			print("Error here... SKU not found.")
			return None
		
		return sku, price, name, url
	elif url:
		# processing URL input
		try:
			soup = bone_soup(url)
			price = int(soup.find('span', class_='-b -ubpt -tal -fs24 -prxs').text.split(" ")[-1].replace(",", ""))
			name = soup.find_all('h1', class_='-fs20 -pts -pbxs')[0].text.strip()

			sku_group = soup.find_all('li', class_='-pvxs')
			# trying to work with this '<li class="-pvxs"><span class="-b">SKU</span>: AI234HA565EGENAFAMZ</li>'
			for sku_item in sku_group:
				if 'SKU' in sku_item.text:
					sku = sku_item.text.split(": ")[-1]
					break
			return sku, price, name, url

		except AttributeError as e:
			print("Error occured... wrong url, try again...")
			return None

def get_connection():
	# Data config
	return psycopg2.connect(
		database = "tengoapp", 
		user = "tengoboos", 
	    host= 'localhost',
	    password = "GArtyPOpGreN",
	    port = 5432
	    )

def add_product_todb(sku, price, name, url):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""CREATE TABLE IF NOT EXISTS products (
	    product_sku VARCHAR(255) PRIMARY KEY,
	    product_name VARCHAR(255) NOT NULL,
	    product_url TEXT
	    );
	""")

	cur.execute("""CREATE TABLE IF NOT EXISTS prices (
	    price_id SERIAL PRIMARY KEY,
	    sku_value VARCHAR(255) NOT NULL REFERENCES products(product_sku),
	    current_price DECIMAL(10, 2) NOT NULL,
	    timestamp BIGINT DEFAULT (EXTRACT(EPOCH FROM NOW()))
	    );
	""")

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
		WHERE sku_value = %s
		ORDER BY timestamp DESC
		LIMIT 1;
	""", (sku,))

	price_result = cur.fetchone()

	if price_result != None:
		if price != float(price_result[0]):
			cur.execute("""
			    INSERT INTO prices (sku_value, current_price)
			    VALUES (%s, %s);
			""", (sku, price))
			print("Price change has been recorded.")
		else:
			print(f"{sku}: No price changes yet.")
	else:
		cur.execute("""
		    INSERT INTO prices (sku_value, current_price)
		    VALUES (%s, %s);
		""", (sku, price))	
		print("New price record has been added.")
	# Closing the database connection
	conn.commit()
	cur.close()
	conn.close()

def price_updater_app():
	conn = get_connection()
	cur = conn.cursor()

	all_data_from_prod = cur.execute("SELECT * FROM products")
	rows = cur.fetchall()
	for sku_dbitem in rows:
		# get actual current price from site
		sku_from_db = sku_dbitem[0]
		try:
			actual_current_price = float(get_product_data({'sku': sku_from_db, 'url' : None})[1])

			# compare with most recently recorded price in db
			all_price_data_from_price = cur.execute("""
				SELECT current_price
				FROM prices
				WHERE sku_value = %s
				ORDER BY timestamp DESC
				LIMIT 1;
				""", (sku_from_db,))

			current_price_from_db = cur.fetchone()[0]
			
			if current_price_from_db != actual_current_price:
				print("price change!", actual_current_price, current_price_from_db)

				cur.execute("""
					INSERT INTO prices (sku_value, current_price)
					VALUES (%s, %s);
					""", (sku_from_db, actual_current_price))	
			else:
				print(f"No change in price! for {sku_from_db}", actual_current_price, current_price_from_db)
		except Exception as e:
			print("Item probably out of stock. Continuing to the next item in for loop.")
			continue
		


	conn.commit()
	cur.close()
	conn.close()

def main():
	while True:
		input_data = validate()
		result = get_product_data(input_data)
		
		if result:
			sku = result[0]
			price  = result[1]
			name = result[2]
			url = result[3]
			add_product_todb(sku, price, name, url)
		else:
			print("loop restart..")
			price_updater_app()

if __name__ == "__main__":
    main()	
