from api_object.species_api import FilmsApi
from api_object.vehicles_api import VehiclesApi
import allure


@allure.story("Question 1")
def test_question_1(session):
    films_api = FilmsApi(session, 6)
    films_api.send()
    result = len(films_api.response.json()['species'])

    assert films_api.response.status_code == 200
    assert result == 20


@allure.story("Question 2")
def test_question_2(session):
    films_api = FilmsApi(session)
    result = films_api.sort_films_by_episode_id()

    assert result == ['The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith', 'A New Hope', 'The Empire Strikes Back', 'Return of the Jedi', 'The Force Awakens']


@allure.story("Question 3")
def test_question_3(session):
    vehicles_api = VehiclesApi(session, 4)
    result = vehicles_api.filter_vehicles_by_max_atmsp_speed(1000)

    assert result == ['T-16 skyhopper', 'TIE/LN starfighter', 'Storm IV Twin-Pod cloud car', 'TIE/IN interceptor', 'Vulture Droid', 'Geonosian starfighter', 'Droid tri-fighter']

