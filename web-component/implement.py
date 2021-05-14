
import option1
import option2
import leaderboard
import streamlit as st

PAGES = {
    "Price Perdiction": option1,
    "Draw Right Now": option2,
    "Competition Leaderboard": leaderboard
}
st.sidebar.title('Navigation')
selection = st.sidebar.selectbox("Select Options", list(PAGES.keys()))
page = PAGES[selection]
page.exe()


