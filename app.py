
import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "あなたは優秀なアシスタントAIです。"}
        ]

# チャットボットとやりとりする関数
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )  

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""  # 入力欄を消去

with open('chat_log.txt', 'a') as log_file:
    log_file.write(f'User: {user_input}\n')
    log_file.write(f'Bot: {bot_response}\n')

import streamlit as st

# 対話データをテキストボックスに表示
with open('chat_log.txt', 'r') as log_file:
    st.text(log_file.read())
    
    import streamlit as st

# ユーザー名でフィルタリング
username = st.text_input("ユーザー名を入力してください:")

with open('chat_log.txt', 'r') as log_file:
    lines = log_file.readlines()
    for line in lines:
        if f'User: {username}' in line:
            st.text(line)



# ユーザーインターフェイスの構築
st.title("My AI Assistant")
st.write("ChatGPT APIを使ったチャットボットです。")

user_input = st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):  # 直近のメッセージを上に
        speaker = "🙂"
        if message["role"]=="assistant":
            speaker="🤖"

        st.write(speaker + ": " + message["content"])
