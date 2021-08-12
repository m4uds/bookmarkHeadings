#script gets google image refults for a keywords that 

from re import search
from pandas.core.frame import DataFrame
from pandas.io.parsers import read_csv
from requests import get
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import os
import re


#url_list = pd.read_csv("/Users/m./Google Drive/DataProject_thandi/history.csv")
#url_list = url_list["url"]

infile = open("HEADINGSLIST.xml","r")
contents = infile.read()
url_list_raw  = str(BeautifulSoup(contents,'xml'))
url_list = re.findall(r'HREF="(.*?)" ADD_DATE', url_list_raw)

print(url_list)

print(len(url_list))

imgCounter = 0
siteCounter = 0

#google syntax for "+"
plus = "+%2B+"
search_string = "data"

if (os.path.isfile(search_string+"HREF_log.csv")):
    HREF_log = pd.read_csv(search_string+"HREF_log.csv")
    
else:
    HREF_log = pd.DataFrame(data = {"HREF_log":[]})

print(HREF_log)



for site in url_list:
    
    url =  "https://www.google.com/search?q="+search_string+"+site%3A"+site+"&tbm=isch&ved=2ahUKEwjW_8qUy47yAhWSLisKHZM6ASsQ2-cCegQIABAA&oq="+search_string+"+site%3A"+site+"&gs_lcp=CgNpbWcQA1CmjAFYiZkBYOWeAWgAcAB4AIABuQKIAccHkgEHMC4yLjEuMZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=de0FYZbxEJLdrAGT9YTYAg&bih=659&biw=1024"
   
    print(url)

    soup = BeautifulSoup(get(url).content, "html.parser")

    siteCounter = siteCounter + 1

    images = soup.findAll("img")
    print(len(images))
    
    if (len(images) > 1):
        
        for img in images:
        
            if (str(img) == '/images/branding/searchlogo/1x/googlelogo_desk_heirloom_color_150x55dp.gif'):
                print()
            else:    
                imgCounter = imgCounter + 1
                try:
                    for i in HREF_log:
                        if(str(img['src']) == i):
                            print("IMAGE ALREADY DOWNLOADED")
                    else:
                        downloadImg = urllib.request.urlretrieve(str(img['src']), str(imgCounter)+search_string+".png")                        
                        df = pd.DataFrame(data = {"HREF_log": [str(img['src'])]})
                        HREF_log = HREF_log.append(df,ignore_index=True)
                        HREF_log = HREF_log["HREF_log"]
                        HREF_log.to_csv(str(search_string)+"HREF_log.csv") 

                except Exception as e:
                   print(e)
            #except:
            #    print("COULD NOT DOWNLOAD")
        
