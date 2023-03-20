import streamlit as st
import pandas as pd
from evaluate import load

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

st.button('**make album alchemy**')

df = pd.read_csv('/Users/kevinborah/Desktop/MADS/pitchfork_reviews.csv')

st.dataframe(df)

# df = df[df.review.str.len() > 20]
# df = df[df.review.str.len() < 10000] df = df[~df.review.str.contains('\n')]

# single_column = df.score.map(str) + "\n" + df.genre + "\n" + df.review  
# single_column.to_csv('score_genre_review.csv', header=False, index=False)

#######################################
# Run model given the above selections#
#######################################

#######################################
######### Evaluate Model ##############
#######################################
# from https://huggingface.co/spaces/evaluate-measurement/perplexity
# Use output generated from fine tuned model and measure perplexity compared to model

perplexity = load('perplexity', module_type = 'measurement')

results = perplexity.compute(data = input_texts, model_id = 'gpt2')

print(round(results['mean_perplexity'],2))
