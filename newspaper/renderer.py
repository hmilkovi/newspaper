from selenium import webdriver
import time

def rendered_page(url, headless=False, proxy=None, sleep=0.1):
    chrome_options = webdriver.ChromeOptions()
    if headless:
        chrome_options.add_argument('--headless')
    if proxy:
        chrome_options.add_argument('--proxy-server={}'.format(proxy))
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    time.sleep(sleep)
    html = driver.page_source
    time.sleep(0.5)
    driver.quit()
    return html