from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

#pip list : 현재 설치된 패키지에 대한 내용을 볼수있다
#pip show 패키지명 : 해당 패키지에 대한 정보를 볼 수 있다
#pip install --upgrade 패키지명 : 해당 패키지를 업그레읻를 할 수 있다
#pip uninstall 패키지명 : 해당 패키지 삭제