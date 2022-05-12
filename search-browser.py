#!/usr/bin/env python3

import datetime
import webbrowser


def main():
    GOOGLE = 'https://www.google.com/search?q={query}'
    DUCK_DUCK_GO = 'https://duckduckgo.com/?q={query}&ia=web'
    LOG_DATA = '{url} | {query}'

    url = DUCK_DUCK_GO
    query = input('Input search query:\n').strip()
    webbrowser.open_new(url.format(query=query))
    write_log(LOG_DATA.format(query=query, url=url))


def write_log(log: str) -> None:
    LOG_FILE = 'search_browser_log.txt'
    with open(LOG_FILE, 'a', encoding='utf-8') as log_file:
        print(datetime.datetime.now(), '|', log, file=log_file)


if __name__ == '__main__':
    main()
