import tweepy
from Tkinter import *

consumer_key = 'PR4wZK71LkCxSUdh5pAtl2rAc'
consumer_secret = 'RehctIAnCa8jtiJvkq2IpXWkEiOAAWQWkNBKyxisLO4Xz7NDD7'
access_token = '32966075-8cvYCHDT6Kb6o8exAmdp7tKHah9g6TEdsBrjhtcNm'
access_token_secret = 'qkZ7aUSZvP9gkfrvJvzQrLoHpvizl4nwUah2ysu0lfva5'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.me()
print (user.name)
print (user.location)

# for follower in tweepy.Cursor(api.followers).items():
# 	follower.follow()

# print ("followed everyone that is following you " + user.name)

root = Tk()

label1 = Label(root, text = "Search")
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


def getE1():
	return E1.get()

def getE2():
	return E2.get()

def getE3():
	return E3.get()

def getE4():
	return E4.get()

def getE5():
	return E5.get()

def getE6():
	return E6.get()

def getE7():
	return E7.get()


def mainFunction():
 	getE1()
 	search = getE1()

 	getE2()
 	numberOfTweets = getE2()
 	numberOfTweets = int(float(numberOfTweets))

 	getE3()
 	phrase = getE3()

 	getE4()
 	reply = getE4()

 	getE5()
 	retweet = getE5()

 	getE6()
 	favourite = getE6()

 	getE7()
 	follow = getE7()

	for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
		try: 
			#Reply
			print ('\nTweet by: @' + tweet.user.screen_name)
			print ('ID: @' + str(tweet.user.id))
			tweetID = tweet.user.id
 			username = tweet.user.screen_name
 			api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetID)
 			#phrase = "hello dilly dilly my friends"
			#print ("replied with the {}".format(phrase))
			print ("Replied with " + phrase)
		except tweepy.TweepError as e:
			print (e.reason)
		except StopIteration:
			break

	for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
		if retweet == 'yes':
			try: 
				#Retweet
				tweet.retweet()
				print ('Retweeted the tweet {}'.format(tweet.user.screen_name) )
			except tweepy.TweepError as e:
				print(e.reason)
			except StopIteration:
				break

	if favourite == 'yes':
		for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
			try:
				#Favourite
				tweet.favourite()
				print 'Favourited the {}'.format(tweet.user.screen_name)

			except tweepy.TweepError as e:
				print (e.reason)
			except StopIteration:
				break

	if follow == 'yes':
		for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
			try:
				#Follow
				tweet.user.follow()
				print ('Followed {}').format(tweet.user.screen_name)
			except tweepy.TweepError as e:
				print (e.reason)
			except StopIteration:
				break
			
submit = Button(root, text = "Submit", command = mainFunction)

label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
label4.pack()
E4.pack()
label5.pack()
E5.pack()
label6.pack()
E6.pack()
submit.pack(side = BOTTOM)

root.mainloop()





















