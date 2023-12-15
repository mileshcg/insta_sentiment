import nltk
import pandas as pd
import numpy as np
from nltk.sentiment import SentimentIntensityAnalyzer


#open the main data csv and comments csv
main_df = pd.read_csv("instagram_data.csv")
comments_df = pd.read_csv("comments_cleaned.csv")
average_sentiments = []
sentiment_analyzer = SentimentIntensityAnalyzer()
for ind in comments_df.index:
	#nested for loop go brrrr
	sentiment_compound_total = 0
	#pandas dataframe magic, convert a pandas dataframe row, make it to a numpy array, so we can change it to a list lol
	i = 0
	for comments in comments_df.loc[ind, :].values.flatten().tolist():
		sentiment_scores = sentiment_analyzer.polarity_scores(str(comments))
		print(sentiment_scores)
		if (float(sentiment_scores['compound']) != 0):
			sentiment_compound_total = sentiment_compound_total + float(sentiment_scores['compound'])
			i = i + 1
	#get the compound average by taking the total and dividing by the num of columns
	if (i != 0):
		sentiment_compound_average = round(sentiment_compound_total / i, 4)
	else:
		sentiment_compound_average = 0
	print(sentiment_compound_average)
	#append the average to the list
	average_sentiments.append(sentiment_compound_average)
#finally, add a new column to the main df
main_df.insert(main_df.shape[1], 'sentiment_average', average_sentiments, allow_duplicates=True)
#now convert the main_df to the final csv
main_df.to_csv('final_data.csv', sep=',', index=False)
