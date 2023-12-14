# 크롤링
from bs4 import BeautifulSoup
import requests

url = "https://www.daangn.com/hot_articles"
response = requests.get(url)

# 검색이 용이한 객체
# soup = BeautifulSoup(response.text, "html.parser")
# posts = soup.find_all("div", attrs={"class":"card-desc"})
# for post in posts :
#     title = post.find("h2", attrs={"class":"card-title"})
#     price = post.find("div", attrs={"class":"card-price"})
#     addr = post.find("div", attrs={"class":"card-region-name"})
#     # print ("{0}, {1}, {2}".format(title.text, price.text, addr.text))
#     title = title.text.strip().replace("\n","")
#     price = price.text.strip().replace("\n","")
#     addr = addr.text.strip().replace("\n","")
#     print ("{0}, {1}, {2}".format(title, price, addr))

# 파일에 저장
soup = BeautifulSoup(response.text, "html.parser")
posts = soup.find_all("div", attrs={"class":"card-desc"})

#저장
f = open("dangn.txt", "wt", encoding="utf-8")
for post in posts :
    title = post.find("h2", attrs={"class":"card-title"})
    price = post.find("div", attrs={"class":"card-price"})
    addr = post.find("div", attrs={"class":"card-region-name"})
    # print ("{0}, {1}, {2}".format(title.text, price.text, addr.text))
    title = title.text.strip().replace("\n","")
    price = price.text.strip().replace("\n","")
    addr = addr.text.strip().replace("\n","")
    print ("{0}, {1}, {2}".format(title, price, addr))
    f.write(f"{title}, {price}, {addr}\n")





    # <div class="card-desc">
    #   <h2 class="card-title">생로랑 반지갑</h2>
    #   <div class="card-price ">
    #     30,000원
    #   </div>
    #   <div class="card-region-name">
    #     서울 서초구 반포4동
    #   </div>
    #   <div class="card-counts">