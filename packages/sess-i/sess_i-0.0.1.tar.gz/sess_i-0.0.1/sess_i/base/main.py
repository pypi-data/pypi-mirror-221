"""
Session-State interface module

Create class containing the whole sess_i interface. The class contains two subclasses:
    * Object space: contains the logic for handling tool calculation layer and communication with the widget spaces
    * Widget space(s): contains the logic for handling data persistency throughout page switching in the GUI
The main class when initialized will automatically generate an object space. Widget spaces will be generated with a
specific command. This is because while there is only one object space, there can be multiple widget spaces (one for
each page).

The user will start by initializing the sess_i object, passing in as argument the streamlit session state for the
current user. Internally, a widget space is initialized with the current page. This creates an entry in the Global
Widget Space that will hold the different widget keys and associate a page id to them.

On page load:
    1) If first pass: Initialize session, create page widget space and Global Space in session_state. Put the widget
    space object into the Global Space. Initialize widget defaults from user kwargs.
    Create object space, add to session state and create objects container inside the Space.
    On leave: add widget values inside widgets container. Update Object in session state from object space.
    2) Else: Initialize session. Initialize widget values from Widget Space stored values.
"""

import streamlit as st


# Object Space
class ObjectSpace:
    """
    The object space contains the objects and their data.
    A method is needed to register objects with specific keys
    """

    def __init__(self, session_state):
        self.session_state = session_state
        if "Object_Space" not in self.session_state.keys():
            self.session_state["Object_Space"] = {}
        self.objects = self.session_state["Object_Space"]

    def __repr__(self):
        return f"Stored objects:\n{self.objects}"

    def __getitem__(self, item):
        return self.objects.get(item)

    def __setitem__(self, key, value):
        self.session_state["Object_Space"].update({key: value})
        self.objects[key] = value


# Widget Space
class WidgetSpace:
    """
    Every widget space must contain two base parameters:
        * The id of the page it communicates with
        * A container with the widgets and their state metadata (key & value)
    """

    def __init__(self, session_state, page):

        self.page = page
        self.session_state = session_state
        self.widgets = {}

        if "Global_Widget_Space" not in session_state.keys():
            self.session_state["Global_Widget_Space"] = {page: self}

        for key, value in session_state.items():
            if str(self.page) in key:
                self.widgets.update({key: value})

    def __repr__(self):
        return f"WidgetSpace.widgets({self.widgets})"

    def __getitem__(self, item):
        return self.widgets.get(item)

    @classmethod
    def initialize_session(cls, session_state, page=None):
        """
        Initialize widget space and add to Global Space
        :param page: page number
        :param session_state: streamlit session state
        :return:
        """
        if page is None:
            page = __file__.split("\\")[-1][:-3]
        if "Global_Widget_Space" not in session_state.keys():
            space = WidgetSpace(session_state, page)
            session_state["Global_Widget_Space"] = {page: space}
            return st.session_state["Global_Widget_Space"][page]
        else:
            if page not in session_state["Global_Widget_Space"].keys():
                session_state["Global_Widget_Space"].update({page: WidgetSpace(session_state, page)})
            return st.session_state["Global_Widget_Space"][page]

    def set_widget_defaults(self, **kwargs):

        if not self.widgets:
            self.widgets = {key: value for key, value in kwargs.items()}

    def register_widgets(self, mapping=None, **kwargs):
        if not self.session_state["Global_Widget_Space"][self.page]:
            raise KeyError(
                f"Widget space for page '{self.page}' doesn't exist."
            )
        if mapping:
            self.widgets.update(mapping)
        if kwargs:
            self.widgets.update(**kwargs)


class SessI:

    def __init__(self, session_state, page=None):
        self.session_state = session_state
        self.page = page if page is not None else __file__.split("\\")[-1][:-3]
        self.object_space = ObjectSpace(self.session_state)
        self.widget_space = WidgetSpace.initialize_session(self.session_state, self.page)

    def __repr__(self):
        return f"Page = {self.page}\n" \
               f"Registered Objects = {self.object_space.objects}\n" \
               f"Widgets = {self.widget_space.widgets}"

    def set_widget_defaults(self, **kwargs):
        self.widget_space.set_widget_defaults(**kwargs)

    def register_widgets(self, mapping=None, **kwargs):
        self.widget_space.register_widgets(mapping, **kwargs)

    def register_object(self, obj, key):
        self.object_space[key] = obj

    def get_object(self, key):
        return self.object_space[key]


if __name__ == "__main__":
    pass
