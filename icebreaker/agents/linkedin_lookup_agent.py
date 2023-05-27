from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from tools.tools import get_profile_url


'''lookup linkedin to get us the URL of the user'''
def lookup(name: str) -> str:
    # create chatopenAi with temp = 0 so that it's not too creative
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # create a prompt template stating exactly what we need to return 
    template = """given the full name {name_of_person} I want you to get it me a link to their linkedin profile page,
                  Your answer should contain only a URL"""

    tools_for_agent = [
        # tool name, function, description
        Tool(
            name="Crawl Google for linkedin profile page", 
            func=get_profile_url,
            description="useful for when you need to get linkedin",
        )
    ]

    # initialize the agent
    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )  # verbose login to be aware of each step b4 we login(reasoning process)

    # create the prompt template
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    linkedin_username = agent.run(prompt_template.format_prompt(name_of_person=name))
    return linkedin_username
