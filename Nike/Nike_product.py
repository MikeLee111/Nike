import requests
import json
import re
import requests
from bs4 import BeautifulSoup
import regex as re
import os

url = "https://www.nike.com.cn/w/"

headers = {
    "authority": "www.nike.com.cn",
    "method": "GET",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "max-age=0",
    "referer": "https://wx.mail.qq.com/",
    "sec-ch-ua": '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
    "sec-ch-ua-full-version-list": '"Chromium";v="136.0.7103.113", "Microsoft Edge";v="136.0.3240.92", "Not.A/Brand";v="99.0.0.0"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"19.0.0"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
    "cookie": "cdn_sec_tc=ddcc169917484941392406312e02fe1735f922fcc32d7e7740ac6ede14; acw_tc=1a0c639f17484941393617823e006e8cc265636ccf5e03c8971180148fc337; geoloc=cc=CN; sajssdk_2015_cross_new_user=1; anonymousId=DSWX315192F4FFBD02007CC9990DED60D48A; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22DSWX315192F4FFBD02007CC9990DED60D48A%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwx.mail.qq.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk3MWE1ZjQwZmUxM2ZlLTAxYTFhZDQzZWE1ZTQwYy00YzY1N2I1OC0xODIxMzY5LTE5NzFhNWY0MGZmMWI1ZCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221971a5f40fe13fe-01a1ad43ea5e40c-4c657b58-1821369-1971a5f40ff1b5d%22%7D; ppd=pw|nikecom>pw>no%20page%20title; sensorsdata2015jssdksession=%7B%22session_id%22%3A%221971a5f465d20750a6da6cdc8840a4c657b5818213691971a5f465e242e%22%2C%22first_session_time%22%3A1748494141020%2C%22latest_session_time%22%3A1748494153576%7D; tfstk=gLcnNrNVTvyBbDxTBfNB3JKCPmp9OWN7p0C827EyQlr1vMCKzYAoYm2r9W3KIumgfMEEZ41uz4oWRuLBB2gQN7-vD7AxR2M_u5lHX78r77UlCK3rW2gQNNwcNfXxRa4Vc2wUa0Pabzz7aT5PLFVaPzNPT85FQGr_b7zUak7aQzzRay5r4V8gPlrza7ozQF4Sp0W7mDix_hFSRuCoQmcg-JqqSK1lafCYKouUj_--syAQ02rGa_q06NeIS2KhGVFI7m4xvC5nmqGsjPo2ZhVSfYozrcRf2WMxAjwi5K5ZWWq_3rlwzsr-tA34jSbyTVV3x-lLLZCx0V0rHRc9uIN3Tkk8O4QDvVcnv2GiyaWatWHgnXV2GMr-BqcurbtWsm0j1c4Z0QxF4TXN3gtVNP8-_T67LPagDKO_WFs381WkSFXX_Jz_RCYMST67LPagDFYG3OyU5yOG.; ssxmod_itna=YqRxBDcGoCqQwxBPGKiQ23k8IeMWxOY870xqGX3mYDZDiqAPGhDC33zqDKbZxe1K7G4BEQSKFr5DkKtA+woff7i53LlUDB3DEx0=5wfjQ4GGfxBYDQxAYDGDDp8Dj4ibDYfzODjBItzZCq=D3qDwDB=DmqG2Kn=Dm4DfDDdyCGo1CT=D4qDBDGUqMWiDG4Gf+T5D0TvFZxhpnxGWCMtUbC0PVnhMfA4yD0tDIqGXiGBQMjBwcEXMBcHOrx6qNeGuDG=5LuLPx0pB/dXRmpeEK7+YBODoiiP5ARq1C7En1Bb1Yi5eYB/Y7GoqGxqYFEM4Or1mbo5Q4tiDD===; ssxmod_itna2=YqRxBDcGoCqQwxBPGKiQ23k8IeMWxOY870xA6uNDkDBuxDK7GaYfILfYYCx8xO9XOq8rLy=56S=YAwh319kRjm5qzwBRLWh9lErj1ctrg=8OO9uOauNcf63T8aWI9oOLvLXpZFn/dkKZzwE/A2iC9uf/j4X9AT=XQ7XqqC2+DWL36SbtqM6NkMNB4C0n3W2iPmdN1k36KPodVQ3a63L81MIkaSaOkPbGSCyNPKa=TWfG74Ngbtfw1tdwc1cEHIasOaBs1UfCkzaY=DMoP8BareRCrQtLEmd8KWWBkXWFkuzi2NZO1uMMEN+ZQ/BXVQY9p3Fgjca0ZPLf=AH1j514DQKQ8xDFqD+pr70DeBDHWx5YD==="
}

response = requests.get(url, headers=headers)

# # 打印状态码和内容摘要
# print("状态码:", response.status_code)
# print("响应内容前500字：\n", response.text[:500])
# print(response.text)
# # print(json.loads(response.text))
# 保存响应内容为 HTML 文件
# with open("response.html", "w", encoding="utf-8") as f:
#     f.write(response.text)
#
# print("已保存 HTML 内容为 response.html，请用浏览器打开查看。")

html = response.text
def get_details_from_product_page(url):
    # print(f"访问详情页URL: {url}")  # 调试用
    print(f"爬取一条商品详情页URL: {url}")  # 调试用

    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'lxml')

        # --- 1. 提取“鞋内长”尺码 ---
        size_fit_details = soup.find('details', id='pdp-info-accordions__size-fit-accordion')
        size_texts = []
        if size_fit_details:
            size_ul = size_fit_details.select_one('ul.css-1vql4bw.eru6lik0.nds-list')
            if size_ul:
                paragraphs = size_ul.find_all('p')
                for p in paragraphs:
                    text = p.get_text(strip=True)
                    if ":" in text and "鞋内长" in text:
                        size_texts.append(text)

        shoe_sizes = [text.split(":")[0].strip() for text in size_texts]

        # --- 2. 提取衣服尺码（从页面中的 JSON） ---
        clothes_sizes = []
        scripts = soup.find_all('script')
        for script in scripts:
            if script.string and '"sizes"' in script.string and '"gtin"' in script.string:
                try:
                    # 用递归匹配，提取 "sizes": [...] 完整内容（包括嵌套）
                    sizes_match = re.search(r'"sizes"\s*:\s*(\[(?:[^\[\]]|(?1))*\])', script.string, re.DOTALL)
                    if sizes_match:
                        sizes_json_str = sizes_match.group(1)

                        # 打印调试，看看实际截取的字符串内容
                        # print("截取的 sizes JSON 字符串:", sizes_json_str)

                        # 直接尝试用json加载，理论上这里无需再补全
                        clothes_sizes_json = json.loads(sizes_json_str)
                        clothes_sizes = [size.get("label") for size in clothes_sizes_json if "label" in size]
                        break
                except json.JSONDecodeError as e:
                    print(f"JSON解析错误: {e}")
                    # 如果你愿意，可以使用 demjson 容错解析
                    # import demjson
                    # clothes_sizes_json = demjson.decode(sizes_json_str)

        # --- 3. 提取页面其他列表项（如尺码表） ---
        detail_lis = soup.select('ul.css-1vql4bw.eru6lik0.nds-list li')
        detail_li_text = "\n".join(li.get_text(strip=True) for li in detail_lis) if detail_lis else ''

        # --- 4. 合并说明 ---
        combined_details = "\n".join(size_texts + ([detail_li_text] if detail_li_text else []))

        # 合并鞋尺码和衣服尺码
        all_sizes = shoe_sizes + clothes_sizes

        return all_sizes, combined_details

    except Exception as e:
        print(f"详情页解析失败: {e}")
        return [], ""

def scrape_products():
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    product_cards = soup.select('.product-card')
    results = []

    for card in product_cards:
        try:
            title = card.select_one('.product-card__title')
            subtitle = card.select_one('.product-card__subtitle')
            price = card.select_one('.product-price')
            color = card.select_one('.product-card__product-count')
            link_tag = card.select_one('a[href*="/t/"]')
            img_tag = card.select_one('img.product-card__hero-image')

            href = link_tag['href'] if link_tag else ''
            if href.startswith('http'):
                product_url = href
            else:
                product_url = f"https://www.nike.com.cn{href}"

            sku_match = re.search(r'/([A-Z0-9]+-\d+)', href) if href else None
            sku = sku_match.group(1) if sku_match else ''

            sizes, details = get_details_from_product_page(product_url)

            results.append({
                "title": title.text.strip() if title else '',
                "price": price.text.strip() if price else '',
                "color": color.text.strip() if color else '',
                "sku": sku,
                "size": sizes,
                "details": details,
                "img_urls": img_tag['src'] if img_tag else '',
                "url": product_url
            })
        except Exception as e:
            print(f"解析失败: {e}")

    return results


def fetch_products_from_api(url):
    headers = {
        ":authority": "api.nike.com.cn",
        ":method": "GET",
        ":path": "/cic/browse/v2?queryid=products&anonymousId=DSWX315192F4FFBD02007CC9990DED60D48A&country=cn&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(CN)%26filter%3Dlanguage(zh-Hans)%26filter%3DemployeePrice(true)%26anchor%3D48%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=zh-Hans&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%94%20%7BhighestPrice%7D",
        ":scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cookie": "geoloc=cc=CN; sajssdk_2015_cross_new_user=1; anonymousId=DSWX315192F4FFBD02007CC9990DED60D48A; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22DSWX315192F4FFBD02007CC9990DED60D48A%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk3MWE1ZjQwZmUxM2ZlLTAxYTFhZDQzZWE1ZTQwYy00YzY1N2I1OC0xODIxMzY5LTE5NzFhNWY0MGZmMWI1ZCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221971a5f40fe13fe-01a1ad43ea5e40c-4c657b58-1821369-1971a5f40ff1b5d%22%7D; ppd=pdp|nikecom>pdp>nikecourt%20slam; ssxmod_itna=iqGx97i=KGqeqBK0QDXKt8C0KGCbie15KWbeatDlgmixA5D8D6DQeGTWukeWDRi0H44QGA87fiK1C0YwGjClWPxfOADB3DEx0=o/RW4iiyDCeDIDWeDiDGR=DFxYoDeoHQDFF5X/ZcpxAQDQ4GyDitDKq0cDi3DA4DjFMeqY76uDYQDGqDSYWuVDD3DfR=4DDN4W=APYDGWFwt6QeiegW4SC0hcD0tDIqGXbD7dcQBhoiNS0aHHaEQ4oeGuDG6Ppwdex0PyBut2CZvxW2vxAA5s7G+e7r4ESADoQ0Cotre4bAwSEYeqlx4sWouhxYCP4e3IGhzYxxD==; ssxmod_itna2=iqGx97i=KGqeqBK0QDXKt8C0KGCbie15KWbebD6p4cbDYqxDsKboDLmesNl3cZ4+qOD8226wK3zlYeOeUx=2TmgFzMpaA55CPfefCX3hycwT=F1S9ReutBIbAs5sqjkMFTTK=TMPu4v/fStRSBKvYbieqMXZ8q559fd+tnxB+AYYiRGkSAY/+LYQNq0k7BnLRbolGwcund09QeLH8C6fS4fjDw6zaL2NOMbfl0b4YzURt3=CyTIjY+NAwSXAdpQEHUSUGqXEt+tCY4UU4XQXdZSVKs8pv8T6M/IXpgC0iarL8VXqo8uEiKA7ULoPOQtBDK5mXd2AH0jPSoM16bh0pptBDUfOd5irLm6e3qVhfEe=zobSrbfZjBcEUmPSno+nEbbXyYwlrTflQVoYMrXwCvqox5iIzQGH1mk8e4jPIGKC7iyGfT8eRmm+eo5OorpKSiUf=AXzUem4DQ9QD08DijOjiqnx+UKqBGeYD===; acw_tc=1a0c652217484999584107765e007d169485e479b7a13cc7b66a1d64d47d35; sensorsdata2015jssdksession=%7B%22session_id%22%3A%221971a5f465d20750a6da6cdc8840a4c657b5818213691971a5f465e242e%22%2C%22first_session_time%22%3A1748494141020%2C%22latest_session_time%22%3A1748499964120%7D; tfstk=ge4ZwX1XZNQN-Pktjyg2LI81SHuTOqWWgrMjiSVm1ADM5F90YJyZ5lNcB-zqL-njIFgM6ke7ZFa1XqTqWq3cFT_5P5NtkqqSR8zsBWVKi6Gi9QZUbq3cF9NrHKBikRvGALN0t6ljMFYgnc0nxjMnsKm0nvmnZb9io-2mtDctaKvijmxH-vhmox2mo6unpjumnxi4B-pSZcfYhlOpbMO1fYNiLEY0SZniU3DK9XUE_ckof5YmcylZbYVazQn0GX4Q80iBGg33wkwiT47Bj4VUm8ruHgtK7SqgHDyOpHkQxPFmnDODPWPzsu03lsA-YJcqqqmeiEVEWvmbS4bkLXE31o4TQI8m6PaS0YnFiEnj-ziuqRRAwW0ii-n8lTLtISV8yugPRh0uTo2z0gk6HXY5TrEwnnoi9Xk5T67e6Uyv-xzh6nKxx0cEF1nDDnni9Xk5T6-vDcLoTY1tm",
        "origin": "https://www.nike.com.cn",
        "priority": "u=1, i",
        "referer": "https://www.nike.com.cn/",
        "sec-ch-ua": '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0")
    }

    # 注意: requests库不支持以冒号开头的伪头部，:authority等可以忽略，
    # 它们是HTTP/2协议里的伪头部，requests只用HTTP/1.1，所以你只要设置正常的HTTP头即可。
    # 下面去掉这些伪头部，仅保留常规的HTTP头。

    clean_headers = {
        "accept": headers["accept"],
        "accept-encoding": headers["accept-encoding"],
        "accept-language": headers["accept-language"],
        "cookie": headers["cookie"],
        "origin": headers["origin"],
        "referer": headers["referer"],
        "sec-ch-ua": headers["sec-ch-ua"],
        "sec-ch-ua-mobile": headers["sec-ch-ua-mobile"],
        "sec-ch-ua-platform": headers["sec-ch-ua-platform"],
        "sec-fetch-dest": headers["sec-fetch-dest"],
        "sec-fetch-mode": headers["sec-fetch-mode"],
        "sec-fetch-site": headers["sec-fetch-site"],
        "user-agent": headers["user-agent"],
        "priority": headers["priority"]
    }

    response = requests.get(url, headers=clean_headers)
    response.raise_for_status()
    return response.json()

def extract_product_info(raw_data):
    print(f"爬取第二页商品数据")  # 调试用
    products = []
    try:
        raw_products = raw_data["data"]["products"]["products"]
        for item in raw_products:
            try:
                colorway = item["colorways"][0]
                price = colorway["price"]["currentPrice"]
                full_price = f"¥{price}"

                product_info = {
                    "title": item.get("title", ""),
                    "price": full_price,
                    "color": item.get("colorDescription", ""),
                    "sku": colorway.get("cloudProductId", ""),
                    "size": [],  # API 中未提供尺码信息，留空
                    "details": item.get("subtitle", ""),
                    "img_urls": colorway["images"].get("portraitURL", ""),
                    "url": "https://www.nike.com.cn" + colorway.get("pdpUrl", "").replace("{countryLang}", "")
                }
                products.append(product_info)
            except Exception as e:
                print(f"跳过一个商品，原因：{e}")
    except KeyError:
        print("原始数据结构异常")
    return products

def load_existing_json(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_data_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    products = scrape_products()

    # 保存成 JSON 文件
    with open("nike_products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

    print(f"共保存 {len(products)} 条商品数据到 nike_products.json")

    # 2. 调用接口获取数据
    url = ("https://api.nike.com.cn/cic/browse/v2?queryid=products&anonymousId=DSWX315192F4FFBD02007CC9990DED60D48A"
           "&country=cn&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(CN)%26filter%3Dlanguage(zh-Hans)%26filter%3DemployeePrice(true)%26anchor%3D48%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24"
           "&language=zh-Hans&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%94%20%7BhighestPrice%7D")
    api_data = fetch_products_from_api(url)
    # 2. 提取成标准格式
    formatted_products = extract_product_info(api_data)

    # # 3. 存储为 JSON 文件
    # save_data_to_json(formatted_products, 'nike_api_products.json')
    # print(f"第二页数据已格式化并保存，共 {len(formatted_products)} 条记录 -> nike_api_products.json")
    # 读取 nike_products.json 中原有数据并合并
    existing_data = load_existing_json("nike_products.json")
    combined_data = existing_data + formatted_products

    # 保存合并后的数据回 nike_products.json
    save_data_to_json(combined_data, "nike_products.json")
    print(f"第二页数据已格式化并保存，共 {len(combined_data)} 条记录 -> nike_products.json")