import requests
import sys
import json


class Get:
    def __init__(self, url):
        self.url = url

    def eprint(self, *args, **kwargs):
        print(*args, file=sys.stderr, **kwargs)

    def unshorten_response(self):
        short_url_code = self.url.partition(".de/")[2]
        return requests.get(f'https://api.shrtco.de/v2/info?code={short_url_code}').text

    def get_unshorten(self):
        response = self.unshorten_response()
        data = json.loads(response)
        self.process_unshorten(data)

    def process_unshorten(self, data):
        full_url = data['result']['url']
        if data['ok']:
            print(f'\nThe full URL for {self.url} is:')
            print(f'\t{full_url}\n')
        else:
            print(data['error'])

    def shorten_response(self):
        return requests.post(f'https://api.shrtco.de/v2/shorten?url={self.url}').text

    def get_shorten(self):
        response = self.shorten_response()
        data = json.loads(response)
        self.process_shorten(data)

    def process_shorten(self, data):
        shurt_url = data['result']['full_short_link']
        if data['ok']:
            print(f'\nThe short URL for {self.url} is:')
            print(f'\t{shurt_url}\n')
        else:
            print(data['error'])
