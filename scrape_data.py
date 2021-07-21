#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 05:19:59 2021

@author: tural
"""

from selenium import webdriver
import pandas as pd

option = webdriver.ChromeOptions()

option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')


# taking each page link from web side 
page_first_part = "https://www.kijiji.ca/b-apartments-condos/british-columbia/page-"
page_second_part = "/c37l9007?ad=offering"
next_pages = []

page_numbers = range(2, 59)
for n in page_numbers:
  pages = page_first_part + str(n)+page_second_part
  next_pages.append(pages)
  # adding list first link of page
next_pages.append("https://www.kijiji.ca/b-apartments-condos/british-columbia/c37l9007?ad=offering")

# scraping each item link from web pages
my_link_ext = []
wd = webdriver.Chrome(options=option)
for link in next_pages:
    wd.get(link)
    my_links = wd.find_elements_by_class_name("info-container")
    index_cont = next_pages.index(link)
    persent = (100*index_cont)/len(next_pages)
    print("progress {} %".format(persent)) # it was just ckecing progress while running 
    for link in my_links:
        link_each = link.find_element_by_xpath(".//*[@class='title']")
        my_link =link_each.get_attribute('innerHTML')
        a = my_link.find("href") + 6
        b = my_link.find("class") - 2
        my_link_ext.append("https://www.kijiji.ca"+my_link[a:b])
        
# Second part of scraping we will going to scrape info from each pages
        
my_home_type = []
my_home_bedroom = []
my_home_bathroom = []
my_price = []
alll_info = []
alll_info_text = []

page_scr = webdriver.Chrome(options=option)
for i in my_link_ext:
    page_scr.get(i)
    try:
        my_pr = page_scr.find_element_by_xpath(".//*[@class='priceWrapper-1165431705']").text
        my_pr_1 = my_pr.split("\n")[0] ## Price for each home
        print(my_pr_1)
    except:
        my_pr_1 = i
        print("price not working")
    try:
        home_types = page_scr.find_element_by_xpath(".//*[@class='unitRow-1281171205']").text
        my_home = home_types.split("\n")[0] # home type condo,apart etc..
        my_bedroom = home_types.split("\n")[1] #bedroom 
        my_bathroom = home_types.split("\n")[2] # bathroom
        print(my_home)
    except:
        my_home = i
        my_bedroom = i
        my_bathroom = i
        print("home my not working")
    try:
      uti = page_scr.find_element_by_xpath(".//*[@class='gradientScrollWrapper-2607347244']").get_attribute('innerHTML')
      uti2 = page_scr.find_element_by_xpath(".//*[@class='gradientScrollWrapper-2607347244']").text
      alll_info.append(uti)
      alll_info_text.append(uti2)
      print(uti[1])
    except:
      alll_info.append(i)
      alll_info_text.append(i)
      print("all info not working or all")
    my_home_type.append(my_home)
    my_home_bedroom.append(my_bedroom)
    my_home_bathroom.append(my_bathroom)
    my_price.append(my_pr_1)
    my_index = my_link_ext.index(i)
    persent = (my_index*100)/len(my_link_ext)
    print(persent)
    
    
    

df = pd.DataFrame(list(zip(my_home_type, my_home_bedroom,my_home_bathroom,my_price,alll_info,alll_info_text)),
               columns =['house_type', 'bedroom',"bathroom","price","all_info","info_text"])

df.to_csv("my_new_scrape_file.csv")