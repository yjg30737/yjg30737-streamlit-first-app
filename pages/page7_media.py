import streamlit as st
# from streamlit_webrtc import webrtc_streamer

st.title('Media elements')
st.sidebar.markdown('To good to be true! :sunglasses:')

st.subheader('Image')
st.image('https://static.streamlit.io/examples/cat.jpg', caption='Cute cat', use_column_width=True)

st.subheader('Audio')
st.audio('a.mp3', format='audio/mp3')

st.subheader('Video')
st.video('https://www.youtube.com/watch?v=Cxhk5Fi7G_s')

# TODO
# st.subheader('Stream')