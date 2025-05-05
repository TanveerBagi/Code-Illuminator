import streamlit as st
from openai import OpenAI

from explainer import explain_code
from analyzer import analyze_code
from executor import execute_code

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>Code Illuminator</h1>", unsafe_allow_html=True)
st.subheader('Analyze, Debug, and Understand Python Code Instantly with AI.')

text = st.text_area('Paste your code here')

col1, col2, col3 = st.columns([2,2,0.5])

analyze_clicked = col1.button("Analyze")
execute_clicked = col2.button("Execute")
explain_clicked = col3.button("Explain")

if analyze_clicked:
    analyzed_code = analyze_code(text)
    st.write(analyzed_code)
if execute_clicked:
    output = execute_code(text)
    st.write("### Output:")
    st.code(output, language='text')

if explain_clicked:
    explain_code(text)
