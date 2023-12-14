
import requests
from bs4 import BeautifulSoup

def naver_search(keyword):
    base_url = "https://search.naver.com/search.naver"
    params = {
        "where": "view",
        "sm": "tab_jum",
        "query": keyword
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        posts = soup.select('.api_txt_lines.total_tit')

        result = []
        for post in posts:
            title = post.get_text(strip=True)
            link = post['href']

            # Get blog name, blog address, and posting date from the post's page
            post_response = requests.get(link)
            if post_response.status_code == 200:
                post_soup = BeautifulSoup(post_response.text, 'html.parser')
                
                # Get blog name
                blog_name = post_soup.select_one('.link_blog .txt84')
                blog_name = blog_name.get_text(strip=True) if blog_name else "N/A"

                # Get blog address
                blog_address = post_soup.select_one('.link_blog')['href'] if post_soup.select_one('.link_blog') else "N/A"

                # Get posting date
                post_date = post_soup.select_one('.se_publishDate, .pcol2 .date') 
                post_date = post_date.get_text(strip=True) if post_date else "N/A"

                result.append({
                    'title': title,
                    'blog_name': blog_name,
                    'blog_address': blog_address,
                    'post_date': post_date
                })

        return result
    else:
        print("Error:", response.status_code)

# Example usage
keyword = "search_keyword"
search_results = naver_search(keyword)

for result in search_results:
    print("Title:", result['title'])
    print("Blog Name:", result['blog_name'])
    print("Blog Address:", result['blog_address'])
    print("Post Date:", result['post_date'])
    print("---")
