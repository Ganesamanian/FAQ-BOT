import streamlit as st
import langchain_helper as lh



# Streamlit UI
st.title("FAQ BOT")
st.header("Ask your Question below")
question = st.text_input("Enter the question here")



if question:
    answer = lh.chain.invoke(question)
    lh.main_placeholder.text("Fetching the Answer")
    st.text(answer['result'])
    lh.main_placeholder.text("Answered, any other questions? Please ask below")
