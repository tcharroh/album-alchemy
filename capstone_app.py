import streamlit as st

st.title('welcome to album alchemy')
st.markdown("here you will find a pitchfork album review and album artwork generator.") 
st.markdown("all we need from you is your band name, your band's genre, and a score for the album.")
st.markdown('we will take care of the rest.')
st.markdown('ready to get started?')

st.markdown('#')

st.subheader('review generator')

col1,col2,col3 = st.columns(3)
with col1:  
    st.markdown('##### band name')
    # help = 'enter a band name, fictional or real, up to 20 characters long'
    band_name = st.text_input( '**band name**', max_chars = 30,label_visibility = 'collapsed',)

with col2:
    st.markdown('##### genre')
    genre = st.selectbox('**genre**',('Rock',
    'Electronic',
    'Rap',
    'Experimental',
    'Pop/R&B',
    'Folk/Country',
    'Metal',
    'Jazz',
    'Global'), label_visibility = 'collapsed')

with col3:
    st.markdown('##### score (example: 5.4)')
    score = st.text_input('score',max_chars = 3, label_visibility = 'collapsed' ,) 

st.markdown('#')

st.button('**create album alchemy**')