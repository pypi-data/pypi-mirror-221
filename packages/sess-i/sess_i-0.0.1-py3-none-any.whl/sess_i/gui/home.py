from dataclasses import dataclass

from sess_i.base.main import SessI
import streamlit as st


@dataclass
class Something:
    foo: str
    bar: dict


session = SessI(st.session_state, page="main")


st.write(session.widget_space["my_slider_main"])


session.widget_space.set_widget_defaults(
    my_slider_main=5,
    text_input_main="Good morning"
)

main_obj_test = st.slider(
    key="my_slider_main",
    label="test",
    value=session.widget_space["my_slider_main"]
)

with st.form("The form"):
    main_text_test = st.text_input(
        key='text_input_main',
        label="test",
        value=session.widget_space["text_input_main"]
    )
    submitted = st.form_submit_button()

if submitted:
    test = Something(main_text_test, {"echo": 2})

    session.register_object(test, "tester")

session.register_widgets({
    "my_slider_main": main_obj_test,
    "text_input_main": main_text_test
})

st.write(session)
st.write(st.session_state["Global_Widget_Space"])
