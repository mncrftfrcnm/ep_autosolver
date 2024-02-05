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
    t = driver.find_element(By.ID, value='loginId').send_keys(input('ENTER YOUR MAIL'))
    t = driver.find_element(By.ID, value='password').send_keys(input('ENTER YOUR PASSWORD'))
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
    driver.get("https://app.educationperfect.com/app/Spanish/2568316/1938169/activity-starter?task=9281326")



    driver.switch_to.window(driver.window_handles[0])

    # Perform actions on the first window if needed


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
    for x in driver.find_elements(By.XPATH, "//span[@class='abb-label']"):
        driver.execute_script("arguments[0].click();", x)      
    while True:
        qe = 0
        
        question = driver.find_element(By.ID, 'question-container-group').text
        if question in questions:
            print(f"//span[text()={questions[question]}]")
            xpath_expression = "//span[text()='{}']".format(questions[question])
            tre = driver.find_elements(By.CLASS_NAME, "highlight-token")
            answer = questions[question]
            for x in tre:
                if x.text.lower() == answer:
                    driver.execute_script("arguments[0].click();", x)
            button = driver.find_element(By.XPATH, "//button[contains(., 'Submit')]")

            driver.execute_script("arguments[0].click();", button)
            first_span = driver.find_element(By.XPATH, "//span[@class='abb-label']")
            for x in driver.find_elements(By.XPATH, "//span[@class='abb-label']"):
                driver.execute_script("arguments[0].click();", x)

        else:
            button = driver.find_element(By.XPATH, "//button[contains(., 'Submit')]")

            driver.execute_script("arguments[0].click();", button)
            first_span = driver.find_element(By.XPATH, "//span[@class='abb-label']")
            for x in driver.find_elements(By.XPATH, "//span[@class='abb-label']"):
                driver.execute_script("arguments[0].click();", x)
            print('ppp')
            time.sleep(4)
            
            try:
                answer = driver.find_element(By.XPATH, "//span[@class='highlight-token missing']").text
            except:
                first_span = driver.find_element(By.XPATH, "//span[@class='abb-label']")
                for x in driver.find_elements(By.XPATH, "//span[@class='abb-label']"):
                    driver.execute_script("arguments[0].click();", x)           
            try:
                answer = driver.find_element(By.XPATH, "//span[@class='highlight-token missing']").text
            except:
                print('this is multichoice or other')
            print(answer)
            if re.fullmatch(r"\s*", answer):
                first_span = driver.find_element(By.XPATH, "//span[@class='abb-label']")
                for x in driver.find_elements(By.XPATH, "//span[@class='abb-label']"):
                    driver.execute_script("arguments[0].click();", x)                
                answer = driver.find_element(By.XPATH, "//span[@class='highlight-token missing']").text
                print(answer)
            questions[question] = answer
            
            time.sleep(5)
            

            for x in driver.find_elements(By.XPATH, "//span[@class='abb-label']"):
                driver.execute_script("arguments[0].click();", x)
            
            
            # button = driver.find_element(By.XPATH, "//button[contains(., 'Submit')]")
            # driver.execute_script("arguments[0].click();", button)
            print('rrtrretter')
            
            
            # first_span = driver.find_element(By.XPATH, "//span[@class='abb-label']")
            # for x in driver.find_elements(By.XPATH, "//span[@class='abb-label']"):
            #     driver.execute_script("arguments[0].click();", x)



            # for x in driver.find_elements(By.XPATH, "//span[@class='abb-label']"):
            #     driver.execute_script("arguments[0].click();", x)  
            # time.sleep(3)      
            



 
        print('dsfsfsdfsdfsdfs')


main()