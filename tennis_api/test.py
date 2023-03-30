#tennis_api/tests.py
from django.test import TestCase
from django.conf import settings

class TennisTestCase(TestCase):

    def test_players_url_is_status_okay(self):
        response = self.client.get('/api/players_api/')
        self.assertEqual(200, response.status_code)

    def test_players_api_should_return_json(self):
        response = self.client.get('/api/players_api/')
        self.assertEqual('application/json', response['Content-Type'])


    def valid_game(self):
        response = self.client.get('/api/players_api/')
        test = response.json()
        print(test)
        lst_scores = list(test.values())
        diff = abs(lst_scores[0] - lst_scores[1])
        self.assertTrue((lst_scores[0] in settings.SCORES and lst_scores[1] in settings.SCORES) or (
                        abs(lst_scores[0] - lst_scores[1]) == 1 and min(lst_scores[0], lst_scores[1]) >= 3))
