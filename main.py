import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content

st.title("Ai webscrape")
url = st.text_input("Enter a url")

if st.button("Scrape"):
    st.write("works")
    result = scrape_website(url)
    print(result)

    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content
    
    with st.expander("View DOM Content"):
        st.text_area("DOM content", cleaned_content, height=300)

    if "dom_content" in st.session_state:
        parse_description = st.text_area("what are you looking to parse")

        if st.button("Parse Content"):
            if parse_description:
                st.write("Parsing content")

                dom_chunks = split_dom_content(st.session_state.dom_content)
                