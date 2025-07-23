from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=0.9)

result = model.invoke("give me 5 line of poem on cricket")

print(result.content)
