# web1.py
# 웹크롤링을 위한 선언

from bs4 import BeautifulSoup

# 웹페이지를 로딩
# 메서드체인
page = open ('test01.html', 'rt', encoding='utf-8').read()

#검색이 용이한 객체 
soup = BeautifulSoup(page, "html.parser")

# 전체문서
# print (soup.prettify())

# print(soup.find_all("p"))

# 첫번째 <p>만 건색
# print(soup.find('p'))

# print(soup.find_all ("p", class_="outer-text"))

# print(soup.find_all ("p", attrs={"class" : "outer-text"}))

# 특정태그(id)
# print (soup.find(id="first"))

# 태그 내부에 컨텐츠 가져오기 (Text 속성)
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n","")
    print(title)
