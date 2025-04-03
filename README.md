# FPL Team Selection Agent: fpl-gameweek-guru

An autonomous agent built with the HuggingFace `smolagents` framework to select an optimal Fantasy Premier League team.

## Features
- Selects a 15-player team within a £100m budget.
- Limits to 3 players per team.
- Uses form (last 5 games), fixture difficulty (double gameweeks, home/away), and a greedy fallback.
- Incorporates web search via DuckDuckGoSearchTool for injury news and expert insights.
- Chooses a captain based on form and fixture difficulty.

## Setup
1. Install `uv`: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Navigate to `fpl-gameweek-guru/`.
3. Create virtual environment and install dependencies: `uv sync`
4. Add your Hugging Face API key in `src/main.py` as an environment variable for security.
5. Run: `uv run python src/main.py`

## Structure
- `src/tools/fpl_tools.py`: API tools.
- `src/agent/fpl_agent.py`: Agent logic.
- `src/main.py`: Entry point.
- `pyproject.toml`: Project metadata and dependencies.