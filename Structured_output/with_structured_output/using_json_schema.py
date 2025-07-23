from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, EmailStr, Field
from typing import Annotated, Optional, Literal

from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

## Schema for structured output 
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}

structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke(
    """I recently watched the movie 'Inception'. It was a mind-bending thriller that kept me on the edge of my seat. The plot was complex but intriguing, and the visuals were stunning. I would highly recommend it to anyone who enjoys science fiction and psychological thrillers. Overall, I would give it a 9/10 for its originality and execution. but I felt the ending was a bit confusing and left me with more questions than answers. The acting was top-notch, especially Leonardo DiCaprio's performance. The soundtrack was also fantastic, adding to the overall atmosphere of the film. 
    reviewer name: John Doe""")

print(result)
print(type(result))