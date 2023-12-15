#Link to the instagrapi github: https://subzeroid.github.io/instagrapi/
from instagrapi import Client
from instagrapi.exceptions import (LoginRequired, BadPassword)
import pandas as pd
import numpy as np
import csv

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
client.delay_range = [2, 5]


#scrape 10 public figures 20 most recent posts for num of likes, comments, and views
#trying to go for a good mix of well liked and disliked public figures/organizations with mixed backgrounds so we don't have a useless dataset
user_ids = [client.user_id_from_username("mrbeast"), client.user_id_from_username("igndotcom"), client.user_id_from_username("jakepaul"), client.user_id_from_username("tanamongeau"), client.user_id_from_username("tomholland2013"), client.user_id_from_username("blizzard"), client.user_id_from_username("mileycyrus"), client.user_id_from_username("champagnepapi"), client.user_id_from_username("caradelevingne"), client.user_id_from_username("rockstargames")]
print(user_ids)
#for every user export a post as a csv file line, with likes views and comments
dictionary = {'likes': [], 'comment_count': [], 'mediatype': [], 'media_id' : []}
#dataframes can't have more than 2 dimensions it seems, so we have to put them in their own csv file (yay........)
fields = []
row = []
i = 1
while (i < 51):
    fields.append(str(i))
    row.append("n/a")
    i = i + 1
df = pd.DataFrame(data=dictionary)
comments = pd.DataFrame(columns=fields)
index = 0
for user_id in user_ids:
    #gets the users last 20 posts as a media list if they have 20 posts
   medias = client.user_medias(user_id, 20)
   for media in medias:
    media_info = media.dict()
    media_id = client.media_id(media_info['pk'])
    df.loc[index] = [media_info["like_count"], media_info["comment_count"], media_info["media_type"], media_id]
    #where we should add our comments to rows
    comments.loc[index] = row
    index = index + 1
    print(f"processed media number {index}")
#print what we are about to export
print(df)
#export as a csv
file_name = 'instagram_data.csv'
comment_file_name = 'comments.csv'
df.to_csv(file_name, sep=',', index=False)
comments.to_csv(comment_file_name, sep=',', index=False)