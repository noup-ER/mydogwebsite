import requests
from lxml import etree
def getweibonews():
    url= 'https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6'
    #print(response.text)
    headers={
        'User-Agent': 'Mozilla/5.0 (Wind ows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    html=etree.HTML(response.text)
    datas=html.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr')
    ans = []
    for data in datas[:20]:
        data_title=data.xpath('td[2]/a/text()')#标题的xpath路径
        ans.append(data_title[0])
    return ans
