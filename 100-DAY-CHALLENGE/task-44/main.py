from bs4 import BeautifulSoup
import requests
import random

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')

empire_webpage = response.text
soup = BeautifulSoup(empire_webpage, 'html.parser')

x = soup.select('h2 strong')
l = [v.getText() for v in x]
l = l[::-1]

with open('movies.txt', mode='w', encoding='utf-8') as file:
    for i in l:
        file.write(f'{i}\n')

# response = requests.get('https://news.ycombinator.com/news')
#
# yc_web_page = response.text
# soup = BeautifulSoup(yc_web_page, 'html.parser')
#
# article_tag = soup.find(name='a', class_='storylink')
#
#
# article_tag1 = soup.find_all(name='span', class_='score')
# l = []
# for i in article_tag1:
#     l.append(int(i.getText().split()[0]))
# print(l)

# import lxml
#
# with open('website.html') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.a)
#
# all_links = soup.find_all(name='a')
# print(all_links)
# for link in all_links:
#     # print(link.getText())
#     print(link.get('href'))
#
# heading = soup.find(name='h1', id='name')
# print(heading)
#
# heading1 = soup.find(name='h3', class_='heading')
# print(heading1)
#
#
#
# company_url = soup.select_one(selector='p a')
# print(company_url)
#
#
# headings = soup.select('.heading')
# print(headings)