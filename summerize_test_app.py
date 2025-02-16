# streamlit 패키지 추가
import streamlit as st
# openai 패키지 추가
import openai
##### 기능 구현 함수 #####
def askGpt(prompt,apikey):
    client = openai.OpenAI(api_key = apikey)
    response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages = [{'role' : 'user','content' : prompt}] )
    gptResponse = response.choices[0].message.content
    return gptResponse
##### 메인 함수 #####
def main():
    st.set_page_config(page_title='요약 프로그램')
    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""
    with st.sidebar:
        open_apikey = st.text_input(label="OPENAI AIP 키를 입력해주세요",placeholder='Enter your openai API key',value='',type='password')
        if open_apikey:
            st.session_state["OPENAI_API"] = open_apikey
        st.markdown('---')
    st.header('📃요약 프로그램')
    st.markdown('---')

    text = st.text_area("요약 할 글을 입력하세요")
    if st.button('요약'):
        prompt = f'''
        **Instructions** :
    - You are an expert assistant that summarizes text into **Korean language**.
    - Your task is to summarize the **text** sentences in **Korean language**.
    - Your summaries should include the following :
        - Omit duplicate content, but increase the summary weight of duplicate content.
        - Summarize by emphasizing concepts and arguments rather than case evidence.
        - Summarize in 3 lines.
        - Use the format of a bullet point.
    -text : {text}
    '''
        st.info(askGpt(prompt,st.session_state["OPENAI_API"]))

if __name__=="__main__":
    main()
