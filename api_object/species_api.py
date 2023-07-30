from utils.api_base import ApiBase
import os

DOMAIN = os.getenv('DOMAIN')


class FilmsApi(ApiBase):
    def __init__(self, session, target=0):
        url = f'https://{DOMAIN}/api/films/{target}/'
        super().__init__(session, url)

    def send(self):
        self.api_request('get')

    def sort_films_by_episode_id(self):
        self.url = f'https://{DOMAIN}/api/films/'
        self.send()

        films = self.response.json()['results']
        result = [None] * len(films)
        for film in films:
            result[film['episode_id']-1] = film['title']

        return result





