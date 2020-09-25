import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

correct_value = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
browser.find_element_by_css_selector("#book").click()
x = browser.find_element_by_css_selector('#input_value').text
answer_text_field = browser.find_element_by_css_selector('#answer')
submit_btn = browser.find_element_by_css_selector('[type="submit"]')

answer = str(math.log(abs(12*math.sin(int(x)))))
answer_text_field.send_keys(answer)
submit_btn.click()
