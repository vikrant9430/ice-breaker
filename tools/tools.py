from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name: str) -> str:
    """Get the profile URL of a user on Tavily."""
    try:
        search = TavilySearchResults()
        res = search.run(f"{name}")
        
        # Check if we have results and that 'url' exists
        if res and "url" in res[0]:
            return res[0]["url"]
        else:
            print(f"No valid URL found for {name}.")
            return None
    except IndexError:
        # Handles the case where no results are returned
        print(f"No results found for {name}.")
        return None
    except Exception as e:
        # Handles any other unexpected errors
        print(f"An error occurred while searching for {name}: {e}")
        return None