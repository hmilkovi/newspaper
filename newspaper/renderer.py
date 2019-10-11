from selenium import webdriver
from fake_useragent import UserAgent
import time

ua = UserAgent()

def rendered_page(url, headless=False, proxy=None, sleep=0.1):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    global ua
    userAgent = ua.random
    chrome_options.add_argument(f'user-agent={userAgent}')
    if headless:
        chrome_options.add_argument('--headless')
    if proxy:
        chrome_options.add_argument('--proxy-server={}'.format(proxy))
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.set_window_size(1920, 1200)
    driver.get(url)
    time.sleep(sleep)
    html = driver.page_source
    time.sleep(0.5)
    driver.quit()
    return html