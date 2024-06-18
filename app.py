import json
import requests
import streamlit as st

def main():
    st.set_page_config(page_title="Chat PDF")
    
    st.header("CyBot🔐")

    user_question = st.text_input("Ask your question:")

    if st.button("Enter"):
        with st.spinner("Processing..."):
            try:
                url = "https://ldjao8swv3.execute-api.ap-south-1.amazonaws.com/dev/blog-generation"
                payload = {
                    "blog_topic": user_question
                }
                headers = {
                    "Content-Type": "application/json"
                }
                response = requests.post(url, data=json.dumps(payload), headers=headers)
                
                # Attempt to parse JSON response
                try:
                    response_data = response.json()
                    st.write(response_data)
                except json.JSONDecodeError:
                    st.error("Failed to decode JSON response. Please check the API response format.")
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
