import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

open_api_key = st.secrets["openai"]["api_key"]
import os
os.environ['open_api_key']=open_api_key

st.title('I am Your Langchain AI....')

st.chat_message("assistant").write("Hi, Welcome to our Bot.. How may I help you today...?")

if "messages" not in st.session_state:
    st.session_state["messages"]= []

for msg in st.session_state["messages"]:
    if isinstance(msg, dict) and "role" in msg and "content" in msg:
        st.chat_message(msg["role"]).write(msg["content"])

#Creating LLM

chatgpt = ChatOpenAI(model_name ='gpt-3.5-turbo', api_key=open_api_key)

query = st.chat_input("Enter your question:")

prompt_template= ChatPromptTemplate.from_template("Answer the question in an easy, understandable way: {query}")
llmchain_o=prompt_template | chatgpt

if query:
    st.session_state["messages"].append({"role":"user", "content": query})
    response = llmchain_o.invoke({"query":query})
    st.session_state["messages"].append({"role": "assistant", "content": response.content})
    #print(response.content)
    st.write(response.content)


