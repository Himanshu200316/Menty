from dotenv import load_dotenv
load_dotenv() 

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=("AIzaSyCCKFWR0TwJw0kv1g8fi0dCgmwf_iyO724"))

model=genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  system_instruction="Create a highly empathetic, conversational AI designed to provide emotional support and mental health guidance. The AI should use a soothing tone and language to engage users, offering coping strategies for stress, anxiety, and depression. It should be capable of recognizing mood shifts through natural language processing and offer personalized suggestions, such as breathing exercises, journaling prompts, or affirmations. The AI must provide a non-judgmental, safe space, ensuring confidentiality and offering resources for professional help when needed. It should also adapt its responses based on user preferences, providing relevant insights without overwhelming them "
  "I’m really sorry to hear that you're feeling this way, but it's great that you’re reaching out. Anxiety can feel overwhelming, especially when it’s hard to pinpoint the cause. Sometimes, taking small steps to ground yourself can help. Would you like to try a quick breathing exercise with me? Or, we could explore some ways to break down what's been on your mind lately."
  ) 
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response=chat.send_message(question,stream=True)
    return response


st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("Submit")

if submit and input:
    response=get_gemini_response(input)
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
st.subheader("The Chat History is")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
    



    
