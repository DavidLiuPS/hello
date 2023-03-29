#tennis_api/tests.py
from django.test import TestCase
from django.conf import settings

class TennisTestCase(TestCase):

    def test_players_url_is_status_okay(self):
        response = self.client.get('/api/players/')
        self.assertEqual(200, response.status_code)

    def test_players_api_should_return_json(self):
        response = self.client.get('/api/players/')
        self.assertEqual('application/json', response['Content-Type'])
    
    def test_time_api_should_return_json(self):
        response = self.client.get('/api/players/')
        self.assertEqual('application/json', response['Content-Type'])

    def test_player_scores_are_status_okay(self):
        response = self.client.get('api/players/')
        player_1_score = self.client.get('api/players/')["player_1"]
        player_2_score = self.client.get('api/players/')["player_2"]
        self.assertTrue((player_1_score in settings.SCORES and player_2_score in settings.SCORES) or (
                        abs(player_1_score - player_2_score) == 1 and min(player_1_score, player_2_score) >= 3))

    def test_game_not_won(self):
        response = math.abs(self.client.get('api/players/')["player_1"] - self.client.get('api/players/')["player_2"])
        self.assertTrue(difference in settings.SCORES)

    #def test_player_2_is_status_okay(self):
    #    response = self.client.get('api/players/')["player_2"]
    #    #response = response.lower()
    #    self.assertTrue(response in settings.SCORES)