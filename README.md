import openai
import streamlit as st

# Initialize OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Set the app title
st.title("Aastha's Chat aPP")

# Initialize session state to maintain chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Define a function to get a response from OpenAI's GPT-3.5 Turbo
def get_response(conversation_history, user_input):
    """
    Sends the conversation history and new user input to the OpenAI GPT-3.5 Turbo model
    and returns the assistant's response.
    """
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ] + conversation_history + [{"role": "user", "content": user_input}]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    assistant_message = response["choices"][0]["message"]["content"]
    return assistant_message

# Display chat history in a conversational format
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input box for entering messages
if user_input := st.chat_input("Type your message here..."):
    # Append user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get assistant's response
    response = get_response(st.session_state.messages[:-1], user_input)
    
    # Append assistant message to session state
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
