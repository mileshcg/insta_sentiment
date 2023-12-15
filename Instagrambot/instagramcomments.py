#Link to the instagrapi github: https://subzeroid.github.io/instagrapi/
from instagrapi import Client
from instagrapi.exceptions import (LoginRequired, BadPassword, PleaseWaitFewMinutes)
import pandas as pd
import numpy as np
import time

with open("credentials.txt", "r") as f:
    username, password, session_id = f.read().splitlines()

#start the client and login to our scraping account
client = Client()
try:
    client.login(username=username, password=password)
    print("work")
except BadPassword:
    print("didn't")
    client.login_by_sessionid(session_id)

#add a delay between api calls so we dont get banned :D
client.delay_range = [3, 6]

#return a dataframe
fields = ["media_id"]
i = 1
while (i < 51):
    fields.append(str(i))
    i = i + 1
comments = pd.DataFrame(columns=fields)
df = pd.read_csv("instagram_data.csv")
index = 0
try:
    for ind in df.index:
        #shove the comments into the row, with the first variable being the media id
        row = []
        #start the row with the media_id
        media_id = df["media_id"][ind]
        row.append(media_id)
        #grab the last 50 comments
        media_comments = client.media_comments_chunk(media_id, 50, None)
        print("got comments")
        comment_texts = [comment.text for comment in media_comments[0]][:50]  # Get up to 50 comments
        comment_texts += ['n/a'] * (50 - len(comment_texts))
        for comment in comment_texts:
            row.append(comment)
        comments.loc[index] = row
        index = index + 1
        print(f"processed comments of media {media_id}")
except LoginRequired:
    client.relogin()
    for ind in df.index:
        #shove the comments into the row, with the first variable being the media id
        row = []
        #start the row with the media_id
        media_id = df["media_id"][ind]
        row.append(media_id)
        #grab the last 50 comments
        media_comments = client.media_comments_chunk(media_id, 50, None)
        print("got comments")
        comment_texts = [comment.text for comment in media_comments[0]][:50]  # Get up to 50 comments
        comment_texts += ['n/a'] * (50 - len(comment_texts))
        for comment in comment_texts:
            row.append(comment)
        comments.loc[index] = row
        index = index + 1
        print(f"processed comments of media {media_id}")
comment_file_name = 'comments.csv'
comments.to_csv(comment_file_name, sep=',', index=False)