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

- Second part was scraping **Price ,Size,House type,Hydro-Water-Heat include,Smoke,Outdor Space, Air Conditioning,Appliances,Furnished or not,Pet allow or not,Parking,Size S/F,Wifi and TV,Bathrooms,Bedrooms** (FYI we can take more data but I think its enough)

```python
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
    percent = (my_index*100)/len(my_link_ext)
    print(percent) #just for display process
    
```
- Third part was cleaning and make it more more clean our dataset. **all_info and info_text** columns were cleaned and file was saved csv format

#
2. Data Cleaning , Data Visualization, Feature extraction and Traing part
- While cleaning column appliances was cleaned like : Laundry_In_Building yes or not etc.,Hydro Water and Heat was same . Bedrooms and Bathrooms values was "[' 2']" simvols was deleted
- Data Visualization (images will loaded)
- Feature extraction and Training: I find first price per sqrft then descirbed my data
```python
for i in df4["house_type"].unique():
    print("{} type of home per_price_sq".format(i))
    print(df4[df4["house_type"]==i]["per_price_sq"].describe())
    print(20*('*'))
``` 
values which is out of major 75% and 25% was droped for next steps same parametrs not effecting to much our dataset that ones also was dropped from our datset
and DataFrame was ready for traing.
- Training I used RandomForestRegressor and DecisionTreeRegressor 
```python
model = RandomForestRegressor(criterion="mse",max_features="sqrt",n_estimators=200,max_depth=10)
model.fit(X_train, y_train)
tree_preds = model.predict(X_test)
print('Random Forest: ', r2_score(y_test, tree_preds))

model1 = DecisionTreeRegressor() 
model1.fit(X_train, y_train)
tree_preds1 = model1.predict(X_test)
print('Random Forest: ', r2_score(y_test, tree_preds))
``` 
both of then resul was 77% and it was great and I saved model which is trained with RandomForestRegressor
#
3. [Flask server (End of project)](https://github.com/tural327/price_pred_full_project)
Basic web app was created for show results (html css used)
*[](https://github.com/tural327/price_pred_full_project/blob/master/result.PNG)

