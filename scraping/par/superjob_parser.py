# # import asyncio
# # import locale
# # import aiohttp
# import requests
# from bs4 import BeautifulSoup
# import datetime
#
# # locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# #
# # created_date = datetime.date(2024, 6, 8)
# # created_str = created_date.strftime("%d %B")
# #
# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
# #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# #     'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
# #     'Referer': 'https://www.google.com/'
# # }
# # URL = 'https://russia.superjob.ru/vacancy/search/?keywords=Python&click_from=facet'
# #
# #
# # async def get_html(session, url):
# #     async with session.get(url, headers=headers) as response:
# #         return await response.text()
# #
# #
# # def get_all_url():
# #     return [f'https://russia.superjob.ru/vacancy/search/?keywords=Python&click_from=facet&page={i}' for i in
# #             range(1, 3)]
# #
# #
# # async def get_content(lst: list):
# #     async with aiohttp.ClientSession() as session:
# #         tasks = [get_html(session, url) for url in lst]
# #         html_texts = await asyncio.gather(*tasks)
# #
# #     lst_vacancy = []
# #     for html_text in html_texts:
# #         soup = BeautifulSoup(html_text, 'html.parser')
# #         all_vacancy = soup.find_all('div', attrs={'class': 'MoqhP _3rqtS'})
# #         for vacany in all_vacancy:
# #             data = {
# #                 'url': f"https://russia.superjob.ru/{vacany.find('a').get('href')}",
# #                 'title': vacany.find('a', attrs={'class': 'EruXX'}).text,
# #                 'company': vacany.find('div', attrs={'class': '_2nR82'}).text,
# #                 'skills': vacany.find('span', attrs={'class': '_27f3U Vdry2 _3ez7W _2RdtR _2oO_g'}).text,
# #                 'created': vacany.find('span', attrs={'class': '_27f3U Vdry2 _13MIX _2RdtR'}).text \
# #                     if 'Сегодня' not in vacany.find('span', attrs={'class': '_27f3U Vdry2 _13MIX _2RdtR'}).text \
# #                        and 'Вчера' not in vacany.find('span', attrs={'class': '_27f3U Vdry2 _13MIX _2RdtR'}).text \
# #                     else created_str
# #             }
# #
# #             lst_vacancy.append(data)
# #     return lst_vacancy
#
#
# # async def main():
# #     urls = get_all_url()
# #     vacancies = await get_content(urls)
# #
# #
# # if __name__ == '__main__':
# #     asyncio.run(main())
#
# created_date = datetime.date(2024, 6, 8)
# created_str = created_date.strftime("%d %B")
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#     'Referer': 'https://www.google.com/'
# }
# URL = 'https://russia.superjob.ru/vacancy/search/?keywords=Python&click_from=facet'
#
#
# def get_html(url):
#     response = requests.get(url, headers=headers)
#     return response.text
#
#
# def get_all_url():
#     return [f'https://russia.superjob.ru/vacancy/search/?keywords=Python&click_from=facet&page={i}' for i in
#             range(1, 3)]
#
#
# def get_content(lst):
#     lst_vacancy = []
#     print(lst)
#     for url in lst:
#         html_text = get_html(url)
#         soup = BeautifulSoup(html_text, 'html.parser')
#         all_vacancy = soup.select('div.1')
#         print(len(all_vacancy))
#         for vacancy in all_vacancy:
#             data = {
#                 'url': f"https://russia.superjob.ru/{vacancy.find('a').get('href')}",
#                 'title': vacancy.find('a', attrs={'class': 'EruXX'}).text,
#                 'company': vacancy.find('div', attrs={'class': '_2nR82'}).text,
#                 'skills': vacancy.find('span', attrs={'class': '_27f3U Vdry2 *3ez7W *2RdtR *2oO*g'}).text,
#                 'created': vacancy.find('span', attrs={
#                     'class': '_27f3U Vdry2 *13MIX *2RdtR'}).text if 'Сегодня' not in vacancy.find('span', attrs={
#                     'class': '_27f3U Vdry2 *13MIX *2RdtR'}).text and 'Вчера' not in vacancy.find('span', attrs={
#                     'class': '_27f3U Vdry2 *13MIX *2RdtR'}).text else created_str
#             }
#             lst_vacancy.append(data)
#     return lst_vacancy
#
#
# urls = get_all_url()
# vacancies = get_content(urls)
# print(vacancies)
