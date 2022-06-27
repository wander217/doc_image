# from html2image import Html2Image
#
# hti = Html2Image()
# hti.screenshot(url='https://www.python.org',
#                save_as='python_org.png')
import asyncio
from pyppeteer import launch


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto(r'D:\python_project\doc_image\doc\test.html')
    await page.screenshot({'path': 'example.png', 'fullPage': 'true'})
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
