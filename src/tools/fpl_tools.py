import requests
from smolagents import tool
from typing import List, Dict


@tool
def get_fpl_player_data() -> List[Dict]:
    """Fetches player data from the FPL API, including form from the last 5 games."""
    url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    response = requests.get(url)
    data = response.json()
    players = data["elements"]
    teams = {team["id"]: team["name"] for team in data["teams"]}

    player_list = []
    for player in players:
        summary_url = (
            f"https://fantasy.premierleague.com/api/element-summary/{player['id']}/"
        )
        summary_response = requests.get(summary_url)
        summary_data = summary_response.json()
        history = summary_data["history"][-5:]
        form_last_5 = sum(game["total_points"] for game in history) / max(
            len(history), 1
        )

        player_list.append(
            {
                "id": player["id"],
                "name": f"{player['first_name']} {player['second_name']}",
                "position": player["element_type"],
                "cost": player["now_cost"] / 10,
                "total_points": player["total_points"],
                "form_last_5": form_last_5,
                "team_id": player["team"],
                "team_name": teams[player["team"]],
            }
        )
    return player_list


@tool
def get_fpl_fixtures() -> Dict:
    """Fetches fixture data for the current gameweek, accounting for double gameweeks and home/away."""
    url = "https://fantasy.premierleague.com/api/fixtures/"
    response = requests.get(url)
    data = response.json()
    current_gw = min(
        [f["event"] for f in data if not f["finished"] and f["event"] is not None]
    )

    team_fixtures = {}
    for fixture in data:
        if fixture["event"] == current_gw:
            team_h, team_a = fixture["team_h"], fixture["team_a"]
            team_fixtures.setdefault(team_h, []).append(
                {
                    "opponent": team_a,
                    "difficulty": fixture["team_h_difficulty"],
                    "is_home": True,
                }
            )
            team_fixtures.setdefault(team_a, []).append(
                {
                    "opponent": team_h,
                    "difficulty": fixture["team_a_difficulty"],
                    "is_home": False,
                }
            )

    difficulty_map = {}
    for team_id, fixtures in team_fixtures.items():
        total_difficulty = sum(f["difficulty"] for f in fixtures)
        avg_difficulty = total_difficulty / len(fixtures)
        home_count = sum(1 for f in fixtures if f["is_home"])
        difficulty_map[team_id] = avg_difficulty - (0.5 * home_count / len(fixtures))

    return {
        "current_gw": current_gw,
        "team_fixtures": team_fixtures,
        "difficulty_map": difficulty_map,
    }
