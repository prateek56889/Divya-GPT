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
    flow = gemini_res(input="""provide me latex code of the following topic which follows this format heading, abstract, introduction, description,
    flowcharts, and conclusion in the form of LaTeX Note:- make sure to create flowchats in latex code and emmbed them into this report""", prompt=inp)
    
    
    st.subheader("Rendered LaTeX Output")
    st.write(flow)
    st.sidebar.download_button("PDF report",flow, file_name="divya_gpt.tex")
    
st.write("Note: Divya GPT can make mistakes. Retry the prompt if issues arise.")
