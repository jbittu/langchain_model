from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=0.5)

result = model.invoke('write me a short poem of 5 lines about a robot learning to dance')

print(result.content)