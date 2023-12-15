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
df = pd.read_csv("instagram_data.csv")
index = 0

try:
    row = []
    for ind in df.index:
        user_id = str(df["media_id"][ind]).split('_')[1]
        user_info = client.user_info(user_id).dict()
        row.append(int(user_info['follower_count']))
        print(ind)
    df.insert(df.shape[1], 'follower_count', row, allow_duplicates=True)
except LoginRequired:
    client.relogin()
    row = []
    for ind in df.index:
        user_id = str(df["media_id"][ind]).split('_')[1]
        user_info = client.user_info(user_id).dict()
        row.append(user_info['follower_count'])
    df.insert(df.shape[1], 'follower_count', row, allow_duplicates=True)
        
comment_file_name = 'instagram_data.csv'
df.to_csv(comment_file_name, sep=',', index=False)