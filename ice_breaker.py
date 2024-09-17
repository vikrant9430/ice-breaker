import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from third_parties.linkedin import scrape_linkedin_profile


# Load environment variables from .env file
load_dotenv()

# Now the OpenAI API key should be accessible via os.getenv
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key is missing. Ensure it's set in the .env file.")

if __name__ == '__main__':
    print('Hello Langchain')
    
    summary_template = """
    Given the Linkedin Information {information} about a person, create:
    1. A Short Summary
    2. Two interesting facts about them
    """
    
    
    
    summary_prompt_template = PromptTemplate(input_variables=['information'], template=summary_template)

    # Initialize the OpenAI LLM with the API key
    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=api_key)
    
    # Initialize the ChatOllama model
    # llm = ChatOllama(model="llama3.1")
    llm = ChatOllama(model="mistral")
    
    # Create the chain
    chain = summary_prompt_template | llm | StrOutputParser()
    
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/vikrant-nandan/", mock=True
    )
    
    # Run the chain with the provided information
    res = chain.invoke(input={"information": linkedin_data})
    
    # Print the result
    print(res)