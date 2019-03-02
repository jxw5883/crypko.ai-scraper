from bs4 import BeautifulSoup, SoupStrainer
import requests
from os.path import basename
import os

url = "https://s.crypko.ai/c/"
jsonURLHeader = "https://api.crypko.ai/crypkos/"
jsonURLEnding = "/detail"
#r_session = requests.Session()

def getImages(soup, count):
    soup.find_all("img")
    for link in soup.select("img[src^=http]"):
        lnk = link["src"]
        with open("img/" + str(count) + "-" + basename(lnk), "wb") as f:
            f.write(requests.get(lnk).content)
            
def getJSON(num):
    url = jsonURLHeader + str(num) + jsonURLEnding
    with open("json/" + str(num) + "-" + basename(url) + ".json", "wb") as f:
        f.write(requests.get(url).content)
        
#def checkProgress(): TODO
    #dir_info = os.listdir("img")
    
    
def main(final_img):
    
    if not os.path.exists("img") or not os.path.exists("json"):
        os.makedirs("img")
        os.makedirs("json")
    
    start = 1
    for i in range(start, final_img):
        soup = BeautifulSoup(requests.get(url + str(i)).content, "lxml")
        print("passed request")
        getImages(soup, i)
        #getJSON(i)
        print("successful: " + str(i))
        
main(712044);

# 1105 8:50:48,  1205 08:54:02
