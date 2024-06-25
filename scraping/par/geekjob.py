import requests
import json


def get_page(page: int):
    headers = {
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'sid=s%3Aa282111d097abd86a63f551d02bbe091.Vb3lhUOtv7gdTaw1uD7xwCs0jG%2FbyY2xg%2Fux33Vawoo; _fp=56adac73fb54132149301836f1a8a658; suid=udEcaGZjn+EHzAAVS8vwAg==; _ym_uid=1717805031988125254; _ym_d=1717805031; _cgdprb=1; _gid=GA1.2.929121557.1719347005; cf_clearance=4lDXlHNCLyX3DPUXqmUKOF0iEy81Z5R9FQ1ObDgjz5o-1719347006-1.0.1.1-iCzYT5R4aicXN1dJSykLpVaDAQuix_HfYt1OMgPiw2PM6Z3vHLgfZuF_1ZSWWnXnyYjgCJ41AOLlOc5UYl71DQ; _ym_isad=1; _gat_gtag_UA_147026738_1=1; _ga=GA1.1.1690865399.1717805030; _ga_G4VTDCYF96=GS1.1.1719347005.5.1.1719347258.0.0.0',
        'priority': 'u=1, i',
        'referer': 'https://geekjob.ru/vacancies?qs=python',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }
    params = {
        'page': f'{page}',
        'qs': 'python',
    }
    response = requests.get('https://geekjob.ru/json/find/vacancy', params=params, headers=headers)

    return response.json()


def get_content(rest_json: json):
    lst = []
    for i in rest_json['data']:
        vacancy = {
            'url': f'https://geekjob.ru/vacancy/{i["id"]}',
            'title': i['position'],
            'company': i["company"]["name"],
            'created': i["log"]["modify"]
        }
        lst.append(vacancy)
    return lst


