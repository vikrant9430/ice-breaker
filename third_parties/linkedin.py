import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    Scrape information from LinkedIn Profiles, Manually Scrape the information from the LinkedIn Profile.
    """
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/vikrant9430/97f179e2089f7aeb6b4a149b104183c3/raw/b406d206beeb65d0579438dce872ddb78c483cc3/vikrant-nandan.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dic,
            timeout=10,
        )
    data = response.json()
    
    data = {
        k:v for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    
    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/vikrant-nandan/", mock=True
    )
          )
    