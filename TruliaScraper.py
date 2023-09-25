
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json
import ast
import os
from urllib.request import Request, urlopen
import pandas as pd
import time
import random


def Scraper_price_history (links):
    for link in links:
        price_history = pd.DataFrame()
        try:
            # For ignoring SSL certificate errors
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            
            # Input from user
            # Making the website believe that you are accessing it using a mozilla browser
    
        # List of user-agent strings for different browsers
            user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/94.0.992.50',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/92.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 OPR/78.0.4093.112',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'
                ]
            user_agent = random.choice(user_agents)
            req = Request(link, headers={'User-Agent': user_agent})
            webpage = urlopen(req).read()
            
            # Creating a BeautifulSoup object of the html page for easy extraction of data.
            
            soup = BeautifulSoup(webpage, 'html.parser')
            html = soup.prettify('utf-8')
            product_json = {}
            
            
            
            # Find the div element with data-test-id="price-history-container"
            price_history_container = soup.find('div', {'data-testid': 'price-history-container'})
    
            # Check if the div element is found
            if price_history_container:
                col_index = 0
                # Find the table element within the div
                price_history_table = price_history_container.find('table')
                # Check if the table element is found
                if price_history_table:
                    for row in price_history_table.find_all('tr', attrs={'style':""}):
                        for cells in row.find_all('td'):
                            for divs in cells.find_all('div'):
                                col_index = col_index + 1
                                price_history.loc[link,col_index] = divs.text.strip()
                                
                else:
                    print("No table found inside the div with data-test-id='price-history-container'")
            else:
                print("Div with data-test-id='price-history-container' not found on the page")
            time.sleep(4)
        except:
            pass
    return price_history
    
    



























