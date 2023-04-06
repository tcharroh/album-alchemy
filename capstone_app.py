import streamlit as st
import pandas as pd
import openai
import numpy as np
import requests
from PIL import Image
from tqdm import tqdm
from evaluate import load
from datetime import date

st.title('welcome to album alchemy')
st.markdown("here you will find a pitchfork-like album review and album artwork generator.") 
st.markdown("all we need from you is your band name, your band's genre, and a score for the album.")
st.markdown('we will take care of the rest.')
st.markdown('ready to get started?')

st.markdown('#')

st.subheader('review generator')

with st.form(key='model_inputs'):

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
        score = st.slider('score', min_value = 0.0, max_value = 10.0, value = 5.0, step = .1, label_visibility = 'collapsed')

    create = st.form_submit_button('**make album alchemy**')

# if button is clicked (and band and album not blank), run model, produce output 

if create:
    if (band_name.replace(" ","") != '') | (album_name.replace(" ","") != ''):
        with st.spinner('reviewing...'): 

            # get review given above input

            openai.api_type = "open_ai"
            openai.organization_key = st.secrets.openai_keys.org_key
            openai.api_key = st.secrets.openai_keys.chat_key
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
            
            output = generate_review(band_name, album_name, genre, score)

            def generate_artwork_descrip(artist, album, genre, score, review):
                messages = [
                    {"role": "system", "content": "You are an agent to help generate creative descriptions of album artwork."},
                    {"role": "user", "content": f" Write a three sentence description of album artwork for the album '{album}' by {artist}. The band's music genre is {genre}. The description must meet the following criteria:"},
                    {"role": "user", "content": "1. Your response must begin with 'Create an album cover' "},
                    {"role": "user", "content": "2. uses descriptive language to explain images present in the artwork."},
                    {"role": "user", "content": "3. takes into account this recent album review for the band '{review}'."},
                ]
                return chat_completion_request(messages, temperature=1.0, max_tokens=1000, top_p=1.0)
            
            artwork_descrip = generate_artwork_descrip(band_name, album_name, genre, score,output)

            # get image given above input

            def generate_image_from_text():
                openai.organization_key = st.secrets.openai_keys.org_key
                openai.api_key = st.secrets.openai_keys.chat_key
                response = openai.Image.create(
                prompt=artwork_descrip,
                n=1,
                size="256x256"
            )
                
                image_url = response['data'][0]['url']
                return image_url

            image = generate_image_from_text()

            today = date.today().strftime('%B %d, %Y')

            col1,col2 = st.columns(2)
            
            with col1:
                st.markdown('#')
                st.markdown(f'**ARTIST: {band_name}  \n ALBUM: {album_name}  \n GENRE: {genre}  \n SCORE: {score}  \n LABEL: Album Alchemy Records  \n REVIEWED: {today}**')
            
            with col2:
                st.image(image,caption = None)
        #         image_data = requests.get(image).content
        #         with open('AA_artwork.png','rb') as file:
        #             btn = st.download_button(
        #                     label="download artwork",
        #                     data=file,
        #                     file_name="AA_artwork.png",
        #                     mime="image/png"
        # )

            st.markdown('#')
            st.markdown(output)
    else:
        st.error('please enter a valid band and album name')


