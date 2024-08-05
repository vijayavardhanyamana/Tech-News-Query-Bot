import requests
from bs4 import BeautifulSoup

def get_dict(url,title,writer):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    outer_div = soup.find_all(class_="content_text row description")

    data=[]
    # data.append("title = " + '"' + title+ '"' + " , ")

    
    count=0
    if outer_div:
        key_=title
        text = ""
        for i in outer_div[0].children:
            text = text + " " + i.text.strip()

        data.append("title = " + '"' + title+ '"' + " , "+text) 

    return data

    