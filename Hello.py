import streamlit as st

NAME = 'yjg30737'

st.set_page_config(
    page_title=f"{NAME}'s first streamlit app",
    page_icon="👋",
)

st.write(f"# Welcome to {NAME}'s Streamlit! 👋")
st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.

    **👈 Select a demo from the dropdown on the left** to see some examples
    of what Streamlit can do!

    ### Want to learn more?

    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
      forums](https://discuss.streamlit.io)

    ### See more complex demos

    - Use a neural net to [analyze the Udacity Self-driving Car Image
      Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)
#
# page_names_to_funcs = {
#     "—": intro,
#     "Plotting Demo": plotting_demo,
#     "Mapping Demo": mapping_demo,
#     "DataFrame Demo": data_frame_demo
# }
#
# demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
# page_names_to_funcs[demo_name]()