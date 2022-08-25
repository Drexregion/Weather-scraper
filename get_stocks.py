# Import the necessary libraries for the code
import requests
import csv
from bs4 import BeautifulSoup

# Processing of the user input
class functionality:
    def __init__(self,product):
        self.product = product

    def stocks(self):
        # Main csv file created
        csv_file = open(f"{self.product}.csv",'w')
        writer = csv.writer(csv_file)

        # Creating a fixed header for the csv file
        header = ["Laptop","Costprice","Sellingprice",]
        writer.writerow(header)

        # Initializing the web scraper to scrape the website for stocks
        url = requests.get(f'https://www.jumia.com.ng/catalog/?q={self.product}')
        web_parser= BeautifulSoup(url.content,'html.parser')
        parent_parse = web_parser.find(class_='-paxs row _no-g _4cl-3cm-shs')

        # The amount of items present in the stock(8 sensored product on every page)
        counter = len(parent_parse)-8

        # Getting the chunk of data that contains the name and the laptops
        laptops = parent_parse.find_all(class_="name")#list that contains the product names
        price = parent_parse.find_all(class_="prc")#list that contains the product original price

        # Loop that runs to arrange the data chunks
        for i in range(counter):
            laptop = laptops[i].get_text()
            string_1 = (str(f"{price[i].get_text()}"))

            # Remove unnecessary characters from the price string for easy casting(int())
            formatted_string = string_1.translate({ord(','): None})
            # original_price= int(formatted_string.translate({ord('₦'): None}))(Another way)
            original_price = int(formatted_string.replace('₦',''))

            # increment price of the original price of products on the website
            dropship_price = int((original_price) * 1.2)

            # Profit gotten after every sale
            profit = dropship_price - original_price

            # Verification of fuctionality
            print(f"{laptop}  : ₦{original_price}  :  ₦{dropship_price}   : ₦{profit}")

            # Creating the main csv file for products
            writer.writerow([str(laptop),str(original_price),str(dropship_price)])
        