import streamlit as st
from domain.services.gospel_service import GospelService
from domain.services.news_service import NewsService

def show():
    st.title("Daily Reflection")
    
    gospel = GospelService.get_daily_gospel()
    news = NewsService.get_top_news()
    
    st.subheader("Today's Gospel")
    st.write(f"{gospel.reference}: {gospel.text}")
    
    st.subheader("Top News")
    for item in news:
        st.write(f"- {item.title}")
    
    if st.button("Generate Reflection"):
        # TODO: Implement reflection generation
        pass
