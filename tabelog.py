from bs4 import BeautifulSoup
import requests
import csv
import random

jinbo_url = "https://tabelog.com/tokyo/A1310/A131003/rstLst/"
ocha_url  = "https://tabelog.com/tokyo/A1310/A131002/R2080/rstLst/"
list_usl  = "?SrtT=rt&Srt=D&sort_mode=1"

def read_csv(f_name):
    csv_file = open("list.csv", "r", encoding="utf_8", errors="", newline="" )
    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\n", quotechar='"', skipinitialspace=True)
    return f

def make_url(csv_list, town, food):
    req_url = ""
    for i in csv_list:
        if i[0] == food:
            req_url = town + i[1] + "/" +list_usl
    return req_url

def scrape_list(list_url):
    """
    一覧ページのパーシング
    """
    shop_list = []
    r = requests.get(list_url)
    if r.status_code != requests.codes.ok:
        return False
    soup = BeautifulSoup(r.content, 'lxml')
    soup_a_list = soup.find_all("a", class_="list-rst__rst-name-target")
    if len(soup_a_list) == 0:
        return False
    for soup_a in soup_a_list:
        item_url = soup_a.get("href")
        shop_list.append(item_url)
    return shop_list

def get_shop_list(erea, food):
    data = read_csv('list.csv')
    tabelogu_url = ""
    if erea == "神保町":
        tabelogu_url = make_url(data, jinbo_url, food)
    elif erea == "御茶ノ水":
        tabelogu_url = make_url(data, ocha_url, food)
    rank_list = scrape_list(tabelogu_url)
    return rank_list[random.randint(0,4)]
