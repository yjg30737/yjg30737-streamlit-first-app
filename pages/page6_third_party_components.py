import streamlit as st

from streamlit_extras.stoggle import stoggle

st.title('Input widgets - Third party components')
st.sidebar.markdown('Yes, it is. input widgets, i mean Third party components! :sunglasses:')
stoggle('Toggle me', 'Addicted to Streamlit')

from streamlit_chat import message

message('My message')
message('Hello, bot!', is_user=True)

# Anything below are not necessary to me currently

from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu('Main Menu', ['Home', 'Settings'],
                           icons=['house', 'gear'], menu_icon='cast',
                           default_index=1)
    selected

from streamlit_elements import elements, mui

with elements('new_element'):
    mui.Typography('Hello, Streamlit!')

with elements('multiple_children'):
    mui.Button(
        mui.icon.EmojiPeople,
        mui.icon.DoubleArrow,
        'Button with multiple children'
    )

# import time
# from stqdm import stqdm
#
# # https://github.com/Wirg/stqdm
# # Even though streamlit supports progressbar, they say this is the simplest way to use progressbar
# for _ in stqdm(range(5)):
#     time.sleep(0.5)
# Related bug:
# It loads again for some reasons

from streamlit_timeline import timeline

with open('example.json', 'r') as f:
    timeline(f.read(), height=800)

from camera_input_live import camera_input_live

image = camera_input_live()

if image:
    st.image(image)

from streamlit_ace import st_ace

content = st_ace()

content