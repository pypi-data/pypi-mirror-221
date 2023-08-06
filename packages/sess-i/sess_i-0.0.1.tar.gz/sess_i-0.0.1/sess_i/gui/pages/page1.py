import streamlit as st
from sess_i.base.main import SessI

session = SessI(st.session_state, "page1")
st.write(session.page)
session.set_widget_defaults(
    numbers_test_page1=2
)

numbers = st.number_input(
    key="numbers_test_page1",
    value=session.widget_space["numbers_test_page1"],
    label="test"
)

st.write(session)
session.register_widgets(
    {
        "numbers_test_page1": numbers
    }
)

tester = session.get_object("tester")

text_example = st.text_input(
    key="text_example_page1",
    value=tester.foo,
    label="Get foo from home page"
)
