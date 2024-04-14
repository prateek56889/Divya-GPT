import streamlit as st
import google.generativeai as model
from io import BytesIO
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
def flow_char(title,over):
    graph = Digraph()
    # Nodes ko add karein
    graph.node(name=title,style="filled",color="cyan")
    for j in over.split(","):
        graph.node(name=j[:80],style="filled",color="green")
    for j in over.split(","):
        graph.edge(title,j[:80])
    # Graph ko visualize karein aur save karein
    return graph
def gemini_res(input,prompt):
    """
    this has to be get in return through gemini
    """
    gemini=model.GenerativeModel("gemini-pro")
    res=gemini.generate_content([input,prompt])
    return res.text
st.set_page_config(page_title="Divya GPT",page_icon="div.png")
st.image("divya.png")
inp=st.text_area(label="Enter the Topic to generate")
response=gemini_res(input=prompts(),prompt=inp)
gen_per=st.button(label="Generate")
if gen_per==True:
     st.write(response)
     st.sidebar.image("favicon.svg")
     st.sidebar.title("Wanna download your important Topics ?")
     st.sidebar.subheader("DivyaGPT offers Download the chat option")
     st.sidebar.download_button("Download Chats",response,file_name="summarise.txt")
     st.sidebar.title("Get's hard to understand Text?")
     st.sidebar.subheader("Dont'worry Divya gpt too provides Ascii based flowcharts , Wanna check?")
     flow=gemini_res(input="""According to the input make sure to mention some key points around 5 key points,
                     each point should be seperated by comma ',' dont mention numbers only a paragraph seperated by comma""",prompt=inp)
     with open("flow.jpg","wb") as flo:
           st.write(flow)
           flowchar=flow_char(title=inp,over=flow)
           flowchart_bytes = BytesIO()
           flowchart_bytes.write(flowchar.pipe(format='png'))
           flowchart_bytes.seek(0)
           st.sidebar.download_button("Download Flowcharts",flowchart_bytes.getvalue(),file_name="Flowchat.jpg",mime="image/png")
     
st.write("NOte:-Divya Gpt can make mistakes, retry the prompt is issue engagges")
