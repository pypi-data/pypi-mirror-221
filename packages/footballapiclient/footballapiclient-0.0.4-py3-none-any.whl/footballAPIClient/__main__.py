from footballAPIClient import footballAPI

import requests
import time


def players_data(league, season, page=1, player_data_list=None):
    if player_data_list is None:
        player_data_list = []

    players = fp.get_player(league=league, season=season, page=page)
    # call_api('players', {'league': league, 'season': season, 'page': page})
    player_data_list.extend(players['response'])

    if players['paging']['current'] < players['paging']['total']:
        next_page = players['paging']['current'] + 1
        if next_page % 2 == 1:
            time.sleep(1)
        player_data_list = players_data(league, season, next_page, player_data_list)

    return player_data_list


fp = footballAPI.FootballAPI("api-sports", "ce93fa521937b7ca038a4ead76d8668f")
# Get all the teams from this competition
# teams = call_api('teams', {'league': 39, 'season': 2021})
# print(teams) # To display the results if necessary

# Get all the players from this competition
# players = players_data(39, 2021)
# print(players)  # To display the results if necessary
print(fp.get_status())
