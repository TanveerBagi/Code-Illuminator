import streamlit as st
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=st.secrets["API_KEY"], # Instead of st.secrets["API_KEY"] add your api key as "your api key" and don't forget the double quotation marks
)

def explain_code(text):
    st.markdown(f"**Your Code:** {text}")
    response_text = ""
    output_text = st.empty()

    completion = client.chat.completions.create(
        extra_body={},
        model="deepseek/deepseek-r1:free",
        messages=[
          {"role": "system", "content": f"explain the code:{text}"},
          {"role": "user","content": text}
        ],
        stream = True
    )

    for chunk in completion:
        if chunk.choices[0].delta.content:  
            response_text += chunk.choices[0].delta.content 
            output_text.markdown(f"**Code Illuminator:** {response_text}")

