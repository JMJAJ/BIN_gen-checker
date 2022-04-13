from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from undetected_chromedriver import Chrome
import undetected_chromedriver.v2 as uc

driver = webdriver.Chrome(ChromeDriverManager().install())
driver = uc.Chrome(use_subprocess=True)

import time


bin_list = ['417849xxxxxxxxxx', '440393xxxxxxxxxx', '520737xxxxxxxxxx', '526879xxxxxxxxxx', '409602xxxxxxxxxx',
          '513483xxxxxxxxxx', '404942xxxxxxxxxx', '527680xxxxxxxxxx', '527684xxxxxxxxxx', '525500xxxxxxxxxx',
          '414718xxxxxxxxxx']
new_bin = []

def gen():
    url_gen = "https://technmind.com/ccgen/"
    url_check_a = "https://www.mrchecker.net/card-checker/ccn2/" 
    url_check_b = "https://checker.visatk.com/ccn1/"
    ############# "https://www.ontools.net/2022/04/cc-checker.html"
    url_lookup = "https://binlist.net"

    bin = "5438164124xxxxxx"
    act = ActionChains(driver)

    ### First Part ###
    driver.get(url_gen)
    driver.find_element_by_name("ccp").send_keys(new_bin)
    driver.find_element_by_name("ccghm").click()
    act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    driver.find_element_by_name("ccghm").send_keys(100)
    driver.find_element_by_id("generar").click()
    driver.find_element(By.CLASS_NAME, "copytoclipboard_data").click()
    
    print("With CloudFlare - 1\nWithout CloudFlare - 2")
    if (switch == 1):
        ### Second Part (A) ###
        driver.get(url_check_a)
        time.sleep(7)
        driver.find_element_by_class_name("form-control").click()
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        time.sleep(1)
        driver.find_element(By.NAME,"valid").click()
        time.sleep(60)
        # element_to_store = driver.find_element_by_class_name("panel-body").text()
        # print(element_to_store)
    else:                                             
        ### Second Part (B) ###
        driver.get(url_check_b)
        driver.find_element_by_class_name("form-control").click()
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        time.sleep(1)
        driver.find_element_by_id("submit").click()
        time.sleep(60)
        store = driver.find_element(By.XPATH, "//div[@id='tvmit_live']").text()

    ######################## X Not working part X ########################
    # driver.find_element(By.CSS_SELECTOR, ".panel-body.success")
    # content = act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
    # print(content)
    ######################## X Not working part X ########################

    ### Third Part ###
    file = open('Live_check.txt', 'a')
    file.write(str(content) + '\n')
    file.close()
    

    ### Bonus Part ###
    ### /Exaple2.py ###

    time.sleep(2)

gen()
