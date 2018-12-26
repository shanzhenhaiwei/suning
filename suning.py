import requests
from pyquery import PyQuery as pq


url='http://order.suning.com/order/queryOrderList.do?transStatus=&pageNumber=1&condition=&startDate=2018-09-26&endDate=2018-12-26&orderType='
cookies=''
ua='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
headers={
    'User-Agent':ua,
    'Cookie':cookies,
}
try:
    res=requests.get(url=url,headers=headers)
    text=res.text
    html=pq(text)
    dingdan=html('.name > a:nth-child(1)').text()
    print(dingdan)
except:
    print('fail')

cookielist=cookies.split(';')
testlist=cookielist.copy()

for cookie in cookielist:
    testlist.remove(cookie)
    testcookies=';'.join(testlist)
    headers = {
        'User-Agent': ua,
        'Cookie': testcookies,
    }
    try:
        res = requests.get(url=url, headers=headers)
        status=res.status_code
        print('无效：'+cookie)
    except:
        print('有效：'+cookie)
        testlist.append(cookie)

print('有效cookies：'+testcookies)



