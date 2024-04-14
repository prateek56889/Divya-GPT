import streamlit as st
import google.generativeai as model
from io import BytesIO
from matplotlib import pyplot as plt
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
def flow_char(title, over):
    # Create a new figure
    fig, ax = plt.subplots(figsize=(8, 6))

    # Draw nodes
    ax.text(0.5, 0.9, title, ha='center', va='center', fontsize=12, bbox=dict(facecolor='cyan', alpha=0.5))
    for j_idx, j in enumerate(over.split(",")):
        ax.text(0.5, 0.7 - j_idx * 0.1, j[:80], ha='center', va='center', fontsize=12, bbox=dict(facecolor='green', alpha=0.5))

    # Draw edges
    for j_idx, j in enumerate(over.split(",")):
        ax.annotate("", xy=(0.5, 0.8 - j_idx * 0.1), xytext=(0.5, 0.75 - j_idx * 0.1),
                    arrowprops=dict(arrowstyle="->"))

    # Remove axes
    ax.axis('off')

    return fig
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
           flowchart_file = BytesIO()
           flowchar.savefig(flowchart_file, format='png')
           flowchart_file.seek(0)
           st.sidebar.download_button("Download Flowcharts",flowchart_file.getvalue(),file_name="Flowchat.jpg",mime="image/png")
     
st.write("NOte:-Divya Gpt can make mistakes, retry the prompt if issues engagges")
