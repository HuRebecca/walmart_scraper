
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://grocery.walmart.com/'

#open webdriver. get url
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

#clicks shop by department -> fruits and vegetables -> fresh fruit
Nav_button = driver.find_element_by_class_name('NavigationButton__button___1rVY9')
Nav_button.click()
time.sleep(3)
Nav_buttons = driver.find_elements_by_class_name('NavigationPanel__item___2JSjO')
Nav_buttons[2].click()
time.sleep(3)
Fresh_fruit_button = driver.find_element_by_link_text('Fresh Fruit')
Fresh_fruit_button.click()
time.sleep(5)

#html parsing
soup_level1 = soup(driver.page_source, 'html.parser')

#grabs each product
containers = soup_level1.findAll('div', {'class':'productTile__detailsOld___2bsVT'})
cents = soup_level1.findAll('sup', {'class':'priceTile__partialUnits___2fOQB'})

#create file
filename = 'products.csv'
f = open(filename, 'w')

headers = 'Item Name, Price \n'
f.write(headers)

for i, container in enumerate(containers):
    name = container.a.div.text
    price = container.div.div.span.sup.text + container.div.div.span.span.text + '.' + cents[i].text
    #print(name, price)
    f.write(name + ', ' + price + '\n')

f.close()
