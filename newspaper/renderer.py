import asyncio
from pyppeteer import launch
import time

browser = None

async def render_js(url, headless=False, proxy=None, sleep=0.1):
    args = ['--no-sandbox']
    if proxy:
        args.append('--proxy-server=%s' % proxy)
    global browser
    if not browser:
        browser = await launch(headless=headless, ignoreHTTPSErrors=True, dumpio=True, args=args)
    page = await browser.newPage()
    await page.goto(url)
    if sleep:
        time.sleep(sleep)
    html = await page.content()
    await page.close()
    return html

def rendered_page(url, headless=True, proxy=None, sleep=0.1):
    loop = asyncio.get_event_loop()
    html = loop.run_until_complete(render_js(url, headless=headless, proxy=proxy, sleep=sleep))
    return html