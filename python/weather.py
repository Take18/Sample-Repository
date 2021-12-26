import sys
import requests
from bs4 import BeautifulSoup

def show_forecast(dl):
    print(dl.dt.contents[0]+"の天気\n")
    print(dl.dd.contents[1].img.attrs['alt'])
    print("最高気温は"+dl.dd.contents[3].contents[0].contents[0]+"度")
    print("最低気温は"+dl.dd.contents[3].contents[2].contents[0]+"度")
    print("降水確率は"+dl.dd.contents[5].contents[0])


if len(sys.argv) == 1:
    print("都市が指定されていません。")
    exit()
city_name = sys.argv[1]

url='https://weather.yahoo.co.jp/weather/'
res=requests.get(url)
soup=BeautifulSoup(res.text,"html.parser")

dl = False

# 最初のページに指定された都市があるか確認
city_names = soup.select("#map li.point > a > dl > dt.name")
for city in city_names:
    if city_name == city.contents[0]:
        dl = city.parent

if dl == False:
    # 各ページのリンク取得
    hrefs = map(lambda a: a.attrs['href'], soup.select("#map li.point > a"))

    # 取得したページの中に指定された都市があるか確認
    for href in hrefs:
        res=requests.get("https://weather.yahoo.co.jp"+href)
        soup=BeautifulSoup(res.text,"html.parser")
        city_names = soup.select("#map li.point > a > dl > dt.name")
        for city in city_names:
            if city_name == city.contents[0]:
                dl = city.parent

if dl == False:
    print("指定された都市が見つかりませんでした。")
    exit()

show_forecast(dl)
