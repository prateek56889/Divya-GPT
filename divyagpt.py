import streamlit as st
import google.generativeai as model
from matplotlib import pyplot as plt
import matplotlib

model.configure(api_key=st.secrets["GEN_API"])

def prompts():
    return """
    Hi buddy I am giving you some names you have to filter them out and generate accordingly
    1. Title of the given prompt (use your intellect for it)
    2. Overview of that topic
    3. Summary of that topic
    4. Important keywords of that topic
    5. Glossary or hard words
    6. Questions and answers up to 5
    """



def gemini_res(input, prompt):
    """
    This has to get in return through Gemini
    """
    gemini = model.GenerativeModel("gemini-pro")
    res = gemini.generate_content([input, prompt])
    return res.text



st.set_page_config(page_title="Divya GPT", page_icon="div.png")
st.image("divya.png")

inp = st.text_area(label="Enter the Topic to generate")
response = gemini_res(input=prompts(), prompt=inp)

gen_per = st.button(label="Generate")
if gen_per:
    st.write(response)
    
    st.sidebar.image("favicon.svg")
    st.sidebar.title("Wanna download your important Topics?")
    st.sidebar.subheader("DivyaGPT offers Download the chat option")
    st.sidebar.download_button("Download Chats", response, file_name="summarise.txt")
    
    st.sidebar.title("Get's hard to understand Text?")
    st.sidebar.subheader("Don't worry Divya GPT too provides ASCII-based flowcharts. Wanna check?")
    flow = gemini_res(input="""provide me a report of the following topic including heading, abstract, introduction, description,
    flowcharts, and conclusion in the form of LaTeX""", prompt=inp)
    
    
    st.subheader("Rendered LaTeX Output")
    st.latex(r'\begin{equation}' + flow + r'\end{equation}')
    
st.write("Note: Divya GPT can make mistakes. Retry the prompt if issues arise.")
