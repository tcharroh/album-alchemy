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

create = st.button('**make album alchemy**')

# df = pd.read_csv('/Users/kevinborah/Desktop/MADS/pitchfork_reviews.csv')



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

sample_output = '''

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Dui vivamus arcu felis bibendum ut tristique et egestas quis. Nunc scelerisque viverra mauris in aliquam sem fringilla ut. Dignissim enim sit amet venenatis urna. Mauris augue neque gravida in. Facilisi nullam vehicula ipsum a arcu cursus vitae congue mauris. Ut tristique et egestas quis. Libero id faucibus nisl tincidunt eget nullam non nisi. Potenti nullam ac tortor vitae. Leo duis ut diam quam nulla porttitor massa id. Diam sit amet nisl suscipit adipiscing. Feugiat vivamus at augue eget. Neque aliquam vestibulum morbi blandit cursus risus. Nec feugiat nisl pretium fusce. Leo duis ut diam quam nulla porttitor massa.

Tincidunt dui ut ornare lectus sit. Felis imperdiet proin fermentum leo. Velit sed ullamcorper morbi tincidunt ornare massa eget egestas purus. Odio aenean sed adipiscing diam donec adipiscing. Velit ut tortor pretium viverra suspendisse potenti nullam ac tortor. Odio eu feugiat pretium nibh ipsum consequat nisl. Turpis egestas maecenas pharetra convallis. Facilisis volutpat est velit egestas dui id ornare. Nisi est sit amet facilisis magna etiam tempor orci. Lacus sed viverra tellus in hac habitasse platea dictumst. Ac tortor vitae purus faucibus. At erat pellentesque adipiscing commodo elit at imperdiet dui accumsan. Fringilla urna porttitor rhoncus dolor purus non. Aliquam etiam erat velit scelerisque in dictum non consectetur. Adipiscing enim eu turpis egestas pretium aenean pharetra. Adipiscing at in tellus integer feugiat scelerisque varius morbi enim.

Consectetur lorem donec massa sapien. Auctor urna nunc id cursus metus aliquam eleifend. Vel fringilla est ullamcorper eget. Nulla facilisi morbi tempus iaculis. Arcu non sodales neque sodales ut etiam sit. Fermentum leo vel orci porta non pulvinar. Placerat in egestas erat imperdiet sed. Id venenatis a condimentum vitae sapien pellentesque. Viverra mauris in aliquam sem fringilla ut. Posuere urna nec tincidunt praesent semper feugiat nibh. Lorem mollis aliquam ut porttitor leo. Faucibus purus in massa tempor nec feugiat nisl. Tellus in metus vulputate eu scelerisque felis imperdiet. Neque volutpat ac tincidunt vitae semper quis lectus. Proin sagittis nisl rhoncus mattis.

Imperdiet sed euismod nisi porta lorem mollis aliquam ut porttitor. Tortor at auctor urna nunc id. Platea dictumst vestibulum rhoncus est. Laoreet id donec ultrices tincidunt arcu non. In hac habitasse platea dictumst quisque. Et molestie ac feugiat sed lectus vestibulum. Rutrum tellus pellentesque eu tincidunt tortor aliquam nulla. Tellus cras adipiscing enim eu turpis egestas pretium aenean. Eu sem integer vitae justo eget magna fermentum iaculis eu. A arcu cursus vitae congue. Tempor id eu nisl nunc mi. Amet consectetur adipiscing elit pellentesque habitant morbi tristique. Cras adipiscing enim eu turpis egestas pretium aenean. Ultricies tristique nulla aliquet enim.

Mauris rhoncus aenean vel elit scelerisque mauris pellentesque. Senectus et netus et malesuada. Sit amet risus nullam eget felis eget nunc. Ut sem nulla pharetra diam sit. In nulla posuere sollicitudin aliquam ultrices sagittis. Malesuada proin libero nunc consequat. Cursus turpis massa tincidunt dui ut ornare lectus. Feugiat nisl pretium fusce id velit ut tortor pretium viverra. At tempor commodo ullamcorper a lacus vestibulum sed. Elementum tempus egestas sed sed risus pretium quam vulputate dignissim. Volutpat est velit egestas dui id ornare arcu odio.

'''

#if 'create' button above is clicked, produce output

if create:
    st.markdown(sample_output)

# perplexity = load('perplexity', module_type = 'measurement')

# results = perplexity.compute(data = input_texts, model_id = 'gpt2')

# print(round(results['mean_perplexity'],2))
