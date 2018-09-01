# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 02:07:13 2018

@author: write
"""

# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

#specify URL
quote_page = input('What URL would you like to scrape?')

#query website and return HTML to the variable page
page = urlopen(quote_page)

#parse the HTML with BeautifulSoup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

#now we have the HTML as soup, so we need to grab the title and headers
for x in soup:
    title = soup.find('title')
    h1s = soup.find_all('h1')
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')

#print out the data in readable format, including "none" for missing data types
print()
print('Title:')
for t in title:
    print(title) 
print()
print('H1s:')

print(h1s)
print()
print('H2s:')
print(h2s)
print()
print('H3s:')
print(h3s)