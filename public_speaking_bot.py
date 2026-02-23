import streamlit as st

st.title("🎤 Public Speaking Bot")

topic = st.text_input("Enter your speech topic")

if st.button("Generate Speech"):
    speech = f"""
Good morning everyone,

Today I am going to speak about {topic}.
This topic is important in our daily life and future.

First, it helps us gain knowledge.
Second, it improves our confidence.
Finally, it prepares us for success.

In conclusion, {topic} plays a vital role in our growth.
Thank you.
"""
    st.success("Speech Generated!")
    st.write(speech)
