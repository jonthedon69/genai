from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

sentences = [

"I love this product! It works perfectly.",

"This is the worst experience I've ever had.",

"The weather is nice today.",

"I feel so frustrated with this service."

]

results = sentiment_pipeline(sentences)

for sentence, result in zip(sentences, results):

    print(f"Sentence: {sentence}")

    print(f"Sentiment: {result['label']}, Confidence:{result['score']:.4f}")

    print()

