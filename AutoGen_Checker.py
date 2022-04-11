from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from undetected_chromedriver import Chrome
import undetected_chromedriver.v2 as uc

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = Chrome()
driver = uc.Chrome(use_subprocess=True)

import time


bin_list = ['417849xxxxxxxxxx', '440393xxxxxxxxxx', '520737xxxxxxxxxx', '526879xxxxxxxxxx', '409602xxxxxxxxxx',
          '513483xxxxxxxxxx', '404942xxxxxxxxxx', '527680xxxxxxxxxx', '527684xxxxxxxxxx', '525500xxxxxxxxxx']
new_bin = []

def gen():
    url_gen = "https://technmind.com/ccgen/"
    url_check = "https://www.mrchecker.net/card-checker/ccn2/" 
             ### https://checker.visatk.com/ccn1/
             ### https://www.ontools.net/2022/04/cc-checker.html
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
    # driver.find_element_by_class_name("copytoclipboard_data").click()
    driver.find_element(By.CLASS_NAME, "copytoclipboard_data").click()
    
    ### Second Part ###
    driver.get(url_check)
    time.sleep(7)
    driver.find_element_by_class_name("form-control").click()
    act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    time.sleep(1)
    # driver.find_element_by_id("submit").click()
    driver.find_element(By.NAME,"valid").click()
    time.sleep(60)
    # element_to_store = driver.find_element_by_class_name("panel-body").text()
    # print(element_to_store)

    ######################## X Not working part X ########################
    driver.find_element(By.CSS_SELECTOR, ".panel-body.success")
    content = act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
    print(content)
    ######################## X Not working part X ########################

    ### Third Part ###
    # path = r'C:\Users\uzivatel 1\source\repos\AutoGen+Checker\AutoGen+Checker\Live_check.txt'
    file = open('Live_check.txt', 'a')
    file.write(str(content) + '\n')
    file.close()
    

    ### Bonus Part ###
    def virtualCards():
        driver.get(url_lookup)
        bin_list_2 = [417849, 440393, 520737, 526879, 409602, 513483,
                    526879, 409602, 513483, 404942, 527680, 527684, 525500]
        i = 0
        while (i < int(max(bin_list_2))):
            num = int(bin_list_2[i])
            num_str = str(num)
            eDigit = num_str[:8]
            driver.find_element(By.CLASS_NAME, "iin").click()
            act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
            # driver.find_element_by_name("iin").send_keys(eDigit)
            driver.find_element(By.CSS_SELECTOR, "input[value='4571 7360']").send_keys(eDigit)
            if (num == int(max(bin_list_2))):
                print("It works")
                exit(0)
            i = i + 1
            time.sleep(1)

    virtualCards()

    time.sleep(2)

gen()
