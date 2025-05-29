import gensim.downloader as api

model = api.load("glove-wiki-gigaword-50")

def construct_paragraph(seed_word, similar_words):

    paragraph = (

    f"In the spirit of {seed_word}, one might embark on an unforgettable {similar_words[0][0]}"f"to distant lands. Every {similar_words[1][0]} brings new challenges and opportunitiesfor{similar_words[2][0]}. "

    f"Through perseverance and courage, the {similar_words[3][0]} becomes a tale of triumph,muchlike an {similar_words[4][0]}."

    )

    return paragraph

seed_word = "adventure"

similar_words = model.most_similar(seed_word, topn=5)

paragraph = construct_paragraph(seed_word, similar_words)

print(paragraph)

from transformers import pipeline

import gensim.downloader as api

glove_model = api.load("glove-wiki-gigaword-50")

def get_similar_words(model, word, topn=5):

    return [w for w, _ in model.most_similar(word, topn=topn)]

generator = pipeline("text-generation", model="gpt2")

def generate_story(prompt, max_length=100):

    response = generator(prompt, max_length=max_length, num_return_sequences=1)

    return response[0]['generated_text']

seed_word = "adventure"

similar_words = get_similar_words(glove_model, seed_word, topn=5)

prompt = f"Write a story about {seed_word}, including elements of {', '.join(similar_words)}."

story = generate_story(prompt)

print(story)


