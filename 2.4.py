from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser.find_element_by_css_selector("button.btn").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    time.sleep(2)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    browser.find_element_by_css_selector("#answer").send_keys(y)

    but = browser.find_element_by_css_selector("button.btn")
    but.click()

finally:
    time.sleep(10)
    browser.quit()