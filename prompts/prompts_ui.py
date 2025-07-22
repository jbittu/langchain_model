from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
st.header('Summarizer Tool')


## STATIC PROMPT
# user_input = st.text_input("Enter text here:")

# if st.button("Summarize"):
#     result = model.invoke(user_input)  
#     st.write(result.content)

## DYNAMIC PROMPT
# paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )
# style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 
# length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )
# #template
# template = PromptTemplate(
#     template="""
# please summarize the research paper '{paper_input}' in a {length_input} manner, suitable for a {style_input} audience.
# 1. Mathematical Details:
#     - Include relevant key equations and mathematical concepts if present in paper.
#     - Provide intuitive explanations for each equation and concept.
# 2. Anologies:
#     - Use analogies to explain complex concepts in a way that is easy to understand.
# if certain information is not present in the paper, response with inssuficient information.
# """,
# input_variables=["paper_input", "length_input","style_input"])
# prompt = template.invoke(
#     {
#         "paper_input": paper_input,
#         "length_input": length_input,
#         "style_input": style_input
#     }
# )
# if st.button("Summarize"):
#     result = model.invoke(prompt)
#     st.write(result.content)
    

# DYNAMIC PROMPT WITH TEMPLATE JSON FILE
paper_input = st.selectbox("Select Research Paper Name", ["Attention Is All You Need",
                                                           "BERT: Pre-training of Deep Bidirectional Transformers",
                                                           "GPT-3: Language Models are Few-Shot Learners",
                                                           "Diffusion Models Beat GANs on Image Synthesis"])
style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])
length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

# Template
template = load_prompt('prompts/template.json')

prompt = template.invoke(
    {
        "paper_input": paper_input,
        "length_input": length_input,
        "style_input": style_input
    }
)

if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)


## using chain

# if st.button('Summarize'):
#     chain = template | model
#     result = chain.invoke({
#         'paper_input':paper_input,
#         'style_input':style_input,
#         'length_input':length_input
#     })
#     st.write(result.content)