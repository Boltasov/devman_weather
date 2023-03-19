import requests
import os
import json
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(token, url):
    full_token = 'Bearer ' + token
    bitly_url = 'https://api-ssl.bitly.com/v4/shorten'
    full_link_json = json.dumps({'long_url': url})
    headers = {
      'Authorization': full_token,
      'Content-Type': 'application/json',
    }

    response = requests.post(bitly_url, headers=headers,
                             data=full_link_json)
    response.raise_for_status()

    return response.json()['link']


def count_clicks(token, url):
    full_token = 'Bearer ' + token
    parsed = urlparse(url)
    bitly_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}{}/clicks/summary'\
                .format(parsed.hostname, parsed.path)
    headers = {
      'Authorization': full_token,
    }

    response = requests.get(bitly_url, headers=headers)
    response.raise_for_status()

    clicks_count = response.json()['total_clicks']

    return clicks_count


def is_bitlink(url, token):
    full_token = 'Bearer ' + token
    parsed = urlparse(url)
    bitly_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}{}'\
                .format(parsed.hostname, parsed.path)

    headers = {
      'Authorization': full_token,
    }

    response = requests.get(bitly_url, headers=headers)

    return response.ok


def main():
    parser = argparse.ArgumentParser(
        description='Программа делает из простой ссылки битлинк,\n \
                    а для, битлинка считает количество переходов'
    )
    parser.add_argument('url', help='Ваша ссылка')
    namespace = parser.parse_args()
    url = namespace.url

    load_dotenv()
    token = os.getenv('BITLY_TOKEN')

    if is_bitlink(url, token):
        try:
            clicks_count = count_clicks(token, url)
            print('Количество кликов по ссылке: ', clicks_count)
        except requests.exceptions.HTTPError as error:
            print('Не удалось подсчитать количество кликов.\n \
            Проверьте корректность введённой ссылки\n\n', error)
    else:
        try:
            short_link = shorten_link(token=token, url=url)
            print('Битлинк ', short_link)
        except requests.exceptions.HTTPError as error:
            print('Не удалось сократить ссылку\n\n', error)


if __name__ == '__main__':
    main()