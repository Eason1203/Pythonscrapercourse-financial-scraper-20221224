import requests
from bs4 import BeautifulSoup


response = requests.get('https://tw.stock.yahoo.com/class-quote?sectorId=46&exchange=TAI')
soup = BeautifulSoup(response.text, 'lxml')
date = soup.find('time').get('datatime')

rows = soup.find_all('div', {'class':'Bgc(#fff) table-row D(f) H(48px) Ai(c) Bgc(#e7f3ff):h Fz(16px) Px(12px) Bxz(bb) Bdbs(s) Bdbw(1px) Bdbc($bd-primary-divider)'})

result = []
for row in rows:
    company = row.find('div', {'class':'Lh(20px) Fw(600) Fz(16px) Ell'}).getText()
    price = row.find('div', {'class':'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(68px)'}).getText()
    status_element = row.find_all('div', {'class': 'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(74px)'})[0]
    status_class = status_element.find('span').get('class')
    status = ''

    if 'C($c-trend-down)' in status_class:
        status = 'down' + status_element.getText()
    elif 'C($c-trend-up)' in status_class:
        status = 'up' + status_element.getText()
    else:
        status = status_element.getText()

    Precentage_element = row.find_all('div', {'class': 'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(74px)'})[1]
    Precentage_class = Precentage_element.find('span').get('class')
    Precentage = ''

    if 'C($c-trend-down)' in Precentage_class:
        Precentage = 'down' + Precentage_element.getText()
    elif 'C($c-trend-up)' in Precentage_class:
        Precentage = 'up' + Precentage_element.getText()
    else:
        Precentage = Precentage_element.getText()

    result.append([date, company, price, status, Precentage])

print(result)


