#!/usr/bin/env python3
import datetime
import webbrowser

SEARCH_ENGINE_URL = {
    'GOOGLE': 'https://www.google.com/search?q={query}',
    'DUCK_DUCK_GO': 'https://duckduckgo.com/?q={query}&ia=web',
}

LOG_FORMAT = '{url} | {query}'
LOG_FILE = 'search_browser_log.txt'


def write_log(file:str, log:str) -> None:
    with open(file, 'a', encoding='utf-8') as file:
        print(datetime.datetime.now(), '|', log, file=file)


def main():
    query = input('Input search query:\n').strip()
    url = SEARCH_ENGINE_URL['GOOGLE'].format(query=query)
    webbrowser.open_new(url)
    write_log(LOG_FILE, LOG_FORMAT.format(query=query, url=url))


if __name__ == '__main__':
    main()
