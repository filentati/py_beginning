from typing import List
from collections import defaultdict, deque


class Twitter:

    def __init__(self):
        self.users_tweets = defaultdict(deque)
        self.following = defaultdict(set)
        self.time = 0

    def post_tweet(self, user_id, tweet_id):
        self.users_tweets[user_id].appendleft((self.time, tweet_id))
        self.time += 1
        if len(self.users_tweets[user_id]) > 10:
            self.users_tweets[user_id].pop()

    def get_news_feed(self, user_id) -> List[int]:
        news_feed = []
        
        for followee in self.following[user_id]:
            news_feed.extend(self.users_tweets[followee])
            
        news_feed.sort(reverse=True)
        
        return [tweet_id for time, tweet_id in news_feed[:10]]
            

    def follow(self, follower_id, followee_id):
        self.following[follower_id].add(followee_id)

    def unfollow(self, follower_id, followee_id):
        if followee_id in self.following[follower_id]:
            self.following[follower_id].remove(followee_id)

twitter = Twitter()
twitter.follow(1, 2)
twitter.follow(1, 3)
twitter.post_tweet(2, 4)
twitter.post_tweet(2, 6)
twitter.post_tweet(3, 2)
twitter.post_tweet(3, 7)
twitter.post_tweet(3, 3)
twitter.post_tweet(3, 8)
twitter.post_tweet(2, 1)
twitter.post_tweet(2, 9)
twitter.follow(1, 4)
twitter.post_tweet(4, 5)
twitter.post_tweet(4, 10)
twitter.unfollow(1, 2)
twitter.post_tweet(5, 11)
twitter.post_tweet(5, 12)
twitter.post_tweet(5, 13)
twitter.post_tweet(6, 14)
twitter.follow(1, 5)
twitter.post_tweet(7, 15)
twitter.post_tweet(7, 16)
twitter.post_tweet(7, 17)
twitter.post_tweet(7, 18)
twitter.follow(1, 7)
print(twitter.get_news_feed(1))
