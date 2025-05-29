!pip install gensim nltk

import gensim

from gensim.models import Word2Vec

import nltk

from nltk.tokenize import word_tokenize



nltk.download('punkt')



corpus = [

    "A patient with diabetes requires regular insulin injections.",

    "Medical professionals recommend exercise for heart health.",

    "Doctors use MRI scans to diagnose brain disorders.",

    "Antibiotics help fight bacterial infections but not viral infections.",

    "The surgeon performed a complex cardiac surgery successfully.",

    "Doctors and nurses work together to treat patients.",

    "A doctor specializes in diagnosing and treating diseases."

]



tokenized_corpus = [word_tokenize(sentence.lower()) for sentence in corpus]



model = Word2Vec(

    sentences=tokenized_corpus,

    vector_size=100,

    window=3,

    min_count=1,

    workers=4,

    sg=1  

)



#model.save("medical_word2vec.model")



similar_words = model.wv.most_similar("doctor", topn=5)



print("Top 5 words similar to 'doctor':")

for word, score in similar_words:

    print(f"{word}: {score:.4f}")



