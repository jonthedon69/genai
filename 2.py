import gensim.downloader as api

import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

import numpy as np

model = api.load("glove-wiki-gigaword-50")

words = ["computer", "internet", "software", "hardware", "disk", "robot", "data",

"network", "cloud", "algorithm"]

word_vectors = np.array([model[word] for word in words])

pca = PCA(n_components=2)

reduced_vectors = pca.fit_transform(word_vectors)

plt.figure(figsize=(8, 6))

for i, word in enumerate(words):

    plt.scatter(reduced_vectors[i, 0], reduced_vectors[i, 1])

    plt.annotate(word, (reduced_vectors[i, 0], reduced_vectors[i, 1]))

plt.title("PCA Visualization of Word Embeddings (Technology Domain)")

plt.xlabel("PCA Component 1")

plt.ylabel("PCA Component 2")

plt.show()

input_word = "computer" # You can change this to any word in your list

similar_words = model.most_similar(input_word, topn=5)

print(f"Words similar to '{input_word}':", similar_words)

