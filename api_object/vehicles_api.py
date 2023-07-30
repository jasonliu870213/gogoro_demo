from utils.api_base import ApiBase
import os

DOMAIN = os.getenv('DOMAIN')

class VehiclesApi(ApiBase):
    def __init__(self, session, target=0):
        url = f'https://{DOMAIN}/api/vehicles/{target}/'
        super().__init__(session, url)

    def send(self):
        self.api_request('get')

    def filter_vehicles_by_max_atmsp_speed(self, target):
        self.url = f'https://{DOMAIN}/api/vehicles/'
        result = []

        while self.url is not None:
            self.send()
            response = self.response.json()

            vehicles = response['results']
            for vehicle in vehicles:
                if vehicle['max_atmosphering_speed'] != 'unknown':
                    if int(vehicle['max_atmosphering_speed']) > target:
                        result.append(vehicle['name'])

            self.url = response['next']

        return result






