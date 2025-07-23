from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict
from pydantic import BaseModel
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

##Schema for structured output dictionary
class Review(BaseModel):
    summary: str
    sentiment: str
    



structured_model = model.with_structured_output(Review)


info = """I recently watched the movie 'Inception'. It was a mind-bending thriller that kept me on the edge of my seat. The plot was complex but intriguing, and the visuals were stunning. I would highly recommend it to anyone who enjoys science fiction and psychological thrillers. Overall, I would give it a 9/10 for its originality and execution.
"""
result = structured_model.invoke(info)


print(result)
print(type(result))
print(result.summary)
print(result.sentiment)

