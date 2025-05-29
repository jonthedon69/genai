pip install gensim

import gensim.downloader as api

model = api.load("glove-wiki-gigaword-50")

word1 = "king"

word2 = "man"

word3 = "woman"

result_vector = model[word1] - model[word2] + model[word3]

predicted_word = model.most_similar([result_vector], topn=2)

print(f"Result of '{word1} - {word2} + {word3}' is: {predicted_word[1][0]}")



