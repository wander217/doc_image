# from html2image import Html2Image
#
# hti = Html2Image()
# hti.screenshot(url='https://www.python.org',
#                save_as='python_org.png')
import asyncio
from pyppeteer import launch

data = {
    "department": {
        "content": "Sở kế hoạch và đầu tư tỉnh ABCADADS".upper(),
        "label": "OTHER"
    },
    "nation": {
        "content": "Cộng hòa xã hội chủ nghĩa Việt Nam".upper(),
        "label": "OTHER"
    },
    "room": {
        "content": "phòng đăng ký kinh doanh".upper(),
        "label": "OTHER"
    },
    "slogan": {
        "content": "Độc lập - Tự do - Hạnh phúc",
        "label": "OTHER"
    },
    "company_code": {
        "content": "0123S312312",
        "label": "COMPANY_CODE"
    },
    "first_register_date": {
        "content": "Đăng ký lần đầu, Thứ 3 ngày 28 tháng 6 năm 2022",
        "label": "REGISTER_DATE"
    },
    "second_register_date": {
        "content": "Đăng ký lần thứ 2, Thứ 3 ngày 28 tháng 6 năm 2022",
        "label": "REGISTER_DATE"
    },
    "vietnamese_company_name": {
        "content": "Tên công ty viết bằng tiếng Việt (ghi bằng chữ in hoa): Công ty ABC",
        "label": "VIETNAMESE_COMPANY_NAME"
    },
    "foreign_company_name": {
        "content": "Tên công ty viết bằng tiếng nước ngoài (nếu có): ABC Company " + "ABCD " * 15,
        "label": "FOREIGN_COMPANY_NAME"
    },
    "short_company_name": {
        "content": "Tên viết tắt (nếu có): ABC",
        "label": "SHORT_COMPANY_NAME"
    },
    "company_address": {
        "content": "Số 9, TDP ABC, ABCDDEERR, DSAHDAD, ĐẠASDADASD",
        "label": "SHORT_COMPANY_NAME"
    }
}


async def main():
    browser = await launch()
    page = await browser.newPage()
    with open(r'D:\python_project\doc_image\doc\test.html', 'r', encoding='utf-8') as f:
        html = f.read()
    for key, value in data.items():
        code = "${" + key + "}"
        html = html.replace(code, value['content'])
    with open(r'D:\python_project\doc_image\doc\test1.html', 'w', encoding='utf-8') as f:
        f.write(html)
    await page.goto(r'D:\python_project\doc_image\doc\test1.html')
    await page.setViewport({
        "width": (960 - 22),
        "height": 1280
    })
    print(len("Tên công ty viết bằng tiếng nước ngoài (nếu có): ABC Company " + "abcd " * 10))
    await page.screenshot({'path': 'example.png', 'fullPage': 'true'})
    element = await page.JJ('#foreign_company_name')
    for item in element:
        bbox = await item.boundingBox()
        content = await item.getProperty("innerHTML")
        value = await content.jsonValue()
        print(bbox, value.strip())

    # print(title)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
