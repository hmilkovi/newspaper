from selenium import webdriver
import time
import os

SELENIUM_HUB = os.environ.get('HUB', None)

def rendered_page(url, headless=False, proxy=None, sleep=0.1):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    userAgent = 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0'
    chrome_options.add_argument(f'user-agent={userAgent}')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--disable-javascript")
    chrome_options.add_argument("--window-size=1920, 1200")
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--disable-dev-shm-usage')
    if headless:
        chrome_options.add_argument('--headless')
    if proxy:
        chrome_options.add_argument('--proxy-server={}'.format(proxy))
    if SELENIUM_HUB:
        driver = webdriver.Remote(command_executor=SELENIUM_HUB)
    else:
        driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(sleep)
    if 'One more step' in driver.page_source:
        driver.quit()
        return rendered_page(url, headless, None, sleep)
    html = driver.page_source
    time.sleep(0.5)
    driver.quit()
    return html

if __name__ == "__main__":
    rendered_page('https://telegraf.com.ua/ukraina/mestnyiy/5237623-rossiya-provodit-masshtabnyie-ucheniya-v-chernom-more.html', proxy='http://127.0.0.1:8119', sleep=10)