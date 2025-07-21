from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-large", dimension=32)

document = [
    "What is the capital of India?",
    "The capital of India is New Delhi.",
    "India is a country in South Asia.",
    "New Delhi is the capital city of India.",
    "India's capital is New Delhi, known for its rich history and culture."
]

result = embedding.embed_documents(document)

print(str(result))

