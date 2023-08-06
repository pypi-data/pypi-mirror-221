from sess_i.base.main import WidgetSpace
import streamlit as st

class TestObject:

    def __init__(self, name):

        self.name = name


widget_space = WidgetSpace.initialize_session("home", st.session_state)
obj_test = st.slider(
    key="Page_home_slider",
    label="test",
    value=widget_space.widgets["Page_home_slider"]
)

text_test = st.text_input(
    key='Page_home_text',
    label="test",
    value=widget_space.widgets["Page_home_text"]
)

widget_space.check_session()
st.write(widget_space.widgets)
