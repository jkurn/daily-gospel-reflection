import streamlit as st
from app.pages import home, reflection

def main():
    st.set_page_config(page_title="Daily Gospel Reflection", page_icon="🙏")
    
    pages = {
        "Home": home.show,
        "Daily Reflection": reflection.show,
    }
    
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    
    page = pages[selection]
    page()

if __name__ == "__main__":
    main()
