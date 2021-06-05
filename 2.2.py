from selenium import webdriver
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    inputs = browser.find_elements_by_css_selector(".form-group input")
    for i in inputs:
        got = i.send_keys("U wanna play?")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "text.txt")
    uploader = browser.find_element_by_css_selector("#file")
    uploader.send_keys(file_path)

    but = browser.find_element_by_css_selector("button.btn")
    but.click()

finally:
    time.sleep(10)
    browser.quit()