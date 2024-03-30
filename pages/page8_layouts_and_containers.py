import streamlit as st

# Columns
# Insert containers laid out as side-by-side columns.
col1, col2 = st.columns(2)
col1.write('This is column 1')
col2.write('This is column 2')

# Container
# Insert a multi-element container.
c = st.container()
st.write('This will show last')
c.write('This will show first')
c.write('This will show second')

# Empty
# Insert a single-element container.
c = st.empty()
st.write('This will show last')
c.write('This will be replaced by first')
c.write('This will show first')

# Expander
# Insert a multi-element container that can be expanded/collapsed.
with st.expander('Open to see more'):
    st.write('This is more content')

# Popover
# Insert a multi-element popover container that can be opened/closed.
with st.popover('Settings'):
    st.checkbox('Show completed')

# Sidebar
# Dislay items in a sidebar.
st.sidebar.write('This lives in the sidebar.')
st.sidebar.button('Click me!')

# Tabs
# Insert containers separated into tabs.
tab1, tab2 = st.tabs(['Tab 1', 'Tab 2'])
tab1.write('this is tab 1')
tab2.write('this is tab 2')