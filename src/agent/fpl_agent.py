from smolagents import CodeAgent, HfApiModel, DuckDuckGoSearchTool
from ..tools.fpl_tools import get_fpl_player_data, get_fpl_fixtures


def create_fpl_agent(api_key: str) -> CodeAgent:
    """Creates and configures the FPL team selection agent."""
    model = HfApiModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct", token=api_key)
    search_tool = DuckDuckGoSearchTool()

    system_prompt = """
You are an autonomous Fantasy Premier League (FPL) team selection agent.
Your task is to select an optimal team for the current gameweek within a £100m budget.
The team must follow these rules:
- 2 Goalkeepers (position 1)
- 5 Defenders (position 2)
- 5 Midfielders (position 3)
- 3 Forwards (position 4)
- Maximum of 3 players from any single Premier League team (use team_id to track).
- Select a starting 11 (1 GK, at least 3 DEF, at least 1 FWD, rest any position) and 4 substitutes.
- Maximize predicted points, weighting players by:
  - Form: Use 'form_last_5' (average points from the last 5 games) from get_fpl_player_data.
  - Fixture Difficulty: Use 'difficulty_map' from get_fpl_fixtures (lower is better; accounts for double gameweeks and home/away status).
  - Web Context: Use DuckDuckGoSearchTool to search for additional context (e.g., 'FPL Gameweek {current_gw} injury news',
  'Player X injury status', or 'FPL expert picks Gameweek {current_gw}'). Adjust player selection if injuries or expert insights
  suggest a player is unavailable or underperforming. Employ this for the first 11 team, and captain only.
- Tools available:
  - get_fpl_player_data: Player stats and form.
  - get_fpl_fixtures: Fixture data and difficulty.
  - DuckDuckGoSearchTool: Web search for real-time context.
- From the starting 11, choose a captain with the highest score of (form_last_5 / difficulty).
Return a Python script that:
- Defines the team as a list of dictionaries (name, position, cost, team_name, predicted_points, starting, captain).
- Prints the team, total cost, total predicted points, and captain name.
Ensure the script is executable and respects all constraints.
"""

    prompt_templates = {"system_prompt": system_prompt}
    return CodeAgent(
        model=model,
        prompt_templates=prompt_templates,
        tools=[search_tool, get_fpl_player_data, get_fpl_fixtures],
        max_steps=10,
    )
