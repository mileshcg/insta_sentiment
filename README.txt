Software usage guide:

Modules to install:

	1. Instagrapi and its dependencies: https://subzeroid.github.io/instagrapi/

	2. Pandas

	3. Numpy

	4. NLTK and its dependencies: https://www.nltk.org/install.html#

	5. scikit-learn

Exploring the data and final results (if you want to skip building the dataset yourself because it takes a while):
	
	1. Ensure final_data.csv is in the machine learning folder as well as the jupyter file: sentiment_machine_learning.

	2. Open sentiment_machine_learning, and load the cells in order to see the final results of the project

Load Order from Scratch:

	Instagrambot

		1. Fill out the credentials text with an instagram account's username, password, and session_id (which can be acquired in the application cookies section when opening developers' tools on instagram).

		2. Run instabot.py, which will output instagram_data.csv. You can modify the dataset in the code here by adding/deleting account names to the user_ids variable.

		3. Run instagramcomments.py, which will output comments.csv

		4. Run instagramfollowers.py, which will modify instagram_data.csv

	Sentimentanalysis

		1. Copy over from Instagrambot instagram_data.csv, and comments.csv into the folder.

		2. Run clean_comments.py, which will output comments_cleaned.csv

		3. Run sentiment_analysis.py, which will output final_data.csv.

	Machinelearning

		1. Copy over from Sentimentanalysis final_data.csv

		2. Open the sentiment_machine_learning jupyter file, and explore the results of your

Important variables:
	1. client.delay_range[n, x]: found in instabot.py, instagramcomments.py, & instagramfollowers.py, this variable sets a random delay between n & x seconds between api calls; this is to mimic actually browsing instagram and being respectful to their api.
	2. user_ids: found in instabot.py, this variable is contains a list of account id's which we used to build our dataset. To build a larger or smaller dataset, just add or remove accounts in the same format: client.user_id_from_username(username) 

csv/txt file descriptions:

	1. credentials.txt: contains username, password, and session_id of an instagram account

	2. instagram_data.csv: a csv containing the post data of certain users' last 20 posts. data saved includes: media_id, media_type, # of followers, # of comments, # of likes.

	3. comments.csv: a csv containing  the last 50 comments for the posts mentioned in instagram_data.csv

	4. comments_cleaned.csv: a csv which contains the comments of comments.csv, but with the comment tokenized, stopwords removed, and emojis removed.

	5. final_data.csv: a csv with all the data in instagram_data.csv, but includes the average sentiment analysis score for a posts set of comments.