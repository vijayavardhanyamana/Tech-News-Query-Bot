import requests
from bs4 import BeautifulSoup
from Gadgects360_function import get_dict
from datetime import date

def update():
    with open('data/title.txt', 'r') as file:
        content = file.read()
        print(content)


    url = "https://www.gadgets360.com/news"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    outer_div = soup.find("div", class_="pagination row margin_t30 margin_b30")
    s=outer_div.find_all("a")[-1].get("href")
    count = int(s[outer_div.find_all("a")[-1].get("href").rfind('/')+6:])

    dict_list= []
    data = ""
    Break = False
    text = ""
    t =[]

    for i in range(1,count):
      # print("hi")

      url_="https://www.gadgets360.com/news"+"/page-"+str(i)
      response_ = requests.get(url_)
      soup_ = BeautifulSoup(response_.content, "html.parser")
      class_=soup_.find("div", class_="story_list row margin_b30")
      all_list = class_.find_all("li")
      # print("hello1")
      for j in all_list:
        # print("hello2")
        link=j.find('a')
        
        if link ==None:
          continue
        
        link =link.get('href')
        # print("hello3")
        text = j.find('span', class_="news_listing").text.strip()
        t.append(text)
        data = j.find('div',class_="dateline").text.strip()
        dict = get_dict(link,text,data)
        if text == content :
          Break =True
          break

        dict_list.append(dict)
    
      if Break == True:
          break

    s = ""  
    for i in dict_list:
      s = s+str(i[0])+"\n\n\n\n\n"


    day = date.today()
    # print("Today's date:", day)

    if s !="":
      with open('data/notepad'+str(day)+'.txt', 'w', encoding='utf-8') as f:
          f.write(s)
        

    # print(t[0])
    with open('data/title.txt', 'w') as f:
        f.write(t[0])
    

# update() 
  
  

