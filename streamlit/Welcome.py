import streamlit as st


def get_cortex_response(prompt: str) -> str:
    return f"Echo from Snowflake Cortex: {prompt}"


### PAGE CONFIG ###
st.set_page_config(page_title="Snowflake Cortex AI", layout="wide")
# options = ['Cortex AI', 'Document AI']
# sidebar = st.sidebar.selectbox(
#     "Snowflake AI and ML options",
#     set(options),
#     index=None,
#     placeholder="Select the AI Service..."
# )
#
# ### COMPONENTS ###
# if sidebar is None:
#     st.title('Hello')
# ### Cortex AI ###
# if sidebar == 'Cortex AI':
#     st.header(" Welcome to Snowlfake Cortex AI")
#     if "chat_history" not in st.session_state:
#         st.session_state.chat_history = []
#     input_msg = st.chat_input("Ask something")
#     with st.container(height=800):
#         for msg in st.session_state.chat_history:
#             with st.chat_message(msg["role"]):
#                 st.markdown(msg["content"])
#
#         if prompt := input_msg:
#             # Display user message
#             st.session_state.chat_history.append({"role": "user", "content": prompt})
#             with st.chat_message("user"):
#                 st.markdown(prompt)
#
#             # Get response from Snowflake Cortex
#             response = get_cortex_response(prompt)
#             st.session_state.chat_history.append({"role": "assistant", "content": response})
#             with st.chat_message("assistant"):
#                 st.markdown(response)
#     # st.write(st.session_state.chat_history)
#     new_chat_btn = st.button(label='Clear Chat', icon='💬')
#
#     if new_chat_btn:
#         st.session_state.chat_history.clear()
#
# ### Document AI ###
# if sidebar == 'Document AI':
#     st.header("Welcome to Snowflake Document AI")
#     main = st.container()
#     with main:
#         column1, column2 = st.columns(2)
#
#         with column1:
#             file = st.file_uploader(label='## **Select document**', type=None)
#             if file:
#                 file_name = file.name
#                 if file_name:
#                     st.write("Selected document: ", file_name)
#
#         with column2:
#             if file:
#                 with st.container(height=800):
#                     st.write(file.read1() if file is not None else '')
#
# st.sidebar.divider()
