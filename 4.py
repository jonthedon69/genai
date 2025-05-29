pip install gensim openai nltk

pip install transformers

pip install hf_xet

from transformers import pipeline

import gensim.downloader as api

glove_model = api.load("glove-wiki-gigaword-50")

word = "technology"

similar_words = glove_model.most_similar(word, topn=5)

print(f"Similar words to '{word}': {similar_words}")

generator = pipeline("text-generation", model="gpt2")

def generate_response(prompt, max_length=100):

    response = generator(prompt, max_length=max_length, num_return_sequences=1)

    return response[0]['generated_text']

original_prompt = "Explain the impact of technology on society."

original_response = generate_response(original_prompt)

enriched_prompt = "Explain the impact of technology, innovation, science, engineering, and digital advancements on society."

enriched_response = generate_response(enriched_prompt)

print("Original Prompt Response:")

print(original_response)

print("\nEnriched Prompt Response:")

print(enriched_response)

