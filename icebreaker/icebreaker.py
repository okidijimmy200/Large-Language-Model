from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup
from output_pacers import person_intel_parser, PersonIntel
from typing import Tuple


def ice_breaker(name: str) -> Tuple[PersonIntel, str]:
    print("langchain")

    '''perform the linkedin lookuo'''
    linkedin_profile_url = lookup(name)

    summary_template = """
        given the linkedin information {information} about a person from I want to create:
        1. a short summary
        2. two interesting facts about them
        \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], 
        template=summary_template,
        partial_variables={'format_instructions': person_intel_parser.get_format_instructions() }
    )

    # temperature determines how creative the model is going to be, 0 not too creative
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # chain and run the llm in a chain
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    result = chain.run(information=linkedin_data)
    return person_intel_parser.parse(result), linkedin_data.get("profile_pic_url")


# if __name__ == "__main__":
#     ice_breaker("Eden Marco")