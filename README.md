# Home price prediction (**Canada, British Columbia**)
Project contain several parts

1. Data Scraping 

In this project data was taken from kijiji.com by using Selenium. Scraping prosedure containing main parts
- First we need to take links of each page number and it was so simple part I just used "for" loop for each page number and 
added my link list all pages and scrape each item from the links

```python
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
```

- Second part was scraping **Price ,Size,House type,Hydro-Water-Heat include,Smoke,Outdor Space, Air Conditioning,Appliances,Furnished or not,Pet allow or not,Parking,Size S/F,Wifi and TV,Bathrooms,Bedrooms**
(FYI we can take more data but I think its enough)
