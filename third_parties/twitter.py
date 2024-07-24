def scrape_user_tweets(username, num_tweets=5, mock:bool = False):
    """
    Scrapes a Twitter user's original tweets (i.e., not retweets ot replies) and returns them as
    a list of dictionaries. Each dictionary has three fields: "time_posted" (relative to now), "text", and "url"
    :param username:
    :param num_tweets:
    :param mock:
    :return:
    """


if __name__ == "__main__":
    tweets = scrape_user_tweets(username="EdenEmarco117")
    print(tweets)