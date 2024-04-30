import requests
import pandas as pd
from bs4 import BeautifulSoup


def prod_details(link):
    print(f"=> scrapping link | {link}")
    url = link
    payload = {}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'cookie': 'session-id=258-7122708-6536819; session-id-time=2082787201l; i18n-prefs=GBP; sp-cdn="L5Z9:PK"; ubid-acbuk=260-3740334-8477447; session-token="yl0HAV4KIAIMvYIaTGnO3Txn/JQSWy7IpQwgCu7CtTlZuY4eYX1ni1+VviPOLvzgfS8xAgbcQaCs4dfOA22vMNoJdB4cVf5l5aM5rvO++Frj/uzpS8yk2oyvGdpFUHjlrcI8Yh7RJ6axNN764FhYgQpTAit8dbW8KZfp+OVLMREk2G+B3N1GBDMIqMO82niddJ7ke9WU1kR2q/dwfWmlxUKGXBvK3n/ZiUFM61N3n+W5XLbkKB0YRhPhMkxLV2Ys784kgTLHzBdgG+71ym1ZgnnWXF2T3RxVjCFgQJZpzLbAQspAx32+1+vDYpoL8+TvrwY/IgiF1lQS1hm8Bwguy2dNfbzb2fCj+mHr7UTxCZk="; csm-hit=tb:MSXESHCA2DGZVGKYZ2B2+s-756HSVQ86Z7X798DJG98|1714394232270&t:1714394232270&adb:adblk_no; session-token="C/Q3OKCrZhsIfQ/p92O54mJvJJMBzOt5WNhzn+luWshTrcKq2v3Id7RPBwJ3dL2q+NuOV0wrs+RwZy6l/lmbweCzkBs1/mmmFkX0oiejRHASKIB0tX0SCt56C3ELYQl6KsfDat4prQhCnc4c7lq9zbPuEnFGugRMyDot4luZhQJ0HM5clEcRzapx961IvVMxyJKcsPMjWnc1AgVvQrRKM5RblQbwZ2moYlHk/k4tW9W/TdP7RBkrcP+I4nNIiYsNVqkvLHVNYJtzv8I623209PBqsjloVhSreXiIvJdmHJOtVxSuTAScqcJy32N1pbiJQL3XxCjjuAlXS9cdA07WScSSq5QgPEH1hsaawabniWg="',
        'device-memory': '8',
        'downlink': '4.15',
        'dpr': '2',
        'ect': '4g',
        'priority': 'u=0, i',
        'rtt': '100',
        'sec-ch-device-memory': '8',
        'sec-ch-dpr': '2',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-ch-ua-platform-version': '"13.0.0"',
        'sec-ch-viewport-width': '1470',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'viewport-width': '1470'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = str(soup.find("span", {"id": "productTitle"}).getText()).strip()
    price = str(soup.find("span", {"class": "a-price-whole"}).getText()).strip()
    print(f"Title: {title} | Price: {price}")


def scrap_product(keyword):
    url = f"https://www.amazon.co.uk/s?k={keyword}&s=price-desc-rank"
    payload = {}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'cookie': 'session-id=258-7122708-6536819; session-id-time=2082787201l; i18n-prefs=GBP; sp-cdn="L5Z9:PK"; ubid-acbuk=260-3740334-8477447; session-token="DZBj0NRX5T4NvkM8xoKenaLoPdBCf9iLr9G7qJIWfcyoFJjUR+LwZxjuq9k1iin2+K1TKLq4c88FuCkKC1G3epwqa81ttavkzTma21Gqb6t41QixVWqyQxeLspkYvfYl+Kxt3wMFzrmcrU/N8EdeQrnhAZh4uyEL4Y5oqvnjd9mRX/qAuMfDELfBj5FK/71qWnyq6R6E047Hu+QyJu4eRnR6ovzwtsXzcjXlQ76CGYcrZoDHQXzItTPMt3rp+y+wKd5MMCcyQT5N8NeLrUiOc7jRkTHYG4hzy6Y5IWzstxGHRe8frWFYZLYxobZB6ib1yoFympeuWzVe+Xmv1lYgiZLCcXq4u4rgnhnQd9vgMYs="; csm-hit=tb:s-F6K08WRBWS0664AYDTRT|1714381331027&t:1714381331422&adb:adblk_no; session-token="C/Q3OKCrZhsIfQ/p92O54mJvJJMBzOt5WNhzn+luWshTrcKq2v3Id7RPBwJ3dL2q+NuOV0wrs+RwZy6l/lmbweCzkBs1/mmmFkX0oiejRHASKIB0tX0SCt56C3ELYQl6KsfDat4prQhCnc4c7lq9zbPuEnFGugRMyDot4luZhQJ0HM5clEcRzapx961IvVMxyJKcsPMjWnc1AgVvQrRKM5RblQbwZ2moYlHk/k4tW9W/TdP7RBkrcP+I4nNIiYsNVqkvLHVNYJtzv8I623209PBqsjloVhSreXiIvJdmHJOtVxSuTAScqcJy32N1pbiJQL3XxCjjuAlXS9cdA07WScSSq5QgPEH1hsaawabniWg="',
        'device-memory': '8',
        'downlink': '6.3',
        'dpr': '2',
        'ect': '4g',
        'priority': 'u=0, i',
        'rtt': '100',
        'sec-ch-device-memory': '8',
        'sec-ch-dpr': '2',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-ch-ua-platform-version': '"13.0.0"',
        'sec-ch-viewport-width': '1470',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'viewport-width': '1470'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    main_div = soup.find("div", {"class": "s-main-slot s-result-list s-search-results sg-row"})
    for each in main_div.find_all("div", {"data-component-type": "s-search-result"}):
        a_tag = each.find("a", {"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})
        if a_tag is not None:
            link = f"https://www.amazon.co.uk/{a_tag["href"]}"
            prod_details(link)


if __name__ == '__main__':
    scrap_product("laptop")
