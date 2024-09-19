import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama

## Function To get response from Ollama model

def get_ollama_response(input_text, no_words, blog_style):
    ### Ollama model (using Llama 3)
    llm = Ollama(model='mistral')

    ## Prompt Template
    template = """
        Create an engaging blog post aimed at {blog_style} about the topic '{input_text}'. 
        The post should feel personal and relatable, encouraging readers to connect with the subject. 
        Aim for a length of approximately {no_words} words, and include real-world examples or anecdotes where possible.
    """
    
    prompt = PromptTemplate(input_variables=["blog_style", "input_text", 'no_words'],
                            template=template)
    
    ## Generate the response from the Ollama model
    response = llm.invoke(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    return response

st.set_page_config(page_title="Generate Blogs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

## Creating two more columns for additional fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for',
                               ('Researchers', 'Data Scientist', 'Common People'), index=0)

submit = st.button("Generate")

## Final response
if submit:
    st.write(get_ollama_response(input_text, no_words, blog_style))
