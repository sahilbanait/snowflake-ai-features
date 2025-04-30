import streamlit as st

### PAGE CONFIG ###
st.set_page_config(page_title="Snowflake Cortex AI ", page_icon=':material/plagiarism:', layout="wide")


def get_cortex_response(prompt: str) -> str:
    return f"Echo from Snowflake Cortex: {prompt}"


### Document AI ###
st.header("Welcome to Snowflake Document AI :material/document_scanner:")
main = st.container(height=900, border=True)
with main:
    column1, column2 = st.columns(2)

    with column1:
        file = st.file_uploader(label='## **Select document**', type=None)
        if file:
            file_name = file.name
            if file_name:
                st.write("Selected document: ", file_name)

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        input_msg = st.chat_input("Ask questions about your document")
        with st.container():
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

    with column2:
        if file:
            with st.container(height=800):
                st.write(file.read1() if file is not None else '')
        else:

            st.markdown("# :material/pending_actions:")
