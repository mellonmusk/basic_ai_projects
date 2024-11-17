# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st  # streamlit run main.py를 terminal에 입력
# from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI


chat_model = ChatOpenAI()
st.title("인공지능 시인")
content = st.text_input("시의 주제를 제시해주세요.") #주제 정하기


st.write("시의 주제는 ", content)

if st.button("시 작성 요청하기"):
    with st.spinner('시 작성 중...'):
        result = chat_model.predict(content + "에 대한 시를 써줘.")
        st.write(result)
