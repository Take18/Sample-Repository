import requests
from bs4 import BeautifulSoup
import re

url='https://weather.yahoo.co.jp/weather/'
res=requests.get(url)
soup=BeautifulSoup(res.text,"html.parser")

elems_forecast_Tokyo=soup.select('#map > ul > li.point.pt4410 > a > dl > dd > p.icon > img')
elems_high_temp_Tokyo=soup.select('#map > ul > li.point.pt4410 > a > dl > dd > p.temp > em.high')
elems_low_temp_Tokyo=soup.select('#map > ul > li.point.pt4410 > a > dl > dd > p.temp > em.low')
elems_precip_Tokyo=soup.select('#map > ul > li.point.pt4410 > a > dl > dd > p.precip')

elems_forecast_Osaka=soup.select('#map > ul > li.point.pt6200 > a > dl > dd > p.icon > img')
elems_high_temp_Osaka=soup.select('#map > ul > li.point.pt6200 > a > dl > dd > p.temp > em.high')
elems_low_temp_Osaka=soup.select('#map > ul > li.point.pt6200 > a > dl > dd > p.temp > em.low')
elems_precip_Osaka=soup.select('#map > ul > li.point.pt6200 > a > dl > dd > p.precip')

print('東京の天気\n')
print(elems_forecast_Tokyo[0].attrs['alt'])
print('最高気温は'+elems_high_temp_Tokyo[0].contents[0]+'度')
print('最低気温は'+elems_low_temp_Tokyo[0].contents[0]+'度')
print('降水確率は'+elems_precip_Tokyo[0].contents[0]+'\n')
print('大阪の天気\n')
print(elems_forecast_Osaka[0].attrs['alt'])
print('最高気温は'+elems_high_temp_Osaka[0].contents[0]+'度')
print('最低気温は'+elems_low_temp_Osaka[0].contents[0]+'度')
print('降水確率は'+elems_precip_Osaka[0].contents[0])
