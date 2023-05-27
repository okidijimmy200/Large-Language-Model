import os
from datetime import datetime, timezone
import logging, tweepy

logger = logging.getLogger('twitter')

twitter_client = tweepy.Client(
    bearer_token=os.environ.get('TWITTER_BEARER_TOKEN'),
    consumer_key=os.environ.get('TWITTER_API_KEY'),
    consumer_secret=os.environ.get('TWITTER_API_SECRET'),
    access_token=os.environ.get('TWITTER_ACCESS_TOKEN'),
    access_token_secret=os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
)

def scrape_user_tweets(username, num_tweets=1):
    # call client with get user
    print('test')
    user_id = twitter_client.get_user(username=username).data.id
    print(user_id)
    tweets = twitter_client.get_users_tweets(id=user_id, max_results=num_tweets, excludes=['retweets', 'replies'])

    tweet_list = []
    for tweet in tweets.data:
        tweet_dict = {}
        tweet_dict['text'] = tweet['text']
        tweet_dict[
            'url'
        ] = f'http://twitter.com/{username}/status/{tweet.id}'
        tweet_list.append(tweet_dict)

    return tweet_list

if __name__ == '__main__':
    print(scrape_user_tweets(username='aei_ug'))

