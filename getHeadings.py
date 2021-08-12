#script gets all headding tags from list of URLS

from requests import get
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import re




infile = open("HEADINGSLIST.xml","r")
contents = infile.read()
url_list_raw  = str(BeautifulSoup(contents,'xml'))
numProcessed = 0
words = []

url_list = re.findall(r'HREF="(.*?)" ADD_DATE', url_list_raw)

#url_list = pd.read_csv('/Users/m./Google Drive/DataProject_thandi/remaining.csv')

def getHeadings(url, words):
    
    try:
        soup = BeautifulSoup(get(url).content, "html.parser")
        
        
        h1 = soup.find("h1").text
        print(h1)
        input("here")
        
        h1 = h1.split()
        for i in h1:
            print(i)
            words.append(i)
                
        try:
            h2 = soup.find("h2").text
            h2 = h2.split()
            for i in h2:
                words.append(i)
        except Exception as e:
            print(e)


        try:
            h3 = soup.find("h3").text
            h3 = h3.split()
            for i in h3:
                words.append(i)
        except Exception as e:
            print(e)

        try:
            print(words)
            
            csv = pd.DataFrame(data = words)
            print(csv)
            csv.to_csv("headings_raw.csv")
        except Exception as e:
            print(e)
        

    except Exception as e: 
            print(e)
            print("ERROR PROCESSING")
            print(url)


# url_list = url_list["urls"]


for url in url_list:
    
    if(url[-4:] == ".pdf"):
        print('skip')
    
    else:
        print(url)
        try:
            soup = BeautifulSoup(get(url).content, "html.parser")
            if(len(soup.find_all('h1')) > 0):

                h1 = soup.find("h1").text
                h1 = h1.split()
                for i in h1:
                    words.append(i)
                    
            if(len(soup.find_all('h2')) > 0):
                h2 = soup.find("h2").text
                h2 = h2.split()
                for i in h2:
                    words.append(i)
            if(len(soup.find_all('h3')) > 0):
                h3 = soup.find("h3").text
                h3 = h3.split()
                for i in h3:
                    words.append(i)
            
            
            
            csv = pd.DataFrame(data = words)
            
            csv.to_csv("headings_rawv2.csv")
            numProcessed = numProcessed +1
            print(numProcessed)

        except Exception as e: 
                print(e)
                print("ERROR PROCESSING")
                print(url)
#save Collected Words

print("done")
    
    
    
    
  