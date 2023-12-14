# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,11):
        #오늘의 유머 베스트 게시판 주소 
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        #URL 주소
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, headers = hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})

        # <td class="subject">
        # <a href="/board/view.php?table=bestofbest&amp;no=472161&amp;s_no=472161&amp;page=10" target="_top">K-신파 보고 펑펑 우는 외국인들</a>

        for item in list:
                try:
                       title = item.find('a').text.strip()
                       link = item.find('a')['href']
                       print(link)
                    #    print(title)
                       if (re.search('미국', title)):
                                print(title)
                except:
                        pass
        
