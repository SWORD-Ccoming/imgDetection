
from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error

import os
import requests



def main():
    baseurl ="自己想要爬取的网页链接"
    # 1.爬取数据
    datalist = getData(baseurl)

    # 在d盘Pyproject目录下创建名称为img的文件夹
    path2 = r'D://Pyproject'
    os.mkdir(path2 + './' + "img")

    savepath = path2 + './' + "img" + './'

    # 3.保存数据
    savaData(datalist,savepath)

    #askURL("https://pic.netbian.com/4kmeinv/index_")

#图片链接
findImg = re.compile(r'<img.*src="(.*?)"/>')
#图片名字
findName = re.compile(r'<img alt="(.*?)".*/>')

#爬取网页数据
def getData(baseurl):
    datalist = []
    for i in range(2,10):
        url = baseurl+str(i)+'.html'
        html=askURL(url)
        #print(html)

        #2.解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('img'):
            #print(item)
            data = []
            item = str(item)
            # 图片名字
            name = re.findall(findName, item)
            data.append(name)
            #图片链接
            img = re.findall(findImg,item)[0]
            data.append(img)

            datalist.append(data)

    return datalist

#保存数据
def savaData(datalist,savepath):
    print("save...")
    for i in range(0, 160):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 2):
            if j == 0:
                name = str(data[j])
            else:
                r = requests.get('https://pic.netbian.com/' + str(data[j]), stream=True)
        with open(savepath + name + '.jpg', 'wb') as fd:
            for chunk in r.iter_content():
                fd.write(chunk)

#爬取一个数据
def askURL(url):
    head={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55"
    }
    res =urllib.request.Request(url,headers=head)
    html = ''
    try:
        response =urllib.request.urlopen(res)
        html = response.read().decode("gbk")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

if __name__ == "__main__":
    main()
