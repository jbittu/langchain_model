from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
    
model = ChatOpenAI(model = "gpt-4", temperature=0.7, max_completion_tokens=100)

res = model.invoke("What is the capital of India?")
print("Model response:", res)
print(res.content)