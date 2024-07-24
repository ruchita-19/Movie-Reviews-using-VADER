import streamlit as st
import base64
import matplotlib.pyplot as plt
import nltk
import spacy
import pandas as pd
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sa = SentimentIntensityAnalyzer()
st.set_page_config(layout="wide")




def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
# add_bg_from_local("D:/SIXTH SEMISTER/bg_blur.jpg")



st.markdown("""
<style>
.head{
font-size:75px !important;
font-family:sans-serif;
color:red;
text-align:center;
}
.head1{
font-size:60px !important;
font-family:sans-serif;
color:green;
text-align:center;
}
.big-font {
    font-size:300px !important;
    text-align:center;
}
.emo-text1{
font-size:60px !important;
font-family:sans-serif;
color:green;
}
.emo-text2{
font-size:60px !important;
font-family:sans-serif;
color:red;
}
.emo-text3{
font-size:60px !important;
font-family:sans-serif;
color:orange;

}
.text {
font-size:80px !important;
font-family:sans-serif;
color:Purple;
}
</style>
""", unsafe_allow_html=True)


st.markdown('<h1 class="head" >SENTIMENT ANALYSIS</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="head1" >USING VADER</h2>', unsafe_allow_html=True)

review = st.text_input("Enter Review Here")
one = st.button('See Review')


def emojify(a: float):  # a-->dict['compound']

    if a > 0.6:
        st.markdown('<p class="emo-text1" >Loved The Film, Must Watch!!</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">\U0001F970</p>', unsafe_allow_html=True)
    elif a > 0.5:
        st.markdown('<p class="emo-text1">Great Film, Good to Watch</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">\U0001F642</p>', unsafe_allow_html=True)
    elif a > 0.35:
        st.markdown('<p class="emo-text3">Nice Movie , Good</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">\U0001F642</p>', unsafe_allow_html=True)
    elif a > 0.2:
        st.markdown('<p class="emo-text3">Not Good Actually , One time Watchable</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">\U0001F612</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="emo-text2">Bad Film, Better Not to go!!</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">\U0001F972</p>', unsafe_allow_html=True)


def graph(data):
    st.bar_chart(data,use_container_width=True)


def onee(q:float):
    (emojify(q))

def pree1(a):
    c=0
    neg = ['but', 'despite', 'yet', 'however', 'unless', 'rather', 'although', 'even though','and']
    for i in neg:
        if i in a:
            c = c + 1
    if c > 0:
        def pre(a):
            for i in neg:
                if i in a:
                    x = i
            l = []
            l.append(a.split(x))

            l1 = []
            for i in range(0, len(l) + 1):
                l1.append((sa.polarity_scores(l[0][i])))

            l2 = []
            for i in l1:
                l2.append(i['compound'])
            return l2

    if c>0:


        # print(pre(a))
        ans = []
        ans = pre(a)
        s: float = 0.0
        for i in ans:
            s = s + i
        if (s < 0):
            return(min(ans))
            # print("Negative review in it")
        else:
            return(max(ans))
            # print("Positive Review in it")
    else:
        dict=(sa.polarity_scores(a))
        x=dict['compound']
        if x>0:
            return(x)
        else:
            return(x)

# print(pree1(a))






if one:
    dict = sa.polarity_scores(review)
    x=pree1(review)
    onee(x)
    data = {"Attribute": list(dict.keys()), "Scores": list(dict.values())}
    data = pd.DataFrame(data)
    data = data.set_index("Attribute")
    graph(data)