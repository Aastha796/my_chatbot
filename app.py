import openai
import streamlit as st

# Initialize OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Set the app title
st.title("CJ's Chat aPP")

# Initialize session state to maintain chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Define a function to get a response from OpenAI's GPT-3.5 Turbo
def get_response(conversation_history, user_input):
    messages = [{"role": "system", "content": "You are a helpful assistant."}] \
               + conversation_history + [{"role": "user", "content": user_input}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response["choices"][0]["message"]["content"]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input box
if user_input := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    response = get_response(st.session_state.messages[:-1], user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
