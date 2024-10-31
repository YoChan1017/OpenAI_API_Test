#from dotenv import load_dotenv
#load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.title('여행 관광지 추천')

content = st.text_input('가고싶은 여행지를 말하세요.')

if st.button('관광지 추천하기'):
    with st.spinner('관광지 검색 중...'):
        result = chat_model.predict(content + "에 대한 관광지를 3군데 추천해줘.")
        st.write(result)
