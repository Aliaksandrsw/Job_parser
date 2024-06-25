# import asyncio
# import aiohttp
# from bs4 import BeautifulSoup
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#     'Referer': 'https://www.google.com/'
# }
# URL = 'https://career.habr.com/vacancies?q=python&type=all'
#
#
# async def habr_get_html(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url, headers=headers) as response:
#             return await response.text()
#
#
# def habr_get_all_url():
#     url_lst = [f'https://career.habr.com/vacancies?page={i}&q=python&type=all' for i in range(1, 20)]
#     return url_lst
#
#
# async def habr_get_content(lst):
#     lst_vacancy = []
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         for url in lst:
#             task = asyncio.create_task(habr_get_html(url))
#             tasks.append(task)
#         html_texts = await asyncio.gather(*tasks)
#
#         for html_text in html_texts:
#             soup = BeautifulSoup(html_text, 'html.parser')
#             cards = soup.find_all('div', 'vacancy-card')
#             for card in cards:
#                 data = {
#                     'url': f"https://career.habr.com/{card.find('a').get('href')}",
#                     'title': card.find('div', 'vacancy-card__title').text,
#                     'company': card.find('div', 'vacancy-card__company-title').text,
#                     'skills': card.find('div', 'vacancy-card__skills').text,
#                     'created': card.find('time', attrs={'class': 'basic-date'}).text
#                 }
#                 lst_vacancy.append(data)
#     return lst_vacancy
#
#
# # async def main():
# #     url_lst = habr_get_all_url()
# #     content = await habr_get_content(url_lst)
# #     #print(content)
# #
# #
# # if __name__ == '__main__':
# #     asyncio.run(main())

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Referer': 'https://www.google.com/'
}

URL = 'https://career.habr.com/vacancies?q=python&type=all'


def habr_get_html(url):
    response = requests.get(url, headers=headers, timeout=2)
    return response.text


def habr_get_all_url():
    url_lst = [f'https://career.habr.com/vacancies?page={i}&q=python&type=all' for i in range(1, 20)]
    return url_lst


def habr_get_content(lst):
    lst_vacancy = []
    for url in lst:
        html_text = habr_get_html(url)
        soup = BeautifulSoup(html_text, 'html.parser')
        cards = soup.find_all('div', 'vacancy-card')
        for card in cards:
            data = {
                'url': f"https://career.habr.com/{card.find('a').get('href')}",
                'title': card.find('div', 'vacancy-card__title').text,
                'company': card.find('div', 'vacancy-card__company-title').text,
                'skills': card.find('div', 'vacancy-card__skills').text,
                'created': card.find('time', attrs={'class': 'basic-date'}).text
            }
            lst_vacancy.append(data)
    return lst_vacancy


def main():
    url_lst = habr_get_all_url()
    content = habr_get_content(url_lst)
    print(content)


if __name__ == '__main__':
    main()
