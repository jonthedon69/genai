!pip install langchain langchain-community cohere google-auth google-auth-oauthlib google-auth-httplib2 googleapiclient

import os

from cohere import Client

from langchain.prompts import PromptTemplate



os.environ["COHERE_API_KEY"] = "3JE437qflNp5M7TbvoQXMmeDuRrRWgylGCq09x29"

co = Client(os.getenv("COHERE_API_KEY"))



text_document = """

Machine learning is a subset of artificial intelligence that focuses on training algorithms 

to make predictions. It is widely used in industries like healthcare, finance, and retail.

"""



template = """

You are an expert summarizer. Summarize the following text in a concise manner:

Text: {text}

Summary:

"""

prompt_template = PromptTemplate(input_variables=["text"], template=template)

formatted_prompt = prompt_template.format(text=text_document)



response = co.generate(

    model="command",

    prompt=formatted_prompt,

    max_tokens=50

)



print("Summary:")

print(response.generations[0].text.strip())



