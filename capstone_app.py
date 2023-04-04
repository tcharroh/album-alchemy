import streamlit as st
import pandas as pd
import openai
import numpy as np
from tqdm import tqdm
from evaluate import load
from datetime import date

st.title('welcome to album alchemy')
st.markdown("here you will find a pitchfork album review and album artwork generator.") 
st.markdown("all we need from you is your band name, your band's genre, and a score for the album.")
st.markdown('we will take care of the rest.')
st.markdown('ready to get started?')

st.markdown('#')

st.subheader('review generator')

col1,col2,col3,col4 = st.columns(4)
with col1:  
    st.markdown('##### band name')
    # help = 'enter a band name, fictional or real, up to 30 characters long'
    band_name = st.text_input( '**band name**', max_chars = 30,label_visibility = 'collapsed',)

with col2:
    st.markdown('##### album name')
    album_name = st.text_input('**album name**', max_chars = 30, label_visibility = 'collapsed')

with col3:
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

with col4:
    st.markdown('##### score')
    # score = st.text_input('score',max_chars = 3, label_visibility = 'collapsed' ,) 
    score = st.slider('score', min_value = 0.0, max_value = 10.0, value = 5.0, step = .1, label_visibility = 'collapsed')

st.markdown('#')

create = st.button('**make album alchemy**')

# df = pd.read_csv('/Users/kevinborah/Desktop/MADS/pitchfork_reviews.csv')



# df = df[df.review.str.len() > 20]
# df = df[df.review.str.len() < 10000] df = df[~df.review.str.contains('\n')]

# single_column = df.score.map(str) + "\n" + df.genre + "\n" + df.review  
# single_column.to_csv('score_genre_review.csv', header=False, index=False)

#######################################
# Run model given the above selections#
openai.api_type = "open_ai"
openai.api_key = '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'
openai.api_base = "https://api.openai.com/v1"
openai.api_version = None

def chat_completion_request(messages, temperature=0, max_tokens=256, top_p=1.0):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo", 
      messages=messages)
    
    return response['choices'][0]['message']['content']

def generate_review(artist, album, genre, score):
    messages = [
        {"role": "system", "content": "You are an agent to help generate human-like reviews for music albums."},
        {"role": "user", "content": f"Write a a long and insightful music review for the music album '{album}' by {artist}. The music genre is {genre} with a rating of {score} out of 10. The review must meet the following criteria:"},
        {"role": "user", "content": "1. written in a conversational tone, with sophisticated sentence structure and language."},
        {"role": "user", "content": "2. includes details about the band's history and the album's creation story."},
        {"role": "user", "content": "3. includes personal experience and opinions."},
        {"role": "user", "content": "Review:"},
    ]
    return chat_completion_request(messages, temperature=1.0, max_tokens=2048, top_p=1.0)


#######################################

#######################################
######### Evaluate Model ##############
#######################################
# from https://huggingface.co/spaces/evaluate-measurement/perplexity
# Use output generated from fine tuned model and measure perplexity compared to model

sample_output = generate_review(band_name, album_name, genre, score)

#if 'create' button above is clicked, produce output
today = date.today().strftime('%B %d, %Y')

if create:
    if band_name.replace(" ","") != '':    
        st.markdown(f'**ARTIST: {band_name}  \n GENRE: {genre}  \n SCORE: {score}  \n LABEL: Album Alchemy Records  \n REVIEWED: {today}**')
        st.markdown('#')
        st.markdown(sample_output)
    else:
        st.error('please enter a valid band name')

# perplexity = load('perplexity', module_type = 'measurement')

# results = perplexity.compute(data = input_texts, model_id = 'gpt2')

# print(round(results['mean_perplexity'],2))

