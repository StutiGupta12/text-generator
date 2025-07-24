import streamlit as st
from transformers import pipeline, set_seed
st.title("Prompt to Text Generator")

@st.cache_resource
def load_gen():
    return pipeline("text-generation",model="gpt2")


gen=load_gen()

topic=st.text_input("Enter the title")
max_len=st.slider("Max Length",50,500,100)

if topic:
    with st.spinner("Generating Text..."):
        set_seed(42)
        result=gen(topic,max_length=max_len)
        st.success("Done")
        generated=result[0]['generated_text']
        st.write(generated)
    