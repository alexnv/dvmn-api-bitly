import argparse

import requests
import os
from urllib.parse import urlparse


def shorten_link(token, url):
  api_url = "https://api-ssl.bitly.com/v4/shorten"
  payload = {"long_url": url}
  headers = {'Authorization': f'Bearer {token}'}
  response = requests.post(api_url, headers=headers, json=payload)
  response.raise_for_status()
  short_url = response.json()['link']

  return short_url


def count_clicks(token, url):
  parsed_url = urlparse(url)
  bitlink = f'{parsed_url.hostname}{parsed_url.path}'

  api_url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
  headers = {'Authorization': f'Bearer {token}'}
  response = requests.get(api_url, headers=headers)
  response.raise_for_status()

  return response.json()['total_clicks']


def is_bitlink(token, url):
  parsed_url = urlparse(url)
  bitlink = f'{parsed_url.hostname}{parsed_url.path}'

  api_url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}"
  headers = {'Authorization': f'Bearer {token}'}
  response = requests.get(api_url, headers=headers)
  return response.ok

def create_argument_parser():
  parser = argparse.ArgumentParser(
    description='Возвращает короткую ссылку через сервис bit.ly, либо выводит количество переходов по ранее сокращенной ссылке'
  )
  parser.add_argument('url', nargs='?')

  return parser

def main():
  token = os.getenv("BITLY_TOKEN")
  if token:
    argument_parser = create_argument_parser()
    program_aguments = argument_parser.parse_args()
    if program_aguments.url:
      url_to_shorten = program_aguments.url
    else:
      url_to_shorten = input("Введите ссылку для сокращения: ")

    try:
      if is_bitlink(token, url_to_shorten):
        print("Количество кликов: ", count_clicks(token, url_to_shorten))
      else:
        bitlink = shorten_link(token, url_to_shorten)
        print('Битлинк', bitlink)
    except requests.exceptions.HTTPError:
      print("Введены не верные данные, либо достигнут лимит ссылок")

  else:
    print("Не указана переменная окружения BITLY_TOKEN")


if __name__ == "__main__":
  main()
