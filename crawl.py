from utils import *
from book import Book, HEADER
import csv
from tqdm import tqdm

dict_csd = []
dict_td = []


def main():
    no_page = 15
    web_url = "https://tiki.vn/cham-soc-da-mat/c1582?src=tree&page=$PAGE"
    # web_url = "https://www.watsons.vn/1010-deal-hot-th%C3%A1ng-10/c/1000000083?q=%3AigcBestSeller&page=$PAGE"
    #wbe_url = "https://www.watsons.vn/1010-deal-hot-th%C3%A1ng-10/c/1000000083?q=%3AigcBestSeller&page=$PAGE&resultsForPage=64&text=&sort=&deliveryType="
    csv_file = open("crawled.csv", "w")
    csv_writer = csv.writer(csv_file)
    # csv_writer.writerow(HEADER)
    n = 0
    for page in range(1, no_page + 1):
        soup = crawl_page(page, web_url=web_url)
        if n == 200:
            break
        for comp in soup.findAll('div', {'class': 'product-item '}):
            book = Book(comp, "Chăm sóc da mặt")
            if book.category not in dict_csd:
                dict_csd.append(book.category)
            if book.name == None:
                continue
            book.write_csv(csv_writer)
            # book.show()
            n += 1
            print(n)
            if n == 200:
                break

    web_url = "https://tiki.vn/trang-diem/c1584?src=c.1584.hamburger_menu_fly_out_banner&_lc=&page=$PAGE"
    for page in range(1, no_page + 1):
        soup = crawl_page(page, web_url=web_url)
        for comp in soup.findAll('div', {'class': 'product-item '}):
            book = Book(comp, "Trang điểm")
            if book.category not in dict_td:
                dict_td.append(book.category)
            if book.name == None:
                continue
            book.write_csv(csv_writer)
            # book.show()
            n += 1
            print(n)
            if n == 400:
                return


if __name__ == '__main__':
    main()
    print(dict_csd)
    print(dict_td)
