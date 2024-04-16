from openai import OpenAI
import streamlit as st

f = open("keys/.openai_api_key.txt")
key = f.read()
client = OpenAI(api_key=key)


st.title("AI Code Viewer")

def correct_code(code):
    try:
        # Prepare the code for OpenAI GPT-3
        prompt = f"Here is the provided code:\n\n{code}\n\nPlease provide corrections or improvements:"
        
        # Call OpenAI's completion endpoint
        response = client.chat.completions.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None
        )
        
        # Extract the corrected code from OpenAI's response
        corrected_code = response['choices'][0]['text'].strip()
        return corrected_code
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Streamlit app
st.header("AI Code Viewer")

user_code = st.text_area("Enter your code here:", height=400)

if st.button("Check and Correct"):
    if user_code.strip():
        corrected_output = correct_code(user_code)
        st.write("Corrected Code:")
        st.code(corrected_output, language="python")
    else:
        st.warning("Please enter some code to check.")
