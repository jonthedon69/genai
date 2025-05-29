from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

passage = "Machine learning is a subset of artificial intelligence that focuses on training algorithmsto make predictions. It is widely used in industries like healthcare, finance, and retail."

summary = summarizer(passage, max_length=30, min_length=10, do_sample=False)

print("Summary:")

print(summary[0]['summary_text'])

