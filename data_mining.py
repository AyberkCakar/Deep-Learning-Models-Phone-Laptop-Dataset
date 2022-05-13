import time
import urllib.request
from random import randrange
urllib.request._MAXHEADERS = 1000

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'url'
driver.get(url)


SCROLL_PAUSE_TIME = 15

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(SCROLL_PAUSE_TIME)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


x_path = 'x_path'
content = driver.find_elements_by_xpath(x_path);

for val in content:
    src = val.get_attribute('src')
    print(src)
    
    #  urllib.request.urlretrieve(src, 'phone/'+str(randrange(999999999)+'.png')
    urllib.request.urlretrieve(src, 'laptop/'+str(randrange(999999999))+'.png')


driver.quit()
