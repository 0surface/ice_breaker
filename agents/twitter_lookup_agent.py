from dotenv import load_dotenv
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from tools.tools import get_profile_url_tavily

load_dotenv()


def lookup(name: str) -> str:
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0
    )
    template = """
    given the name {name_of_person} I want you to find a link to their Twitter profile page, and extract from it their 
    username. In Your Final answer should only have the person's username.
    """
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 twitter profile page",
            func=get_profile_url_tavily,
            description="useful for when you need yo get the X Page URL"
             )
    ]
    react_prompt = hub.pull('hwchase17/react')
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    twitter_profile_url = result["output"]
    return twitter_profile_url


if __name__ == "__main__":
    twitter_url = lookup(name="Eden Marco")
    print(twitter_url)
