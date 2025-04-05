# WIP: FPL Team Selection Agent: fpl-gameweek-guru

An autonomous agent built with the HuggingFace `smolagents` framework to select an optimal Fantasy Premier League team.

## Features

- Selects a 15-player team within a £100m budget.
- Limits to 3 players per team.
- Uses form (last 5 games), fixture difficulty (double gameweeks, home/away), and a greedy fallback.
- Incorporates web search via DuckDuckGoSearchTool for injury news and expert insights.
- Chooses a captain based on form and fixture difficulty.
- Provides a Gradio-based interactive UI for team generation.

## Setup

1. Install `uv`:  
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
2. Navigate to `fpl-gameweek-guru/`.
3. Create a virtual environment and install dependencies:  
    ```bash
    uv sync
    ```
4. Add your Hugging Face API key in `src/main.py` as an environment variable for security.
5. Run:  
    ```bash
    uv run python src/main.py
    ```

## Structure

- `src/tools/fpl_tools.py`: API tools.
- `src/agent/fpl_agent.py`: Agent logic.
- `src/main.py`: Entry point.
- `Gradio_UI.py`: Defines the Gradio-based user interface.
- `pyproject.toml`: Project metadata and dependencies.

## Deployment on Hugging Face Spaces

### Prepare the Space:

1. Select "Gradio" as the SDK when creating the Space.
2. Upload all project files, including `Gradio_UI.py`, `src/`, and `requirements.txt`.
3. Add `requirements.txt` to support deployment to spaces with the following dependencies:
    ```
    gradio
    smolagents
    requests
    python-dotenv
    ```

### Run the Space:

The Gradio app will launch automatically and be accessible via the Space URL.

## Notes

- The agent uses the `Qwen/Qwen2.5-Coder-32B-Instruct` model for reasoning.
- Ensure your Hugging Face API key has sufficient quota for model inference.

## Future Enhancements

- Add support for additional FPL rules and constraints.
- Improve the agent's reasoning with more advanced models.
