import csv
import mysql.connector as mcon
import requests
from bs4 import BeautifulSoup
from datetime import datetime

cnx = mcon.connect(user='admin', password='admin',
                   host='127.0.0.1',
                   database='hathao')


with open('crawled.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    id = 0
    for row in csv_reader:
        try:
            id += 1
            name = row[0]
            image = row[1]
            image_big = row[2]
            price = row[3]
            desc = row[4]
            desc_image = row[5]
            category = row[6]
            category_par = row[7]


            cur = cnx.cursor()

            insert_stmt = (
                "INSERT INTO item ( name, image, image_big, price, desc_text, desc_img, category, category_par) "
                "VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"
            )

            data = (name, image, image_big, price, desc, desc_image, category, category_par)
            print(data, cur.execute(insert_stmt, data))
            cnx.commit()
        except:
            # print("cc")
            pass

    cnx.close()
