from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.action_chains import ActionChains
questions = {}

def login(driver):
    t = driver.find_element(By.ID, value='loginId').send_keys('diab230234@diabstudents.com')
    t = driver.find_element(By.ID, value='password').send_keys('MenyaZovutVova%5')
    t =  driver.find_element(By.ID, value='password').send_keys(Keys.ENTER)
    return t
def start_lesson(driver):
    while True:
        try:
            t= driver.find_element(By.ID, 'resume-icon').click()
        except:
            pass
        else:
            break
    time.sleep(5)

def extract_text(driver):
    pattern = re.escape('sections done') + r'(.*)'
    match = re.search(pattern, driver.find_element(By.XPATH, "/html/body").text, re.DOTALL)

    if match:
        result = match.group(1)
        return result.replace('''
You don't have focus on this window.
Click the button to continue.
Continue''', '').replace('''You don't have focus on this window.
Click the button to continue.
Continue''', '')
    else:
        return ""    
def get_answer(question):
    pass
def main():
    driver = webdriver.Chrome()
    driver.get("https://app.educationperfect.com/app/Mathematics/6658155/1707863/activity-starter?task=9288630")
    while True:
        try:
            login(driver)
        except:
            pass
        else:
            break
    while True:
        try:
            start_lesson(driver) 
        except:
            pass
        else:
            break
    while True:
        
        question = driver.find_element(By.XPATH, '//*[@id="question-container-group"]/div/div/div').text
        print(question)
        lines = question.split("\n")
        non_empty_lines = [line for line in lines if line.strip() != ""]
        result_string = "\n".join(non_empty_lines)
        question = result_string.split('\n')[0]
        if not question in questions:
            

            button = driver.find_element(By.XPATH, "//button[contains(., 'Submit')]")

            driver.execute_script("arguments[0].click();", button)
            first_span = driver.find_element(By.XPATH, "//span[@class='abb-label']")
            for x in driver.find_elements(By.XPATH, "//span[@class='abb-label']"):
                driver.execute_script("arguments[0].click();", x)
            


            for x in driver.find_elements(By.XPATH, "//span[@class='abb-label']"):
                driver.execute_script("arguments[0].click();", x)
            time.sleep(0.1)
            
            button = driver.find_element(By.XPATH, "//button[contains(., 'Submit')]")
            driver.execute_script("arguments[0].click();", button)
            first_span = driver.find_element(By.XPATH, "//span[@class='abb-label']")
            for x in driver.find_elements(By.XPATH, "//span[@class='abb-label']"):
                driver.execute_script("arguments[0].click();", x)



            for x in driver.find_elements(By.XPATH, "//span[@class='abb-label']"):
                driver.execute_script("arguments[0].click();", x)        
            
            
        else:
            print('i saw you alredy. your answer is', questions[question])
            button_text = questions[question]
            button_xpath = f"//button[text()='{button_text}']"
            button_element = driver.find_elements(By.XPATH, '//*[@id="question-container-group"]/div/div/div/div[2]')
            print(but.text for but in button_element)


            break
            button = driver.find_element(By.XPATH, "//button[contains(., 'Submit')]")

            driver.execute_script("arguments[0].click();", button)
            first_span = driver.find_element(By.XPATH, "//span[@class='abb-label']")
            for x in driver.find_elements(By.XPATH, "//span[@class='abb-label']"):
                driver.execute_script("arguments[0].click();", x)
            


            for x in driver.find_elements(By.XPATH, "//span[@class='abb-label']"):
                driver.execute_script("arguments[0].click();", x)
            time.sleep(0.1)
            
            button = driver.find_element(By.XPATH, "//button[contains(., 'Submit')]")
            driver.execute_script("arguments[0].click();", button)
            first_span = driver.find_element(By.XPATH, "//span[@class='abb-label']")
            for x in driver.find_elements(By.XPATH, "//span[@class='abb-label']"):
                driver.execute_script("arguments[0].click();", x)



            for x in driver.find_elements(By.XPATH, "//span[@class='abb-label']"):
                driver.execute_script("arguments[0].click();", x)        
            print('wrote!')
            time.sleep(4)

            button = driver.find_element(By.XPATH, "//button[contains(., 'Submit')]")

            driver.execute_script("arguments[0].click();", button)
            first_span = driver.find_element(By.XPATH, "//span[@class='abb-label']")
            for x in driver.find_elements(By.XPATH, "//span[@class='abb-label']"):
                driver.execute_script("arguments[0].click();", x)



            

            continue
        correct = driver.find_element(By.CSS_SELECTOR, ".correct").text
        questions[question] = correct
        print(questions)
        print('ghjj')
        time.sleep(4)

        button = driver.find_element(By.XPATH, "//button[contains(., 'Submit')]")

        driver.execute_script("arguments[0].click();", button)
        first_span = driver.find_element(By.XPATH, "//span[@class='abb-label']")
        for x in driver.find_elements(By.XPATH, "//span[@class='abb-label']"):
            driver.execute_script("arguments[0].click();", x)




 
        print('dsfsfsdfsdfsdfs')


main()