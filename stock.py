from cgitb import text
import pandas as pd
import datetime
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup

def web_content_div(web_content,class_path):
    web_content_div=web_content.find_all('div',{'class':class_path})
    try:
        spans=web_content_div[0].findall('span')
        texts=[spans.get_text() for span in spans]
    except IndexError:
         text=[]
         return texts

def real_time_price(stock_code):
    url='https://finance.yahoo.com/quote/'+stock_code+'%3DF?p='+stock_code+'%3DF'
    try:
        r=requests.get(url)
        web_content=BeautifulSoup(r,text,'lxml')
        texts=web_content_div(web_content,'My(6px) Pos(r) smartphone_Mt(6px)')
        if texts !=[]:
            price,change=texts[0],texts[0]
        else:    
            price,change=[],[]
    except ConnectionError:
        price,change= [],[]
    return price,change        
stock=['GC']    
print(real_time_price('GC'))