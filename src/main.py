from .agent.fpl_agent import create_fpl_agent
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    HF_API_KEY = os.getenv("HF_API_KEY")

    agent = create_fpl_agent(HF_API_KEY)
    response = agent.run(
        "Generate a Fantasy Premier League team for the current gameweek."
    )

    print(response)


if __name__ == "__main__":
    main()
