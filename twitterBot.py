import tweepy
from Tkinter import *

# consumer_key = 'PR4wZK71LkCxSUdh5pAtl2rAc'
# consumer_secret = 'RehctIAnCa8jtiJvkq2IpXWkEiOAAWQWkNBKyxisLO4Xz7NDD7'
# access_token = '32966075-8cvYCHDT6Kb6o8exAmdp7tKHah9g6TEdsBrjhtcNm'
# access_token_secret = 'qkZ7aUSZvP9gkfrvJvzQrLoHpvizl4nwUah2ysu0lfva5'

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)
# user = api.me()
# print (user.name)


# # for follower in tweepy.Cursor(api.followers).items():
# # 	follower.follow()
# # 	print ("followed everyone that is following you " + user.name)

# def mainFunction():
# 	search = "dilly dilly"
# 	numberOfTweets = 5
	




# 	for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
# 		try: 
# 			tweet.retweet()
# 			print ('Retweeted the tweet')
# 		except tweepy.TweepError as e:
# 			print (e.reason)
# 		except StopIteration:
# 			break

# 	tweetID = tweet.user.id
# 	username = tweet.user.screen_name
# 	phrase = "hello dilly dilly my friends"


# 	for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
# 		try: 
# 			tweetId = tweet.user.id
# 			username = tweet.user.screen_name
# 			api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId) 
# 			print ("Replied with " + phrase)
# 		except tweepy.TweepError as e:
# 			print(e.reason)
# 		except StopIteration:
# 			break

# mainFunction()

root = Tk()

label1 = Label(root, text = "search")
E1 = Entry(root, bd = 5)

label2 = Label(root, text = "Number of Tweets")
E2 = Entry(root, bd = 5)

label3 = Label(root, text = "Response")
E3 = Entry(root, bd = 5)

label4 = Label(root, text = "Reply?")
E4 = Entry(root, bd = 5)

label5 = Label(root, text = "Retweet?")
E5 = Entry(root, bd = 5)

label6 = Label(root, text = "Favourite?")
E6 = Entry(root, bd = 5)

label7 = Label(root, text = "Follow?")
E7 = Entry(root, bd = 5)


label1.pack()
E1.pack()

root.mainLoop()







