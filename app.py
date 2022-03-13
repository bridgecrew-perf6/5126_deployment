import streamlit as st
from multipage import MultiPage

st.set_page_config(
     page_title="HDB resale price analysis",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )

app = MultiPage()

def introduction():
    st.title("**HDB Resale price analysis**")
    st.subheader(
        """
        Group - 20
        """
    )


def test():
    st.write("Page loaded")

app.add_page("page1",test)
app.add_page("page2",test)
app.add_page("page3",test)
app.add_page("page4",test)
app.add_page("page5",test)

app.run()