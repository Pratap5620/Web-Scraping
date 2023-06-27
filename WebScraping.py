#importing three different libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup as soup

#creating srapping class
class scraping():

    """creating an initialization function.
    so, When ever we call scraping class.
    It would automatically initialized"""
    def __init__(self,url:str):
        self.url = url

    # creating soup function where we will scrap the HTML: text_file
    def Soup(self):
        my_url = requests.get(self.url) #requesting the link
        website = soup(my_url.text,"html")#converting the web page into text_file
        #scrap particular class where your all data is stored
        data_set = website.findAll("div",{"class":"[enter class]"})
        total = len(data_set)

        print("Total Item Found: ",total)
        print("-------------------------------------------------")

        #creating cvs file
        filename = "product.csv"
        with open(filename, 'w') as f:
            header = 'Product Name, Price, Rating\n'
            f.write(header)

            #using for loop method to iterate over every class to get the output
            for container in range(len(data_set)):
                name = data_set[container].find_all("div", {"class": "[enter class]"})
                Brand_name = name[0].get_text()

                price = data_set[container].find_all("div", {"class": "[enter class]"})
                Product_price = price[0].get_text()

                offer = data_set[container].find("div", {"class": "[enter class]"})
                Offer_rate = offer[0].get_text()

                #soring the values in the csv file
                f.write(f'{Brand_name},{Product_price},{Offer_rate}\n')


        f.close()

#calling the class
scraper = scraping("[enter URL]")
scraper.Soup()

df = pd.read_csv("product.csv")
pprint(df)
