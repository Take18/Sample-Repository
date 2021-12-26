import io
import sys
import requests
from bs4 import BeautifulSoup

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.buffer,encoding='utf-8')
sys.stdin=io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8')

locations=sys.argv
url='https://weather.yahoo.co.jp/weather/'
res=requests.get(url)
soup=BeautifulSoup(res.text,"html.parser")

if len(locations)>1:

    for location in locations[1:]:

        if location=='札幌':
            
            elems_forecast_Sapporo=soup.select('#map > ul > li.point.pt1400 > a > dl > dd > p.icon > img')
            elems_temp_high_Sapporo=soup.select('#map > ul > li.point.pt1400 > a > dl > dd > p.temp > em.high')
            elems_temp_low_Sapporo=soup.select('#map > ul > li.point.pt1400 > a > dl > dd > p.temp > em.low')
            elems_precip_Sapporo=soup.select('#map > ul > li.point.pt1400 > a > dl > dd > p.precip')

            print('札幌の天気\n')
            print(elems_forecast_Sapporo[0].attrs['alt'])
            print('最高気温は'+elems_temp_high_Sapporo[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low_Sapporo[0].contents[0]+'度')
            print('降水確率は'+elems_precip_Sapporo[0].contents[0]+'\n')

        elif location=='釧路':

            elems_forecast_Kushiro=soup.select('#map > ul > li.point.pt1900 > a > dl > dd > p.icon > img')
            elems_temp_high_Kushiro=soup.select('#map > ul > li.point.pt1900 > a > dl > dd > p.temp > em.high')
            elems_temp_low_Kushiro=soup.select('#map > ul > li.point.pt1900 > a > dl > dd > p.temp > em.low')
            elems_precip_Kushiro=soup.select('#map > ul > li.point.pt1900 > a > dl > dd > p.precip')

            print('釧路の天気\n')
            print(elems_forecast_Kushiro[0].attrs['alt'])
            print('最高気温は'+elems_temp_high_Kushiro[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low_Kushiro[0].contents[0]+'度')
            print('降水確率は'+elems_precip_Kushiro[0].contents[0]+'\n')

        elif location=='仙台':
            elems_forecast_Sendai=soup.select('#map > ul > li.point.pt3410 > a > dl > dd > p.icon > img')
            elems_temp_high_Sendai=soup.select('#map > ul > li.point.pt3410 > a > dl > dd > p.temp > em.high')
            elems_temp_low_Sendai=soup.select('#map > ul > li.point.pt3410 > a > dl > dd > p.temp > em.low')
            elems_precip_Sendai=soup.select('#map > ul > li.point.pt3410 > a > dl > dd > p.precip')

            print('仙台の天気\n')
            print(elems_forecast_Sendai[0].attrs['alt'])
            print('最高気温は'+elems_temp_high_Sendai[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low_Sendai[0].contents[0]+'度')
            print('降水確率は'+elems_precip_Sendai[0].contents[0]+'\n')

        elif location=='東京':
            elems_forecast_Tokyo=soup.select('#map > ul > li.point.pt4410 > a > dl > dd > p.icon > img')
            elems_temp_high_Tokyo=soup.select('#map > ul > li.point.pt4410 > a > dl > dd > p.temp > em.high')
            elems_temp_low_Tokyo=soup.select('#map > ul > li.point.pt4410 > a > dl > dd > p.temp > em.low')
            elems_precip_Tokyo=soup.select('#map > ul > li.point.pt4410 > a > dl > dd > p.precip')

            print('東京の天気\n')
            print(elems_forecast_Tokyo[0].attrs['alt'])
            print('最高気温は'+elems_temp_high_Tokyo[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low_Tokyo[0].contents[0]+'度')
            print('降水確率は'+elems_precip_Tokyo[0].contents[0]+'\n')

        elif location=='名古屋':
            elems_forecast_Nagoya=soup.select('#map > ul > li.point.pt5110 > a > dl > dd > p.icon > img')
            elems_temp_high_Nagoya=soup.select('#map > ul > li.point.pt5110 > a > dl > dd > p.temp > em.high')
            elems_temp_low_Nagoya=soup.select('#map > ul > li.point.pt5110 > a > dl > dd > p.temp > em.low')
            elems_precip_Nagoya=soup.select('#map > ul > li.point.pt5110 > a > dl > dd > p.precip')

            print('名古屋の天気\n')
            print(elems_forecast_Nagoya[0].attrs['alt'])
            print('最高気温は'+elems_temp_high_Nagoya[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low_Nagoya[0].contents[0]+'度')
            print('降水確率は'+elems_precip_Nagoya[0].contents[0]+'\n')

        elif location=='新潟':
            elems_forecast_Nigata=soup.select('#map > ul > li.point.pt5410 > a > dl > dd > p.icon > img')
            elems_temp_high_Nigata=soup.select('#map > ul > li.point.pt5410 > a > dl > dd > p.temp > em.high')
            elems_temp_low_Nigata=soup.select('#map > ul > li.point.pt5410 > a > dl > dd > p.temp > em.low')
            elems_precip_Nigata=soup.select('#map > ul > li.point.pt5410 > a > dl > dd > p.precip')

            print('新潟の天気\n')
            print(elems_forecast_Nigata[0].attrs['alt'])
            print('最高気温は'+elems_temp_high_Nigata[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low_Nigata[0].contents[0]+'度')
            print('降水確率は'+elems_precip_Nigata[0].contents[0]+'\n')

        elif location=='金沢':
            elems_forecast_Kanazawa=soup.select('#map > ul > li.point.pt5610 > a > dl > dd > p.icon > img')
            elems_temp_high_Kanazawa=soup.select('#map > ul > li.point.pt5610 > a > dl > dd > p.temp > em.high')
            elems_temp_low_Kanazawa=soup.select('#map > ul > li.point.pt5610 > a > dl > dd > p.temp > em.low')
            elems_precip_Kanazawa=soup.select('#map > ul > li.point.pt5610 > a > dl > dd > p.precip')

            print('金沢の天気\n')
            print(elems_forecast_Kanazawa[0].attrs['alt'])
            print('最高気温は'+elems_temp_high_Kanazawa[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low_Kanazawa[0].contents[0]+'度')
            print('降水確率は'+elems_precip_Kanazawa[0].contents[0]+'\n')

        elif location=='大阪':
            elems_forecast_Osaka=soup.select('#map > ul > li.point.pt6200 > a > dl > dd > p.icon > img')
            elems_temp_high_Osaka=soup.select('#map > ul > li.point.pt6200 > a > dl > dd > p.temp > em.high')
            elems_temp_low_Osaka=soup.select('#map > ul > li.point.pt6200 > a > dl > dd > p.temp > em.low')
            elems_precip_Osaka=soup.select('#map > ul > li.point.pt6200 > a > dl > dd > p.precip')

            print('大阪のの天気\n')
            print(elems_forecast_Osaka[0].attrs['alt'])
            print('最高気温は'+elems_temp_high_Osaka[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low_Osaka[0].contents[0]+'度')
            print('降水確率は'+elems_precip_Osaka[0].contents[0]+'\n')

        elif location=='広島':
            elems_forecast_Hiroshima=soup.select('#map > ul > li.point.pt6710 > a > dl > dd > p.icon > img')
            elems_temp_high_Hiroshima=soup.select('#map > ul > li.point.pt6710 > a > dl > dd > p.temp > em.high')
            elems_temp_low_Hiroshima=soup.select('#map > ul > li.point.pt6710 > a > dl > dd > p.temp > em.low')
            elems_precip_Hiroshima=soup.select('#map > ul > li.point.pt6710 > a > dl > dd > p.precip')

            print('広島の天気\n')
            print(elems_forecast_Hiroshima[0].attrs['alt'])
            print('最高気温は'+elems_temp_high_Hiroshima[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low_Hiroshima[0].contents[0]+'度')
            print('降水確率は'+elems_precip_Hiroshima[0].contents[0]+'\n')

        elif location=='高知':
            elems_forecast_Kochi=soup.select('#map > ul > li.point.pt7410 > a > dl > dd > p.icon > img')
            elems_temp_high_Kochi=soup.select('#map > ul > li.point.pt7410 > a > dl > dd > p.temp > em.high')
            elems_temp_low_Kochi=soup.select('#map > ul > li.point.pt7410 > a > dl > dd > p.temp > em.low')
            elems_precip_Kochi=soup.select('#map > ul > li.point.pt7410 > a > dl > dd > p.precip')

            print('高知の天気\n')
            print(elems_forecast_Kochi[0].attrs['alt'])
            print('最高気温は'+elems_temp_high_Kochi[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low_Kochi[0].contents[0]+'度')
            print('降水確率は'+elems_precip_Kochi[0].contents[0]+'\n')

        elif location=='福岡':
            elems_forecast_Fukuoka=soup.select('#map > ul > li.point.pt8210 > a > dl > dd > p.icon > img')
            elems_temp_high_Fukuoka=soup.select('#map > ul > li.point.pt8210 > a > dl > dd > p.temp > em.high')
            elems_temp_low_Fukuoka=soup.select('#map > ul > li.point.pt8210 > a > dl > dd > p.temp > em.low')
            elems_precip_Fukuoka=soup.select('#map > ul > li.point.pt8210 > a > dl > dd > p.precip')

            print('福岡の天気\n')
            print(elems_forecast_Fukuoka[0].attrs['alt'])
            print('最高気温は'+elems_temp_high_Fukuoka[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low_Fukuoka[0].contents[0]+'度')
            print('降水確率は'+elems_precip_Fukuoka[0].contents[0]+'\n')

        elif location=='鹿児島':
            elems_forecast_Kagoshima=soup.select('#map > ul > li.point.pt8810 > a > dl > dd > p.icon > img')
            elems_temp_high_Kagoshima=soup.select('#map > ul > li.point.pt8810 > a > dl > dd > p.temp > em.high')
            elems_temp_low_Kagoshima=soup.select('#map > ul > li.point.pt8810 > a > dl > dd > p.temp > em.low')
            elems_precip_Kagoshima=soup.select('#map > ul > li.point.pt8810 > a > dl > dd > p.precip')

            print('鹿児島の天気\n')
            print(elems_forecast_Kagoshima[0].attrs['alt'])
            print('最高気温は'+elems_temp_high_Kagoshima[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low_Kagoshima[0].contents[0]+'度')
            print('降水確率は'+elems_precip_Kagoshima[0].contents[0]+'\n')

        elif location=='那覇':
            elems_forecast_Naha=soup.select('#map > ul > li.point.pt9110 > a > dl > dd > p.icon > img')
            elems_temp_high_Naha=soup.select('#map > ul > li.point.pt9110 > a > dl > dd > p.temp > em.high')
            elems_temp_low_Naha=soup.select('#map > ul > li.point.pt9110 > a > dl > dd > p.temp > em.low')
            elems_precip_Naha=soup.select('#map > ul > li.point.pt9110 > a > dl > dd > p.precip')

            print('那覇の天気\n')
            print(elems_forecast_Naha[0].attrs['alt'])
            print('最高気温は'+elems_temp_high_Naha[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low_Naha[0].contents[0]+'度')
            print('降水確率は'+elems_precip_Naha[0].contents[0]+'\n')

        elif location=='稚内':

            url_Hokkaido='https://weather.yahoo.co.jp/weather/jp/1.html?day=1'
            res_Hokkaido=requests.get(url_Hokkaido)
            soup_Hokkaido=BeautifulSoup(res_Hokkaido.text,"html.parser")

            elems_forecast=soup_Hokkaido.select('#map > ul > li.point.pt1100 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Hokkaido.select('#map > ul > li.point.pt1100 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Hokkaido.select('#map > ul > li.point.pt1100 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Hokkaido.select('#map > ul > li.point.pt1100 > a > dl > dd > p.precip')

            print('稚内の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='旭川':
        
            url_Hokkaido='https://weather.yahoo.co.jp/weather/jp/1.html?day=1'
            res_Hokkaido=requests.get(url_Hokkaido)
            soup_Hokkaido=BeautifulSoup(res_Hokkaido.text,"html.parser")


            elems_forecast=soup_Hokkaido.select('#map > ul > li.point.pt1200 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Hokkaido.select('#map > ul > li.point.pt1200 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Hokkaido.select('#map > ul > li.point.pt1200 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Hokkaido.select('#map > ul > li.point.pt1200 > a > dl > dd > p.precip')

            print('旭川の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='網走':

            url_Hokkaido='https://weather.yahoo.co.jp/weather/jp/1.html?day=1'
            res_Hokkaido=requests.get(url_Hokkaido)
            soup_Hokkaido=BeautifulSoup(res_Hokkaido.text,"html.parser")


            elems_forecast=soup_Hokkaido.select('#map > ul > li.point.pt1710 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Hokkaido.select('#map > ul > li.point.pt1710 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Hokkaido.select('#map > ul > li.point.pt1710 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Hokkaido.select('#map > ul > li.point.pt1710 > a > dl > dd > p.precip')

            print('網走の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='室蘭':

            url_Hokkaido='https://weather.yahoo.co.jp/weather/jp/1.html?day=1'
            res_Hokkaido=requests.get(url_Hokkaido)
            soup_Hokkaido=BeautifulSoup(res_Hokkaido.text,"html.parser")


            elems_forecast=soup_Hokkaido.select('#map > ul > li.point.pt2100 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Hokkaido.select('#map > ul > li.point.pt2100 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Hokkaido.select('#map > ul > li.point.pt2100 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Hokkaido.select('#map > ul > li.point.pt2100 > a > dl > dd > p.precip')

            print('室蘭の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='函館':

            url_Hokkaido='https://weather.yahoo.co.jp/weather/jp/1.html?day=1'
            res_Hokkaido=requests.get(url_Hokkaido)
            soup_Hokkaido=BeautifulSoup(res_Hokkaido.text,"html.parser")


            elems_forecast=soup_Hokkaido.select('#map > ul > li.point.pt2300 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Hokkaido.select('#map > ul > li.point.pt2300 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Hokkaido.select('#map > ul > li.point.pt2300 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Hokkaido.select('#map > ul > li.point.pt2300 > a > dl > dd > p.precip')

            print('函館の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='青森':

            url_Tohoku='https://weather.yahoo.co.jp/weather/jp/2.html?day=1'
            res_Tohoku=requests.get(url_Tohoku)
            soup_Tohoku=BeautifulSoup(res_Tohoku.text,"html.parser")


            elems_forecast=soup_Tohoku.select('#map > ul > li.point.pt3110 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Tohoku.select('#map > ul > li.point.pt3110 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Tohoku.select('#map > ul > li.point.pt3110 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Tohoku.select('#map > ul > li.point.pt3110 > a > dl > dd > p.precip')

            print('青森の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='秋田':

            url_Tohoku='https://weather.yahoo.co.jp/weather/jp/2.html?day=1'
            res_Tohoku=requests.get(url_Tohoku)
            soup_Tohoku=BeautifulSoup(res_Tohoku.text,"html.parser")


            elems_forecast=soup_Tohoku.select('#map > ul > li.point.pt3210 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Tohoku.select('#map > ul > li.point.pt3210 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Tohoku.select('#map > ul > li.point.pt3210 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Tohoku.select('#map > ul > li.point.pt3210 > a > dl > dd > p.precip')

            print('秋田の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='盛岡':

            url_Tohoku='https://weather.yahoo.co.jp/weather/jp/2.html?day=1'
            res_Tohoku=requests.get(url_Tohoku)
            soup_Tohoku=BeautifulSoup(res_Tohoku.text,"html.parser")


            elems_forecast=soup_Tohoku.select('#map > ul > li.point.pt3310 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Tohoku.select('#map > ul > li.point.pt3310 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Tohoku.select('#map > ul > li.point.pt3310 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Tohoku.select('#map > ul > li.point.pt3310 > a > dl > dd > p.precip')

            print('盛岡の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='山形':

            url_Tohoku='https://weather.yahoo.co.jp/weather/jp/2.html?day=1'
            res_Tohoku=requests.get(url_Tohoku)
            soup_Tohoku=BeautifulSoup(res_Tohoku.text,"html.parser")


            elems_forecast=soup_Tohoku.select('#map > ul > li.point.pt3510 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Tohoku.select('#map > ul > li.point.pt3510 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Tohoku.select('#map > ul > li.point.pt3510 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Tohoku.select('#map > ul > li.point.pt3510 > a > dl > dd > p.precip')

            print('山形の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='福島':

            url_Tohoku='https://weather.yahoo.co.jp/weather/jp/2.html?day=1'
            res_Tohoku=requests.get(url_Tohoku)
            soup_Tohoku=BeautifulSoup(res_Tohoku.text,"html.parser")


            elems_forecast=soup_Tohoku.select('#map > ul > li.point.pt3610 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Tohoku.select('#map > ul > li.point.pt3610 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Tohoku.select('#map > ul > li.point.pt3610 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Tohoku.select('#map > ul > li.point.pt3610 > a > dl > dd > p.precip')

            print('福島の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='水戸':

            url_Kanto='https://weather.yahoo.co.jp/weather/jp/3.html?day=1'
            res_Kanto=requests.get(url_Kanto)
            soup_Kanto=BeautifulSoup(res_Kanto.text,"html.parser")


            elems_forecast=soup_Kanto.select('#map > ul > li.point.pt4010 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Kanto.select('#map > ul > li.point.pt4010 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Kanto.select('#map > ul > li.point.pt4010 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Kanto.select('#map > ul > li.point.pt4010 > a > dl > dd > p.precip')

            print('水戸の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='宇都宮':

            url_Kanto='https://weather.yahoo.co.jp/weather/jp/3.html?day=1'
            res_Kanto=requests.get(url_Kanto)
            soup_Kanto=BeautifulSoup(res_Kanto.text,"html.parser")


            elems_forecast=soup_Kanto.select('#map > ul > li.point.pt4110 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Kanto.select('#map > ul > li.point.pt4110 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Kanto.select('#map > ul > li.point.pt4110 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Kanto.select('#map > ul > li.point.pt4110 > a > dl > dd > p.precip')

            print('宇都宮の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='前橋':

            url_Kanto='https://weather.yahoo.co.jp/weather/jp/3.html?day=1'
            res_Kanto=requests.get(url_Kanto)
            soup_Kanto=BeautifulSoup(res_Kanto.text,"html.parser")


            elems_forecast=soup_Kanto.select('#map > ul > li.point.pt4210 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Kanto.select('#map > ul > li.point.pt4210 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Kanto.select('#map > ul > li.point.pt4210 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Kanto.select('#map > ul > li.point.pt4210 > a > dl > dd > p.precip')

            print('前橋の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='さいたま':

            url_Kanto='https://weather.yahoo.co.jp/weather/jp/3.html?day=1'
            res_Kanto=requests.get(url_Kanto)
            soup_Kanto=BeautifulSoup(res_Kanto.text,"html.parser")


            elems_forecast=soup_Kanto.select('#map > ul > li.point.pt4310 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Kanto.select('#map > ul > li.point.pt4310 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Kanto.select('#map > ul > li.point.pt4310 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Kanto.select('#map > ul > li.point.pt4310 > a > dl > dd > p.precip')

            print('さいたまの天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='千葉':

            url_Kanto='https://weather.yahoo.co.jp/weather/jp/3.html?day=1'
            res_Kanto=requests.get(url_Kanto)
            soup_Kanto=BeautifulSoup(res_Kanto.text,"html.parser")


            elems_forecast=soup_Kanto.select('#map > ul > li.point.pt4510 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Kanto.select('#map > ul > li.point.pt4510 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Kanto.select('#map > ul > li.point.pt4510 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Kanto.select('#map > ul > li.point.pt4510 > a > dl > dd > p.precip')

            print('千葉の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='横浜':

            url_Kanto='https://weather.yahoo.co.jp/weather/jp/3.html?day=1'
            res_Kanto=requests.get(url_Kanto)
            soup_Kanto=BeautifulSoup(res_Kanto.text,"html.parser")


            elems_forecast=soup_Kanto.select('#map > ul > li.point.pt4610 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Kanto.select('#map > ul > li.point.pt4610 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Kanto.select('#map > ul > li.point.pt4610 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Kanto.select('#map > ul > li.point.pt4610 > a > dl > dd > p.precip')

            print('横浜の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='長野':

            url_Kanto='https://weather.yahoo.co.jp/weather/jp/3.html?day=1'
            res_Kanto=requests.get(url_Kanto)
            soup_Kanto=BeautifulSoup(res_Kanto.text,"html.parser")


            elems_forecast=soup_Kanto.select('#map > ul > li.point.pt4810 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Kanto.select('#map > ul > li.point.pt4810 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Kanto.select('#map > ul > li.point.pt4810 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Kanto.select('#map > ul > li.point.pt4810 > a > dl > dd > p.precip')

            print('長野の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='甲府':

            url_Kanto='https://weather.yahoo.co.jp/weather/jp/3.html?day=1'
            res_Kanto=requests.get(url_Kanto)
            soup_Kanto=BeautifulSoup(res_Kanto.text,"html.parser")


            elems_forecast=soup_Kanto.select('#map > ul > li.point.pt4910 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Kanto.select('#map > ul > li.point.pt4910 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Kanto.select('#map > ul > li.point.pt4910 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Kanto.select('#map > ul > li.point.pt4910 > a > dl > dd > p.precip')

            print('甲府の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='静岡':

            url_Cyubu='https://weather.yahoo.co.jp/weather/jp/7.html?day=1'
            res_Cyubu=requests.get(url_Cyubu)
            soup_Cyubu=BeautifulSoup(res_Cyubu.text,"html.parser")

            elems_forecast=soup_Cyubu.select('#map > ul > li.point.pt5010 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Cyubu.select('#map > ul > li.point.pt5010 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Cyubu.select('#map > ul > li.point.pt5010 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Cyubu.select('#map > ul > li.point.pt5010 > a > dl > dd > p.precip')

            print('静岡の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='岐阜':

            url_Cyubu='https://weather.yahoo.co.jp/weather/jp/7.html?day=1'
            res_Cyubu=requests.get(url_Cyubu)
            soup_Cyubu=BeautifulSoup(res_Cyubu.text,"html.parser")

            elems_forecast=soup_Cyubu.select('#map > ul > li.point.pt5210 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Cyubu.select('#map > ul > li.point.pt5210 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Cyubu.select('#map > ul > li.point.pt5210 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Cyubu.select('#map > ul > li.point.pt5210 > a > dl > dd > p.precip')

            print('岐阜の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='津':

            url_Cyubu='https://weather.yahoo.co.jp/weather/jp/7.html?day=1'
            res_Cyubu=requests.get(url_Cyubu)
            soup_Cyubu=BeautifulSoup(res_Cyubu.text,"html.parser")

            elems_forecast=soup_Cyubu.select('#map > ul > li.point.pt5310 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Cyubu.select('#map > ul > li.point.pt5310 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Cyubu.select('#map > ul > li.point.pt5310 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Cyubu.select('#map > ul > li.point.pt5310 > a > dl > dd > p.precip')

            print('津の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='富山':

            url_Cyubu='https://weather.yahoo.co.jp/weather/jp/7.html?day=1'
            res_Cyubu=requests.get(url_Cyubu)
            soup_Cyubu=BeautifulSoup(res_Cyubu.text,"html.parser")

            elems_forecast=soup_Cyubu.select('#map > ul > li.point.pt5510 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Cyubu.select('#map > ul > li.point.pt5510 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Cyubu.select('#map > ul > li.point.pt5510 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Cyubu.select('#map > ul > li.point.pt5510 > a > dl > dd > p.precip')

            print('富山の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='福井':

            url_Cyubu='https://weather.yahoo.co.jp/weather/jp/7.html?day=1'
            res_Cyubu=requests.get(url_Cyubu)
            soup_Cyubu=BeautifulSoup(res_Cyubu.text,"html.parser")

            elems_forecast=soup_Cyubu.select('#map > ul > li.point.pt5710 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Cyubu.select('#map > ul > li.point.pt5710 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Cyubu.select('#map > ul > li.point.pt5710 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Cyubu.select('#map > ul > li.point.pt5710 > a > dl > dd > p.precip')

            print('福井の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='大津':

            url_Cyubu='https://weather.yahoo.co.jp/weather/jp/7.html?day=1'
            res_Cyubu=requests.get(url_Cyubu)
            soup_Cyubu=BeautifulSoup(res_Cyubu.text,"html.parser")

            elems_forecast=soup_Cyubu.select('#map > ul > li.point.pt6010 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Cyubu.select('#map > ul > li.point.pt6010 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Cyubu.select('#map > ul > li.point.pt6010 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Cyubu.select('#map > ul > li.point.pt6010 > a > dl > dd > p.precip')

            print('大津の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='京都':

            url_Cyubu='https://weather.yahoo.co.jp/weather/jp/7.html?day=1'
            res_Cyubu=requests.get(url_Cyubu)
            soup_Cyubu=BeautifulSoup(res_Cyubu.text,"html.parser")

            elems_forecast=soup_Cyubu.select('#map > ul > li.point.pt6110 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Cyubu.select('#map > ul > li.point.pt6110 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Cyubu.select('#map > ul > li.point.pt6110 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Cyubu.select('#map > ul > li.point.pt6110 > a > dl > dd > p.precip')

            print('京都の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='神戸':

            url_Cyubu='https://weather.yahoo.co.jp/weather/jp/7.html?day=1'
            res_Cyubu=requests.get(url_Cyubu)
            soup_Cyubu=BeautifulSoup(res_Cyubu.text,"html.parser")

            elems_forecast=soup_Cyubu.select('#map > ul > li.point.pt6310 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Cyubu.select('#map > ul > li.point.pt6310 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Cyubu.select('#map > ul > li.point.pt6310 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Cyubu.select('#map > ul > li.point.pt6310 > a > dl > dd > p.precip')

            print('神戸の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='奈良':

            url_Cyubu='https://weather.yahoo.co.jp/weather/jp/7.html?day=1'
            res_Cyubu=requests.get(url_Cyubu)
            soup_Cyubu=BeautifulSoup(res_Cyubu.text,"html.parser")

            elems_forecast=soup_Cyubu.select('#map > ul > li.point.pt6410 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Cyubu.select('#map > ul > li.point.pt6410 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Cyubu.select('#map > ul > li.point.pt6410 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Cyubu.select('#map > ul > li.point.pt6410 > a > dl > dd > p.precip')

            print('奈良の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='和歌山':

            url_Cyubu='https://weather.yahoo.co.jp/weather/jp/7.html?day=1'
            res_Cyubu=requests.get(url_Cyubu)
            soup_Cyubu=BeautifulSoup(res_Cyubu.text,"html.parser")

            elems_forecast=soup_Cyubu.select('#map > ul > li.point.pt6510 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_Cyubu.select('#map > ul > li.point.pt6510 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_Cyubu.select('#map > ul > li.point.pt6510 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_Cyubu.select('#map > ul > li.point.pt6510 > a > dl > dd > p.precip')

            print('和歌山の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='岡山':

            url_local='https://weather.yahoo.co.jp/weather/jp/8.html?day=1'
            res_local=requests.get(url_local)
            soup_local=BeautifulSoup(res_local.text,"html.parser")

            elems_forecast=soup_local.select('#map > ul > li.point.pt6610 > a > dl > dd > p.icon > img') 
            elems_temp_high=soup_local.select('#map > ul > li.point.pt6610 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_local.select('#map > ul > li.point.pt6610 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_local.select('#map > ul > li.point.pt6610 > a > dl > dd > p.precip')

            print('岡山の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='松江':

            url_local='https://weather.yahoo.co.jp/weather/jp/8.html?day=1'
            res_local=requests.get(url_local)
            soup_local=BeautifulSoup(res_local.text,"html.parser")

            elems_forecast=soup_local.select('#map > ul > li.point.pt6810 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_local.select('#map > ul > li.point.pt6810 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_local.select('#map > ul > li.point.pt6810 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_local.select('#map > ul > li.point.pt6810 > a > dl > dd > p.precip')

            print('松江の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='鳥取':

            url_local='https://weather.yahoo.co.jp/weather/jp/8.html?day=1'
            res_local=requests.get(url_local)
            soup_local=BeautifulSoup(res_local.text,"html.parser")

            elems_forecast=soup_local.select('#map > ul > li.point.pt6910 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_local.select('#map > ul > li.point.pt6910 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_local.select('#map > ul > li.point.pt6910 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_local.select('#map > ul > li.point.pt6910 > a > dl > dd > p.precip')

            print('鳥取の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='徳島':

            url_local='https://weather.yahoo.co.jp/weather/jp/8.html?day=1'
            res_local=requests.get(url_local)
            soup_local=BeautifulSoup(res_local.text,"html.parser")

            elems_forecast=soup_local.select('#map > ul > li.point.pt7110 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_local.select('#map > ul > li.point.pt7110 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_local.select('#map > ul > li.point.pt7110 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_local.select('#map > ul > li.point.pt7110 > a > dl > dd > p.precip')

            print('徳島の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='高松':

            url_local='https://weather.yahoo.co.jp/weather/jp/8.html?day=1'
            res_local=requests.get(url_local)
            soup_local=BeautifulSoup(res_local.text,"html.parser")

            elems_forecast=soup_local.select('#map > ul > li.point.pt7200 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_local.select('#map > ul > li.point.pt7200 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_local.select('#map > ul > li.point.pt7200 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_local.select('#map > ul > li.point.pt7200 > a > dl > dd > p.precip')

            print('高松の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='松山':

            url_local='https://weather.yahoo.co.jp/weather/jp/8.html?day=1'
            res_local=requests.get(url_local)
            soup_local=BeautifulSoup(res_local.text,"html.parser")

            elems_forecast=soup_local.select('#map > ul > li.point.pt7310 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_local.select('#map > ul > li.point.pt7310 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_local.select('#map > ul > li.point.pt7310 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_local.select('#map > ul > li.point.pt7310 > a > dl > dd > p.precip')

            print('松山の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='山口':

            url_local='https://weather.yahoo.co.jp/weather/jp/8.html?day=1'
            res_local=requests.get(url_local)
            soup_local=BeautifulSoup(res_local.text,"html.parser")

            elems_forecast=soup_local.select('#map > ul > li.point.pt8120 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_local.select('#map > ul > li.point.pt8120 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_local.select('#map > ul > li.point.pt8120 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_local.select('#map > ul > li.point.pt8120 > a > dl > dd > p.precip')

            print('山口の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='大分':

            url_local='https://weather.yahoo.co.jp/weather/jp/10.html?day=1'
            res_local=requests.get(url_local)
            soup_local=BeautifulSoup(res_local.text,"html.parser")

            elems_forecast=soup_local.select('#map > ul > li.point.pt8310 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_local.select('#map > ul > li.point.pt8310 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_local.select('#map > ul > li.point.pt8310 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_local.select('#map > ul > li.point.pt8310 > a > dl > dd > p.precip')

            print('大分の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='長崎':

            url_local='https://weather.yahoo.co.jp/weather/jp/10.html?day=1'
            res_local=requests.get(url_local)
            soup_local=BeautifulSoup(res_local.text,"html.parser")

            elems_forecast=soup_local.select('#map > ul > li.point.pt8410 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_local.select('#map > ul > li.point.pt8410 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_local.select('#map > ul > li.point.pt8410 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_local.select('#map > ul > li.point.pt8410 > a > dl > dd > p.precip')

            print('長崎の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='佐賀':

            url_local='https://weather.yahoo.co.jp/weather/jp/10.html?day=1'
            res_local=requests.get(url_local)
            soup_local=BeautifulSoup(res_local.text,"html.parser")

            elems_forecast=soup_local.select('#map > ul > li.point.pt8510 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_local.select('#map > ul > li.point.pt8510 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_local.select('#map > ul > li.point.pt8510 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_local.select('#map > ul > li.point.pt8510 > a > dl > dd > p.precip')

            print('佐賀の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='熊本':

            url_local='https://weather.yahoo.co.jp/weather/jp/10.html?day=1'
            res_local=requests.get(url_local)
            soup_local=BeautifulSoup(res_local.text,"html.parser")

            elems_forecast=soup_local.select('#map > ul > li.point.pt8610 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_local.select('#map > ul > li.point.pt8610 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_local.select('#map > ul > li.point.pt8610 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_local.select('#map > ul > li.point.pt8610 > a > dl > dd > p.precip')

            print('熊本の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')

        elif location=='宮崎':

            url_local='https://weather.yahoo.co.jp/weather/jp/10.html?day=1'
            res_local=requests.get(url_local)
            soup_local=BeautifulSoup(res_local.text,"html.parser")

            elems_forecast=soup_local.select('#map > ul > li.point.pt8710 > a > dl > dd > p.icon > img')
            elems_temp_high=soup_local.select('#map > ul > li.point.pt8710 > a > dl > dd > p.temp > em.high')
            elems_temp_low=soup_local.select('#map > ul > li.point.pt8710 > a > dl > dd > p.temp > em.low')
            elems_precip=soup_local.select('#map > ul > li.point.pt8710 > a > dl > dd > p.precip')

            print('宮崎の天気\n')
            print(elems_forecast[0].attrs['alt'])
            print('最高気温は'+elems_temp_high[0].contents[0]+'度')
            print('最低気温は'+elems_temp_low[0].contents[0]+'度')
            print('降水確率は'+elems_precip[0].contents[0]+'\n')


        else:             
            print('指定された都市が無いです')


else:
    print('都市が指定されていません')
