import re , csv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

def WriteCsv(filename,the_list):
    f = open(filename,'w',newline='')
    a = csv.writer(f,delimiter=',')
    a.writerows(the_list)
    f.close()

def univ_notice3():
    source = requests.get("http://www.hannam.ac.kr/guide/guide_0200.html")
    soup = bs(source.content, "html.parser")

    search_url = soup.find(class_ = 'borad_frame').find_all('iframe')
    for i in search_url:
        url = i.attrs['src']
    plus = "&p_process=mobileListPage"
    url = url + plus

    html = ur.urlopen(url).read()
    tt = bs(html, 'html.parser')

    a = tt.find(class_= 'moblie-paging').find_all('a')

    board_url = []
    for x in a:
        board_url.append(x.attrs['href'])

    Post = [['게시물 제목','게시 일자']]
    for i in range(1,4):
        pp = "http://uniboard.hannam.ac.kr"
        url = pp + board_url[i]

        html2 = ur.urlopen(url).read()
        tt2 = bs(html, 'html.parser')

        script = tt2.findAll('td')

        for i in range(len(script)):
            txt = script[i].a.get_text()
            day = script[i].span.get_text()
            Post.append([txt,day])
    WriteCsv("POST2.csv",Post)


