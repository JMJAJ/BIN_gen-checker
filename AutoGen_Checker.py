from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

import time
    

bin_list = ['417849xxxxxxxxxx', '440393xxxxxxxxxx', '520737xxxxxxxxxx', '526879xxxxxxxxxx', '409602xxxxxxxxxx',
          '513483xxxxxxxxxx', '404942xxxxxxxxxx', '527680xxxxxxxxxx', '527684xxxxxxxxxx', '525500xxxxxxxxxx']

### Default   - 5438164124xxxxxx [bin]
### MEXICO    - 417849xxxxxxxxxx
### USA       - 440393xxxxxxxxxx
### USA       - 520737xxxxxxxxxx
### AUSTRALIA - 526879xxxxxxxxxx
### BRAZIL    - 409602xxxxxxxxxx
### INDIA     - 513483xxxxxxxxxx
### BOLIVIA   - 404942xxxxxxxxxx
### BRAZIL    - 527680xxxxxxxxxx
### USA       - 527684xxxxxxxxxx
### ITALY     - 525500xxxxxxxxxx

def gen():
    url_gen = "https://technmind.com/ccgen/"
    url_check = "https://checker.visatk.com/ccn1/" # https://www.ontools.net/2022/04/cc-checker.html

    bin = "5438164124xxxxxx"
    act = ActionChains(driver)

    driver.get(url_gen)
    driver.find_element_by_name("ccp").send_keys(bin)
    driver.find_element_by_name("ccghm").click()
    act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    driver.find_element_by_name("ccghm").send_keys(100)
    driver.find_element_by_id("generar").click()
    # driver.find_element_by_class_name("copytoclipboard_data").click()
    driver.find_element(By.CLASS_NAME, "copytoclipboard_data").click()
    
    driver.get(url_check)
    driver.find_element_by_class_name("form-control").click()
    act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    time.sleep(1)
    driver.find_element_by_id("submit").click()
    time.sleep(30)
    # element_to_store = driver.find_element_by_class_name("panel-body").text()
    # print(element_to_store)

    # content = driver.find_elements_by_xpath('//span[@class="rankingItem-value js-countable"]')[0].text
    content = driver.find_elements(By.XPATH("div[@class='panel panel-default']/div[@id='tvmit_live']")).getAttribute("tvmit_live")
    content = driver.find_elements_by_id("tvmit_live")
    print(str(content))
    driver.find_element_by_css_selector('div.')

    # path = r'C:\Users\uzivatel 1\source\repos\AutoGen+Checker\AutoGen+Checker\Live_check.txt'
    file = open('Live_check.txt', 'a')
    file.write(str(content) + "\n")
    file.close()

    time.sleep(10)
    # driver.find_element_by_id("tvmit_live").click()
    # act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

    
    # Copy - Solution was easier than this xd. Sometimes I'm idiot sheesh
    # act = ActionChains(driver)
    # act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

i = 1
n = 10

while i <= n:
    gen()
    i=i+1

# driver.quit()