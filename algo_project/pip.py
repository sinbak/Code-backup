# import requests
# from bs4 import BeautifulSoup
# webpage = requests.get("https://www.daangn.com/hot_articles")
# soup = BeautifulSoup(webpage.content, "html.parser")
# print(soup.p) #P = 해당태그

# from urllib.request import urlopen
# from urllib.error import HTTPError
# from urllib.error import URLError

# try:
#     html = urlopen('http://www.pythonscraping.com/pages/page1.html')
# except HTTPError as e:
#     print(e)
# except URLError as e:
#     print('The server could not be found!')
# else:
#     print('It worked!')

# import requests
# from bs4 import BeautifulSoup

# url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

# response = requests.get(url) #요청한 url를 가져온다

# if response.status_code == 200: #정상적으로 실행이 된다면
#     html = response.text #텍스트 형식으로
#     soup = BeautifulSoup(html, 'html.parser')
#     print(soup)

# else : 
#     print(response.status_code)

# import requests
# payload = { 'key1' : 'value1', 'key2' : 'value2'}
# r = requests.post("https://httpbin.org/post", data = payload)
# print(r.text)

# from bs4 import BeautifulSoup
# from urllib.request import urlopen

# with urlopen('https://en.wikipedia.org/wiki/Main_page') as response: # response = urlopen('https://en.wikipedia.org/wiki/Main_page') 같다
#     soup = BeautifulSoup(response, 'html.parser') #파서를 통한 분석을 하고
#     for anchor in soup.find_all('a'): #a 태그를 찾는다
#         print(anchor.get('href', '/')) #a태그의 주소를 가져와 출력하라

# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# with urlopen('http://www.hannam.ac.kr/community/community_0104.html') as HNU_community:
#     soup = BeautifulSoup(HNU_community, 'html.parser')
#     for anchor in soup.find_all('a'):
#         print(anchor.get('href', '/'))


# import requests
# request = requests.get('http://www.hannam.ac.kr/community/community_0104.html')
# html = request.text.strip()
# print(html)

# from bs4 import BeautifulSoup
# # from urllib.request import urlopen
# import requests
# request = requests.get('http://www.hannam.ac.kr/community/community_0104.html')
# html = request.text
# soup = BeautifulSoup(html, 'html.parser')
# links = soup.select('td > a')

# for link in links:
#     if link.has_attr('href'):
#         print(link.text)
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# with urlopen('http://www.hannam.ac.kr/community/community_0104.html') as response: # response = urlopen('https://en.wikipedia.org/wiki/Main_page') 같다
#     soup = BeautifulSoup(response, 'html.parser') #파서를 통한 분석을 하고
#     for anchor in soup.find_all('a'): #a 태그를 찾는다
#         print(anchor.get('href', '/')) #a태그의 주소를 가져와 출력하라


# import requests
# from bs4 import BeautifulSoup
# soup = requests.get('http://www.hannam.ac.kr/community/community_0104.html')
# soup = BeautifulSoup(soup, 'html.parser')
# soup = soup.select("td", atters={"class":"mobile-bbs list"})
# for anchor in soup.select("td", atters={"class":"mobile-bbs list"}): #a 태그를 찾는다
#         print(anchor.get('href', '/')) #a태그의 주소를 가져와 출력하라

# import requests
# from bs4 import BeautifulSoup

# # 특정 URL에 접속하는 요청(Request) 객체를 생성합니다.
# request = requests.get('http://www.hannam.ac.kr/community/community_0104.html')
# # 접속한 이후의 웹 사이트 소스코드를 추출합니다.
# soup = BeautifulSoup(request, 'html.parser')
# soup = request.select({'class': 'mobile-bbs list'})
# print(soup)

import re #텍스트 수정(탭, 개행, 공백)
import requests
from bs4 import BeautifulSoup
import pandas as pd

source =requests.get("http://uniboard.hannam.ac.kr/servlet/controller.helpdesk.UniboardServlet?seq=MQ==")
soup = BeautifulSoup(source.content, "html.parser")

tr_data = soup.find(class_='tb_brdTmp').find_all('tr') #table class= 'tb_brdTmp' / tr에 있는 내용 가져오기
del tr_data[0] #처음 부분 삭제(불필요한 부분 삭제)

tr_data_len = len(tr_data)

row_list = [] #행
column_list = [] #열
thead_list = ["게시글 번호","제목","날자","작성자","조회수"]

for i in range(0, tr_data_len):
    td_data = tr_data[i].find_all('td')
    
    td_data_len = len(td_data)
    for j in range(0, td_data_len): #td 가져오기
        #element = td_data[j].text.strip()
        
        element = re.sub('&nbsp; | &nbsp;|\n|\t|\r|  ', '', td_data[j].text.strip()) #stripe() #빈공간 정리
        column_list.append(element)
        
        
        # print(j, ' - ', td_data[j])
    del column_list[0:2] #열의 불필요한 부분 제거
    del column_list[2] ##열의 불필요한 부분 제거
    
    row_list.append(column_list) #열에 있는 내용을 행에 넣기
    column_list = []
    
result = pd.DataFrame(row_list,columns=thead_list)
print(result)
# from bs4 import BeautifulSoup
# from urllib.request import urlopen

