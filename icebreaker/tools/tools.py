from langchain.serpapi import SerpAPIWrapper
from langchain.agents import tool


# create our custom tool
@tool  # turn func into tool agent can use
def get_profile_url(text: str) -> str:
    """search for linkedin profile page."""
    search = SerpAPIWrapper()
    res = search.run(f"{text}")
    return res
