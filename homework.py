from bs4 import BeautifulSoup
from openpyxl import Workbook
from selenium import webdriver
import os

murl = 'https://jobs.51job.com/beijing/hy01/p1/'

def get_source(url):
    browser = webdriver.Edge()
    browser.get(url)
    data = browser.page_source
    browser.close()
    return data

def get_all():
    data = get_source(murl)
    soup = BeautifulSoup(data,"html.parser")
    # print(data)
    with open('html.txt','w', encoding='utf8') as file :
        file.write((data))
        file.close()

    infos = soup.find_all('p',{'class':"info"})
    orders = soup.find_all('p',{'class':"order"})

    info_data = []
    order_data = []

    for item in infos : 
        title = item.find('span',{'class':'title'}).text
        time = item.find('span',{'class':'time'}).text
        salary = item.find('span',{'class':'location'}).nextSibling.text
        location = item.find('span',{'class':'location name'}).text
        company = item.find('a',{'class':'name'}).text
        info_data.append([title,time,salary,location,company])
        # print(title,time,salary,location,company)

        
    for order in orders:
        items = order.text.split('|')
        temp = []
        for item in items :
            content = item.split('：')
            temp.append([content[0], content[1]])
        order_data.append(temp)
            # print(content)
    print(len(order_data))
    print(len(info_data))
        
    for i in range(len(info_data)) :
        print(info_data[i])
        print(order_data[i])
        print()
        
    return info_data, order_data

def save_file():
    pass


if __name__ == "__main__":
    get_all()