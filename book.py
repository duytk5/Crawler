from utils import *

# tên sp, ảnh
# giá, mô tả sp , 1 ảnh ở phần mô tả , danh mục,

HEADER = [
    "NAME",
    "IMAGE",
    "IMAGE_BIG",
    "PRICE",
    "DESC",
    "DESC_IMG",
    "CATEGORY",
    "CATEGORY_PAR"
]

def fix(st):
    st = st.replace("₫", "").replace(",", "").replace(">", "")
    st = str(st).strip()
    return st


def fix_desc(st):
    while st.find("<img") != -1:
        index = st.find("<img")
        ie = index
        while st[ie] != '>':
            ie += 1
        st = st[0:index] + st[ie + 1:]
    return st


class Book:
    def __init__(self, comp, cate):
        # print(comp)
        try:
            self.name = comp.get('data-title')
            self.category = fix(comp.get('data-category').split("/")[2])
            self.category_par = cate
            self.price = comp.get('data-price')
            self.image = comp.findAll('img', {'class': 'product-image img-responsive'})[0].get('src')
            self.href = comp.findAll('a')[0].get("href")
            nsoup = crawl_page(0, self.href)
            self.desc = fix_desc(str(nsoup.findAll('div', {'id': 'gioi-thieu'})[0]))
            if len(self.desc) > 10240:
                raise Exception
            try:
                self.desc_image = nsoup.findAll('div', {'id': 'gioi-thieu'})[0].findAll('a')[0].get('href')
            except:
                self.desc_image = "no-image"
            self.image_big = nsoup.findAll('img', {'id':'product-magiczoom'})[0].get("src")
            if self.image_big == "":
                self.image_big = "no-image"
        except:
            self.name = None
            self.image = None
            self.price = None
            self.desc = None
            self.desc_image = None
            self.category = None
            self.category_par = None
            self.image_big = None

    def show(self):
        val = self.get_list()
        for id in range(len(HEADER)):
            print(HEADER[id], ":", val[id])

    def get_list(self):
        return [self.name,
                self.image,
                self.image_big,
                self.price,
                self.desc,
                self.desc_image,
                self.category,
                self.category_par
                ]

    def write_csv(self, csv_file):
        csv_file.writerow(self.get_list())
