!pip install cohere pypdf ipywidgets

import cohere

from pypdf import PdfReader

import getpass



COHERE_API_KEY = "3JE437qflNp5M7TbvoQXMmeDuRrRWgylGCq09x29"

co = cohere.Client(COHERE_API_KEY)



reader = PdfReader("./IPC_186045.pdf")

ipc_text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])



def ask_ipc(question):

    prompt = f"""

You are a legal assistant specialized in the Indian Penal Code (IPC).

Use the following content to answer the user's question:



{ipc_text[:10000]}



User Question: {question}



Respond with a relevant IPC section (if any) and a clear explanation.

"""

    response = co.generate(prompt=prompt, model="command-r-plus", max_tokens=300)

    print("\n" + response.generations[0].text.strip())



# Ask in console

user_input = input("Ask your IPC question: ")

ask_ipc(user_input)



