import streamlit as st
import collections

class MultiPage: 
    def __init__(self) -> None:
        self.pages = collections.defaultdict()
    
    def add_page(self, title, func) -> None:
        """
        self.pages.append({ 
                "title": title, 
                "function": func
            })
        """
        
        self.pages[title] = func
        
    def run(self):
        # Drodown to select the page to run
        """
        page = st.sidebar.selectbox(
            'App Navigation', 
            self.pages, 
            format_func=lambda page: page['title']
        )
        """
        
        st.sidebar.title('Navigation')
        selection = st.sidebar.radio("Go to", list(self.pages.keys()))
        page = self.pages[selection]
        #page.app()
        
        
        # run the app function 
        #page['function']()
        
        
