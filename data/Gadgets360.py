import requests
from bs4 import BeautifulSoup

from Gadgects360_function import get_dict

url = "https://www.gadgets360.com/news"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

outer_div = soup.find("div", class_="pagination row margin_t30 margin_b30")
s=outer_div.find_all("a")[-1].get("href")
count = int(s[outer_div.find_all("a")[-1].get("href").rfind('/')+6:])

dict_list= []


data = ""



b=0
for i in range(1,count):
# for i in range(1,2):
  url_="https://www.gadgets360.com/news"+"/page-"+str(i)
  response_ = requests.get(url_)
  soup_ = BeautifulSoup(response_.content, "html.parser")
  class_=soup_.find("div", class_="story_list row margin_b30")
  all_list = class_.find_all("li")
  
  for j in all_list:
    link=j.find('a')
    
    if link ==None:
      continue
    
    link =link.get('href')
    text = j.find('span', class_="news_listing").text.strip()
    
    date = j.find('div',class_="dateline").text.strip()
    dict = get_dict(link,text,date)

    dict_list.append(dict)



s = ""  
for i in dict_list:
  s = s+str(i[0])+"\n\n\n\n\n"


with open('Gadgets.txt', 'w', encoding='utf-8') as f:
    f.write(s)
    
with open('title.txt', 'w') as f:
    f.write(text)
  
  
  

