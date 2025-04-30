import time

import streamlit as st

### PAGE CONFIG ###
st.set_page_config(page_title="Snowflake Cortex AI", layout="centered")


def get_cortex_response(prompt: str) -> str:
    return f"Echo from Snowflake Cortex: {prompt}"


st.header(" Welcome to :material/mode_cool: Cortex AI Chat :material/robot:")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
input_msg = st.chat_input("Ask something")
with st.container(height=750, ):
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := input_msg:
        # Display user message
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        # Get response from Snowflake Cortex
        response = get_cortex_response(prompt)
        st.session_state.chat_history.append(
            {"role": "assistant", "content": response}
        )
        with st.chat_message("assistant"):
            st.markdown(response)
# st.write(st.session_state.chat_history)
new_chat_btn = st.button(label='Clear Chat', icon=':material/history:')

if new_chat_btn:

    with st.spinner("Wait for it...", show_time=True):
        time.sleep(1)
        st.session_state.chat_history.clear()
        if not st.session_state.chat_history:
            st.success("Chat history cleared",icon=':material/done_outline:')
