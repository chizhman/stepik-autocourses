from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    browser.find_element_by_css_selector("#answer").send_keys(y)

    chb = browser.find_element_by_css_selector("#robotCheckbox")
    chb.click()
    flag = browser.find_element_by_css_selector("[for='robotsRule']")
    flag.click()

    but = browser.find_element_by_css_selector("button.btn")
    but.click()

finally:
    time.sleep(10)
    browser.quit()