import requests
import pandas as pd
from bs4 import BeautifulSoup

out_put = {
    "title": [],
    "price": [],
    "description": [],
    "image": [],

}


def get_book_details(link):
    print(f"=> Getting book | {link}")
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'html.parser')
    article = soup.find("article")
    div = article.find("div", {"class": "col-sm-6 product_main"})
    book_title = div.find("h1").getText()
    book_price = div.find("p", {"class": "price_color"}).getText()
    book_img = article.find("img")["src"]
    all_p_tags = article.find_all("p")
    book_desc = str(all_p_tags[3].getText()).strip()

    out_put["title"].append(book_title)
    out_put["price"].append(book_price)
    out_put["description"].append(book_desc)
    out_put["image"].append(str(book_img).replace("../..", "https://books.toscrape.com/"))


def get_books_links():
    for x in range(50):
        page = f'https://books.toscrape.com/catalogue/page-{x+1}.html'
        page = requests.get(page)
        soup = BeautifulSoup(page.text, 'html.parser')
        section = soup.find("section")
        ol = section.find("ol")
        for each in ol.find_all("li"):
            href = "https://books.toscrape.com/catalogue/"+str(each.find("a")["href"])
            get_book_details(href)

        df = pd.DataFrame(out_put)
        df.to_csv("books-output.csv")
        break


if __name__ == '__main__':
    get_books_links()