'''
Web2table is used for scrapping table(s) from a website to csv(s)
created by Mukhamad Suhermanto

write URL:
'''

from pandas.io.html import read_html
import numpy as np
import pandas as pd

#def web2tables():
url = input("Write your URL here: ")
webtables = read_html(url, attrs={"class":"wikitable"})
tableNum = len(webtables) # measuring the number of tables available
tableList = np.arange(1, tableNum, 1) #creating the list of number of tables within the range of the list
    #return print("The web/wiki input is successful.")


    




