import nltk
nltk.download("stopwords")
nltk.download("punkt")
from nltk.corpus import stopwords
import pandas as pd
import numpy as np


#Emoji unicode file pulled from this github: https://github.com/NeelShah18/emot/blob/master/emot/emo_unicode.py
from emo_unicode import UNICODE_EMOJI

unicodes = [uni for uni in UNICODE_EMOJI]
stop_words = set(stopwords.words("english"))

def tokenize(sentence):
    return nltk.word_tokenize(sentence)
def remove_stopwords(tokens):
    return [non_stop for non_stop in tokens if not non_stop.lower() in stop_words]
def remove_emoji(tokens):
    return [non_emoji for non_emoji in tokens if not non_emoji.encode('utf-8') in unicodes]

df = pd.read_csv("comments.csv")
df = df.drop('media_id', axis=1)

for indx in df.index:
    for indy in range(1, df.shape[1] + 1):
        df[str(indy)][indx] = " ".join(remove_emoji(remove_stopwords(tokenize(str(df[str(indy)][indx])))))

df.to_csv("comments_cleaned.csv", sep=",", index=False)