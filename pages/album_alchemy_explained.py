import streamlit as st

st.set_page_config(page_title="how_we_did_it", page_icon=None)

st.markdown(

"""


# Project statement
""")

st.write("[![Star](https://img.shields.io/github/stars/0-kbo/album-alchemy?style=social)](https://github.com/0-kbo/album-alchemy/tree/main)")

st.markdown("""
>“Strictly considered, writing about music is as illogical as singing about economics. All the other arts can be talked about in the terms of ordinary life and experience. A poem, a statue, a painting or a play is a representation of somebody or something, and can be measurably described (the purely aesthetic values aside) by describing what it represents.” (K 63)

Though people have been writing about music since Plato, the practice of musical criticism, as we have come to know it emerged in the late eighteenth and early nineteenth centuries. (Kivy 247) With the arrival of the internet roughly two-hundred years later, musical criticisms moved online to personal websites and blogs. By the early 2000s, one such musical criticism website, Pitchfork, had amassed a large following and increased cultural currency.

Though musical criticisms can be fun to read and may shed light on influences and cultural context, they can also be filled with over-the-top, artistically pretentious language that attempts to make objective statements on what is ultimately a subjective issue. 


# What We Did

With the above context in mind, our team created Album Alchemy, a StreamLit-hosted app where users enter a band name, album name (either fictional or real), select a genre and album score (1-10) and request album alchemy.  The model outputs an AI generated album review and artwork.
"""
)
# ![Figure 1](images/figure_1.png "image_tooltip")

st.image('images/figure_1.png', caption = None)

st.markdown(
"""

**Figure 1. Sample Album Alchemy Output**


# How We Did It

GPT-3.5, or Generative Pre-trained Transformer 3.5 (Brown), is a language model developed by OpenAI. GPT-3.5 (Hereinafter referred to as GPT) It is a neural network that has been trained on a diverse and enormous amount of text data from the internet, and has the advantage of generating high-quality text with limited resources.

For review generation, we used GPT as both a review generation model and prompt-tuning evaluation model. Using the fine-tuned prompts, the model was able to generate human-like Pitchfork-style reviews given the following limited inputs:

* Artist
* Album Name
* Genre
* Rating of the Album (scale 1-10)

For album art generation, we created a two-layer model: we leveraged GPT to generate descriptions of album artwork, which was then ingested into OpenAI’s DALL-E 2 text to image to generate the final album art. 


## Datasets

The base Pitchfork reviews was scraped by Andrew Thompson (Thompson) for reviews written between 1999-2021. The dataset includes the following attributes:

* Artist - The artist/band’s name
* Album	- The name of the album
* Genre	- The musical genre of the album
* Score	- A rating of 1-10 assigned to the album by human reviewers (1-low, 10-high)
* Date - Date of the album release
* Author	- The human reviewer of the album
* Role - The author’s associate with Pitchfork 
* Review - The text containing the review	
* Link - Link to the review on Pitchfork’s website
* Label - The musical label associated with the album and the artist
* Release_year - The year of the album release

A randomized sample of 500 reviews from this dataset were used for this analysis due to OpenAI rate limitations and the cost associated with each API request. The following attributes from this original dataset were incorporated into the prompt provided to the GPT model for generating its own review - Artist, Album, Score and Genre. 


## Prompt Engineering

Prompt engineering was a critical component of model tuning. We created a metric that measured how well our prompt was able to “activate” GPT’s more human-like writing style. The metric was defined as the false positive rate of GPT review, the percent of GPT reviews incorrectly labeled as the human written review. Without a human rater, we leveraged GPT’s self-evaluation capability to establish a benchmark for our prompt performance. We first masked the reviews as the Pitchfork review being “Review A” and the GPT-generated review being “Review B”. Then, we asked GPT to compare the two reviews and identify the human written review for the same Artist, Album, Score and Genre. We built the following custom template for this evaluation (“How to add a custom eval”):

```
You are comparing a model generated review and a human written review. Here are the reviews:


[BEGIN DATA]


************


[Review A]: {review_a}


************


[Review B]: {review_b}


************


[END DATA]


Compare the Review A and Review B, and determine which one is the human written review. Human written reviews are usually natural, smooth and logical.


First, write out in a step by step manner your reasoning to be sure that your conclusion is correct. 


At the end, provide your conclusion in the format of "Conclusion: [Review A|Review B]".


Answer:
```

We set the baseline using the simple prompt’s false positive rate and measured the improvement as we iterated on the prompt structure. The following prompt was finalized and input to GPT along with the album attributes (Artist, Album, Score and Genre) as inputs:

```
You are an agent to help generate human-like reviews for music albums

Write a long and insightful music review for the music album '{album}' by {artist}. The music genre is {genre} with a rating of {score} out of 10. The review must meet the following criteria:

1. Written in a conversational tone, with sophisticated sentence structure and language.
2. Includes details about the band's history and the album's creation story
3. Includes personal experience and opinions
```

Here is one comparison of a real Pitchfork review and a GPT-generated review:

Band - Pink Floyd

Album - The Early Years 1965-1972

Source - Pitchfork (Real)

> Today’s underground may be the answer to tomorrow’s leisure,” intones an earnest British newscaster, narrating film of London’s U.F.O. Club circa January 1967 while its house band, Pink Floyd, jams amid the flashing lights. And darned if he wasn’t right: the black-and-white segment is now found on the massive new $550, 11-CD/9-DVD/8 Blu-Ray box set, Pink Floyd: The Early Years, 1965–1972. With over 27 hours of material, the package overflows with replica 45 rpm singles, gig flyers, posters, tickets, sheet music, and more, and the ark-like box should provide serious leisure-time satisfaction for both longtime Floyd freaks and aspiring heads alike. The Early Years tells the remarkable story of Pink Floyd’s career up through the moment they became part of yesterday’s underground and today’s mainstream, stopping just before the writing and recording of 1973’s Dark Side of the Moon. Charting the band’s progression from the wig-flipping baroque psychedelia of Syd Barrett’s songwriting through their wooliest jams and into the new space beyond, The Early Years doesn’t follow a straight path. It shows an astonishing capacity to turn corners and evolve, a long arc that might give hope to every band jamming away in its practice space in search of a voice. Beginning as a blues combo with the perfectly British drug-punning name the Tea Set (“tea” being slang for weed, maaaan), the band rechristened themselves as the Pink Floyd Sound by the time of the 1965 demo sessions that open the box

Band - Pink Floyd

Album - The Early Years 1965-1972

Source - GPT

> "When it comes to Pink Floyd, it's hard not to be a little bit in awe of what they've accomplished. With over five decades in the music industry and over 250 million records sold, they're a band that has made an indelible mark on the rock genre. That's why I was particularly excited to listen to "The Early Years 1965-1972," a retrospective compilation that covers the formative years of the group.
> 
> This album is an absolute treasure trove for any Pink Floyd fan, particularly those who are invested in the early days of the band. It's impressive to see how Pink Floyd evolved in just a few short years, transforming from a relatively straightforward blues-rock outfit to the avant-garde experimentalists that we all know and love. And let's not forget about the sheer quality of the music. Even during this early period, it's clear that Pink Floyd had a level of songwriting sophistication that was ahead of its time.
> 
> But before I dive into the music itself, let's talk a little bit about the band's history. Pink Floyd got its start in 1965, when guitarist Syd Barrett, bassist Roger Waters, drummer Nick Mason, and keyboardist Richard Wright started playing around the London music scene. The band's early years were marked by a series of singles and live shows, but it wasn't until 1967 that the band truly hit its stride with the release of "The Piper at the Gates of Dawn," an album that showcased Barrett's unique songwriting abilities and experimental sensibilities."


""")

st.image('images/figure_2.png', caption = None)

st.markdown(
"""
**Figure 2. Word cloud representation for the human written review and GPT generated review for the Album - The Early Years 1965-1972 (Pink Floyd)**

A comparison of the review texts do not raise any obvious flags that may point to a “fake” review. This is simultaneously scary and exciting that human readers are unable to spot the difference. A word cloud of the review text also indicates some interesting similarities with one such emphasis on “Barrett”. Any Pink Floyd fan would attest to the psychedelic roots being traced back to Syb Barrett, one of the earlier pioneers of the genre. GPT was able to incorporate this nuance and thereby adding to its credibility. 

Overall, to our team’s eye, the reviews generated by GPT read very similarly to those written by Pitchfork. In the Model Evaluation section, we dive deeper into some of the evaluation methodologies we employed beyond common sense measures to compare the original and GPT generated reviews.


## Album Artwork

To generate album artwork, we prompted GPT again with some user-generated inputs (Artist, Album, Genre) along with the review generated in the previous step:

```
You are an agent to help generate creative descriptions of album artwork.

Write a three sentence description of album artwork for the album '{album}' by {artist}. The band's music genre is {genre}. The description must meet the following criteria:

1. Your response must begin with 'Create an album cover'
2. Uses descriptive language to explain images present in the artwork.
3. Takes into account this recent album review for the band '{review}'
```

The generated output was then fed as input to DALL-E to, in turn, generate album artwork.  Though generated artwork had a difficult time displaying text appropriate to users’ input (see Figure 1), the creative value-add and documented difficulties in producing text on AI generated album covers (Dorobanțu) had our team comfortable including it in our final product.

In order to limit the scope of our project, we focused evaluation efforts on the album reviews only.  A brief discussion of engineering album artwork prompts can be found in the appendix.


# How We Evaluated It


## Memorization

With the proliferation of Large Language Models such as GPT, the model could have already seen the real Pitchfork reviews during training. We wanted to evaluate the level of data contamination, where the model was simply outputting previously seen data instead of generating unique text. One approach to detect such a problem is to use the measure “memorization” which evaluates the overlapping n-grams between the documents being compared (Carlini). Using the _[overlapy](https://github.com/nlx-group/overlapy)_ module (nlx group), we were able to calculate the number of matches for n-gram sizes between 2 and 6 between the GPT-generated review and the real human review for the same Artist, Album, Score and Genre.
""")

st.image('images/figure_3.png',caption = None)

st.markdown(

"""

**Figure 3. Number of matches for different n-gram size**

Figure 3 plots the number of matches (y) against different n-gram sizes (x). At a span of 2, there were many matches between GPT-generated reviews and real pitchfork reviews. The number of matches dropped sharply once we increased to a span of 3, and dropped to 0 matches at a span of 4 and beyond. 

Detecting matches at a span of 2 are less concerning for long documents, think of “is a”, “the album” etc. Longer spans, such as 6, would be a clearer indicator of memorization. However, our documents had rare matches on 3-gram and no matches beyond a span of 4, which indicates that we were less likely to suffer from memorization issues.


## Cosine Similarity 

We then used cosine similarity to evaluate how similar are two documents in terms of their content. The score ranges from 0 to 1, the higher the score the more similar they are. 

We calculated the cosine similarity of 500 Pitchfork reviews and 500 GPT generated reviews for the same Album, Artist, Genre and Rating. Using the _[openai.embeddings_utils](https://github.com/openai/openai-python/blob/main/openai/embeddings_utils.py) _module, we converted reviews to multidimensional vectors, and estimated the cosine similarity between them using the following formula: 

Similarity = Cos (theta) = (A . B) / (||A|| ||B||)
""")

st.image('images/figure_4.png',caption = None)

st.markdown(
"""

**Figure 4. Distribution of the cosine similarities between Pitchfork-review and GPT-generated review**

Figure 4 shows the distribution of the cosine similarities between the real Pitchfork review and GPT-generated reviews. The similarities ranged between 0.80 and 0.98, with a median of 0.92. This score suggests that the GPT-generated reviews and the real Pitchfork reviews were highly similar in terms of content. Based on the memorization metric and cosine similarity score, the GPT model was able to output high-quality reviews that have similar contents to the real review, while not directly replicating the real one.


## T-distributed Stochastic Neighbor Embedding (TSNE)

We used TSNE (Maaten 86) to help visualize the differences in the GPT-generated reviews and the human written reviews. TSNE is a non-linear dimensionality reduction technique which is primarily used for visualizing higher dimensional datasets which is what we have with the textual data. The chart below shows TSNE plot for the sample of GPT-generated and human written reviews for a sample of 500 albums that were previously reviewed in Pitchfork. Review A indicates a human written review and Review B indicates a GPT generated review. We would expect to see some clustering of the Review A and Review B data points if they were disparate enough. However, we don’t see any clear clustering in the TSNE charts indicating that the reviews are quite similar. 
""")

st.image('images/figure_5.png',caption = None)

st.markdown("""
**Figure 5. TSNE visualization of GPT vs Human written reviews**


# What’s Next?

At the outset of this journey, our team set out to leverage existing large language models to generate reviews that look as closely to Pitchfork’s human written reviews as possible. We wanted to build something fun for users to interact with that would give us more hands-on experience incorporating new technologies into live products. We also wanted to build off of preexisting work on the same topic, specifically Pitchfork review generator created by Jules Becker (Becker) with Components. In the end, we improved on their concept by:

1. Using GPT-3.5 instead of GPT-2
2. Offering end-users the option to choose their own band name and personalize their review to that band
3. Using GPT and Dall-E 2 to generate album artwork
4. Using prompt engineering instead of fine-tuning to generate reviews more similar to real reviews 

There are still many interesting work that could be done for our projects:

1. Our current fine-tuned prompt has a false positive rate of 53%, which means it is able to trick the rater to believe it is written by a human 53% of the time. We can continue to explore more sophisticated prompts that could “activate” GPT’s more human-like writing style.
2. Our memorization metric only compared the n-gram overlaps between the GPT-generated review and the human written Pitchfork review of the same Artist, Album, Score and Genre. We can extend the evaluation to GPT-generated reviews against all Pitchfork reviews.

Though we don’t anticipate our project to send ripples into the musical criticism industry, we have demonstrated that GPT has the potential to write reviews that are indistinguishable from human written reviews and acknowledge the far-reaching impacts of such a reality.  The music industry will be forced to reckon with such far-reaching impact.  Everything from song writing, composition and album artwork has the potential to be disrupted in a significant way. Music critics, who also play a critical role in setting cultural tastes, will be forced to evaluate what the future of their profession looks like and whether generative AI has a place in it. 

With any new groundbreaking technology comes a new set of ethical concerns and generative AI is no exception. For one, though the GPT model used in our project has some guardrails in place to mitigate hateful and harmful speech from their AI, examples such harmful content abound throughout the internet (“Researchers discover a way to make ChatGPT consistently toxic”). 


# Statement of Work

* Kevin Borah (kborah@umich.edu) - Project management, Streamlit App development, Album artwork generation
* Carine Zhang (carinez@umich.edu) - GPT reviews generation and analysis
* Charith Tammineedi (charith@umich.edu) - Stable diffusion exploration, Report coordination


# Appendix 


## Album Review Prompt Engineering

We defined a “false positive rate” metric for evaluating the performance of the GPT-generated reviews. The metric measured the percent of GPT-generated reviews that were misclassified as the human written review when blind-compared against the actual human written review for the same Artist, Album, Score and Genre. The higher the false positive rate, the better the GPT-generated review.

Since we didn’t have the resources to hire real human reviewers, we explored other avenues to gather labels. We decided to use GPT’s self evaluation capabilities to generate labels. We discussed the actual eval template we employed to activate GPT’s evaluation capabilities in the Prompt Engineering section. Below is the false positive rate for our baseline prompt and our final prompt.
""")

st.image('images/figure_6.png',caption=None)

st.markdown("""            
**Figure 6. False Positive Rate for Baseline and Final Prompt**

Our baseline prompt was:
```
Write a short music review for the music album '{album}' by {artist}. The music genre is {genre} with a rating of {score} out of 10.
```

The evaluation model was always able to detect the GPT-generated review was _not _the human written review. Whereas, our fine-tuned prompt was able to trick the evaluation model 53% of the times, slightly better than random guessing. 


## Album Artwork Prompt Engineering

As previously mentioned, our team chose to limit evaluative efforts to our model’s text outputs.  Future iterations of this project may choose to focus their efforts on evaluating how well GPT and DALL-E work to generate album artwork.

Though the inclusion of generated album artwork was just for fun, we spent some time developing prompts to create more fun, creative images.  Originally, our model requested an album cover directly from DALL-E (ex: “generate an album cover by {band_name} for album ‘{album_name}’ of music genre {genre}.”).  Outputs from this stage of development were less creative and more boring than outputs from our model’s final iteration.
""")

col1,col2 = st.columns(2)

with col1:
    st.image('images/figure_7a.png',caption=None)

with col2:
    st.image('images/figure_7b.png',caption=None)

st.markdown("""
**Figure 7. Sample outputs when DALL-E prompted directly**
""")

col1,col2 = st.columns(2)

with col1:
    st.image('images/figure_8a.png',caption=None)

with col2:
    st.image('images/figure_8b.png',caption=None)

st.markdown("""

**Figure 8. Sample outputs when GPT incorporates its own review to write album artwork description**


## Exploratory Word Clouds

Word clouds display the frequency of words with the size of the word encoded to show the frequency of usage in a document. This is another useful visualization when performing exploratory analysis of textual data. Shown here are the comparisons of the reviews (top 20 words) for the albums Breakin’ Point and Pullhair Rubeye. This is another fun way to compare the two review sources. As expected, the words ‘album’, ‘song’, the band name, the album name dominate the word clouds but other than that there are no easy ‘tells’ on what constitutes a real review vs. a fake review. 
""")

st.image('images/figure_9.png',caption=None)

st.markdown("""
**Figure 9: Exploratory Word Clouds of the reviews for Breakin’ Point and Pullhair Rubeye**


## Stable Diffusion 

We initially explored the use of the Stable Diffusion model (Rombach and Blattmann) for text to image generation for album art. We were able to use a forked version (stable-diffusion-v1-4) (Rombach et al.) to generate some basic images. While we were able to develop a working version, the runtime was quite high and not feasible for real-time application. As a future exploration, we would like to integrate the Stable Diffusion model to generate the album art. 


# References


Becker, Jules. “Building a Pitchfork text generator with GPT-2.” _Components_, 4 July 2020, https://components.one/documentation/gpt-2-pitchfork-generator-tutorial. Accessed 16 April 2023.


Brown, Tom B. “[2005.14165] Language Models are Few-Shot Learners.” _arXiv_, 28 May 2020, https://doi.org/10.48550/arXiv.2005.14165. Accessed 16 April 2023.


Carlini, Nicholas. “Quantifying Memorization Across Neural Language Models.” _arXiv_, 15 February 2022, https://doi.org/10.48550/arXiv.2202.07646. Accessed 16 April 2023.


Dorobanțu, Miriana. “I recreated famous album covers with DALL-E.” _Lucy Talks Data_, 20 August 2022, https://lucytalksdata.com/i-receated-famous-album-covers-with-dalle/. Accessed 16 April 2023.


“How to add a custom eval.” _GitHub_, https://github.com/openai/evals/blob/main/docs/custom-eval.md. Accessed 16 April 2023.


K, M. H. “The Unseen World.” _The New Republic_, vol. 14, 1918, p. 63.


Kivy, Peter. “A New Music Criticism.” _The Monist_, vol. 73, no. 2, 1990, p. 247. _JSTOR_, http://www.jstor.org/stable/27903184. Accessed 16 April 2023.


Maaten, Laurens van der. “Visualizing Data using t-SNE.” _Journal of Machine Learning Research_, vol. 9, 2008.


nlx group. “Python package developed to evaluate textual overlap (N-Grams) between two volumes of text.” _GitHub_, 23 September 2021, https://github.com/nlx-group/overlapy. Accessed 16 April 2023.


“Researchers discover a way to make ChatGPT consistently toxic.” _TechCrunch_, 12 April 2023, https://techcrunch.com/2023/04/12/researchers-discover-a-way-to-make-chatgpt-consistently-toxic/. Accessed 16 April 2023.


Rombach, Robin, et al. “CompVis/stable-diffusion-v1-4 · Hugging Face.” _Hugging Face_, https://huggingface.co/CompVis/stable-diffusion-v1-4. Accessed 16 April 2023.


Rombach, Robin, and Andreas Blattmann,. “High-Resolution Image Synthesis with Latent Diffusion Models.” _arXiv_, 20 December 2021, https://arxiv.org/abs/2112.10752. Accessed 16 April 2023.


Thompson, Andrew. “20783 Pitchfork Reviews.” _Components_, 8 February 2019, https://components.one/datasets/pitchfork-reviews-dataset. Accessed 16 April 2023.


"""

)