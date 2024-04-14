import streamlit as st
import google.generativeai as model
model.configure(api_key=st.secrets["GEN_API"])
def prompts():
     return """
     Hi buddy i am giving you some names you have to filter them out and generate accordingly
     1.title of the given prompt(use your intellect for it)
     2. overview of that topic
     3. summary of that topic
     4. important keywords of that topic
     5. glossary or hard words 
     6. questions and answers upto 5 
     """
def gemini_res(input,prompt):
    """
    this has to be get in return through gemini
    """
    gemini=model.GenerativeModel("gemini-pro")
    res=gemini.generate_content([input,prompt])
    return res.text
st.set_page_config(page_title="Divya GPT",page_icon="div.png")
st.image("divya.png")
inp=st.text_area(label="Enter the Prompt")
response=gemini_res(input=prompts(),prompt=inp)
gen_per=st.button(label="Generate")
if gen_per==True:
     st.write(response)
     st.sidebar.image("favicon.svg")
     st.sidebar.title("Wanna download your important Topics ?")
     st.sidebar.subheader("DivyaGPT offers Download the chat option")
     with open("summary.txt","w") as data:
               data.write(response)
               st.sidebar.download_button("Download Summary",response,file_name="summarise.txt")
     st.sidebar.title("Get's hard to understand Text?")
     st.sidebar.subheader("Dont'worry Divya gpt too provides Ascii based flowcharts , Wanna check?")
     flow=gemini_res(input="""can you create an ascii based flowchart for the following data make
                     sure that the flow chart must be simple to understand use blocks instead""",prompt=response)
     with open("flow.txt","w") as flo:
           flo.write(flow)
           st.write(flow)
           st.sidebar.download_button("Download Flowcharts",flow,file_name="Flowchat.txt")
     

