import streamlit as st
from sess_i.base.main import WidgetSpace


widget_space = WidgetSpace.initialize_session(1, st.session_state)
st.write(st.session_state["Global_Widget_Space"]["home"].widgets)
st.write(widget_space.widgets)
widget_space.check_session()
