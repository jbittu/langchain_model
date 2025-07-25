from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model = GoogleGenerativeAI(model='gemini-2.0-flash')

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content = "Tell me in 5 sentences about langchain.")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result))

print(messages)

