import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent, 
    AgentExecutor)

from tools.tools import get_profile_url_tavily
from langchain import hub
import warnings
from dotenv import load_dotenv
load_dotenv()


def lookup(name: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo",
    )
    
    template = """Given the full name {name_of_person} 
    I want you to get it me a link to their Linkedin Profile page. Your answers should contain only a URL."""
    
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    
    tools_for_agents = [
        Tool(
            name = "Crawl Google 4 Linkedin profile page",
            func=get_profile_url_tavily,
            description="Useful for when you need get the linkedin page URL"
        )
    ]
    
    react_prompt = hub.pull("hwchase17/react")
    
    agent = create_react_agent(llm=llm, tools=tools_for_agents, prompt=react_prompt)
    
    agent_executer = AgentExecutor(agent=agent, tools=tools_for_agents, verbose=True)
    
    result = agent_executer.invoke(
        input = {"input": prompt_template.format_prompt(name_of_person=name)}
    )
    
    linkedin_profile_url = result["output"]
    
    return linkedin_profile_url

    
if __name__ == "__main__":
    linkedin_url = lookup(name="Vikrant Nandan")
    print (linkedin_url)