import streamlit as st
import google.generativeai as genai

st.markdown("# Simple Chatbot")
st.sidebar.markdown("# Hi, Pranjul")

GOOGLE_API_KEY = "AIzaSyDqlJmz8LuoVTqXI_QZUrxIhTAlubDCmZs"  # Replace with your Google API Key
genai.configure(api_key=GOOGLE_API_KEY)

gemini_Model = genai.GenerativeModel("gemini-pro")
chat = gemini_Model.start_chat(history=[])

st.header("Welcome")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input_text = st.text_input("Input: ", key="input")
submitButton = st.button("Get Answer")

# Function to get chatbot response
def get_gemini_response(input_text):
    response = chat.send_message(input_text)  # Sends the message to the chatbot
    return response  # Returns the chatbot's response

if submitButton and input_text:
    output = get_gemini_response(input_text)
    st.session_state['chat_history'].append(("You", input_text))
    
    st.subheader("The Response is ")
    for outputChunk in output:
        st.write(outputChunk.text)
        st.session_state['chat_history'].append(("Bot", outputChunk.text))

st.subheader("The Chat History is ")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")


