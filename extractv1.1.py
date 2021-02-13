
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to


# Using TwitterSearchScraper to scrape data and append tweets to list

file1 = open('searchFile.txt', 'r')
Lines = file1.readlines()

month=6

complete_tweets=[]
tweets_list=[]
count=0

for line in Lines:
	print(line)
	
	if line == "STOP":
		# Creating a dataframe from the tweets list above
		tweets_df2 = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

		# Display first 5 entries from dataframe
		tweets_df2.head()

		# Export dataframe into a CSV
		filename=str(month)+".csv"
		tweets_df2.to_csv(filename, sep=',', index=False)
		print(str(month)+" Done")
		month=month+1
		tweets_list=[]
	else:
		search=line
		for i,tweet in enumerate(sntwitter.TwitterSearchScraper(search).get_items()):
		    if i>10:
		        break
		    tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
		    complete_tweets.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
		    
	#complete_tweets.append(tweets_list)	
	count=count+1
	print(str(count))
	if count==3:
		break;


tweets_df2 = pd.DataFrame(complete_tweets, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

# Display first 5 entries from dataframe
tweets_df2.head()

# Export dataframe into a CSV
filename="complete_tweets.csv"
tweets_df2.to_csv(filename, sep=',', index=False)

"""
file1=open('temp.txt','w')
for line in complete_tweets:
	file1.write(str(line))

	"""




