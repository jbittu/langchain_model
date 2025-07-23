from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, EmailStr, Field
from typing import Annotated, Optional, Literal

from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

## Schema for structured output 
class Review(BaseModel):
    Key_things : Annotated[list[str], Field(description="Key things to note about the movie")]
    summary: Annotated[str, Field(description="A brief summary of the movie")]
    sentiment: Annotated[Literal["positive", "neutral", "negative"], Field(description="Return sentiment of the review either positive, neutral or negative")]
    pros: Annotated[Optional[list[str]], Field(default=None, description="Pros of the movie in list format")]
    cons: Annotated[Optional[list[str]], Field(default=None, description="Cons of the movie in list format")]
    name: Annotated[Optional[str], Field(default=None, description="Name of the reviewer")]


structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
    """I recently watched the movie 'Inception'. It was a mind-bending thriller that kept me on the edge of my seat. The plot was complex but intriguing, and the visuals were stunning. I would highly recommend it to anyone who enjoys science fiction and psychological thrillers. Overall, I would give it a 9/10 for its originality and execution. but I felt the ending was a bit confusing and left me with more questions than answers. The acting was top-notch, especially Leonardo DiCaprio's performance. The soundtrack was also fantastic, adding to the overall atmosphere of the film. 
    reviewer name: John Doe""")

print(result)
print(type(result))