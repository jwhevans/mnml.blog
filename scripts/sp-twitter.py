#!/usr/bin/python3

from secrets import twitter as ts
import twitter
from datetime import datetime

t_path = f"./.last_tweet"
path = f"../content/river/"
handle = f"jwhevans"


def main():
    api = twitter.Api(
        consumer_key=ts["CONSUMER_KEY"],
        consumer_secret=ts["CONSUMER_SECRET"],
        access_token_key=ts["ACCESS_TOKEN_KEY"],
        access_token_secret=ts["ACCESS_TOKEN_SECRET"],
    )

    last_tweet = get_last_tweet(f"./.last_tweet")
    t = api.GetUserTimeline(screen_name=handle, since_id=last_tweet)

    try:
        latest_tweet = max(t, key=lambda x: x.id).id
        set_last_tweet(t_path, latest_tweet)
        store_new_tweets(t)

    except ValueError:
        pass


def store_new_tweets(data=None):
    tweets = [i.AsDict() for i in data]

    for t in tweets:
        # Twitter stores the created date in the format
        # Mon May 31 12:18:34 +0000 2021
        # %a  %b  %d %H:%M:%S %z    %Y
        # Create a datetime from the string twitter returns
        dt = datetime.strptime(t["created_at"], "%a %b %d %H:%M:%S %z %Y")

        # Format the twitter datetime as a string for use in the
        # front matter of my Hugo markdown files
        ds = datetime.strftime(dt, "%Y%M%D%H%M%S")
        dp = datetime.strftime(dt, "%Y-%M-%DT%H:%M:%S")

        # Create each tweet as a post. The filename of the post
        # is the tweet id. Front matter is formatted in YAML
        # The tweet is embedded as a Hugo Tweet shortcode
        f = open(f"{path}{t['id']}.md", "w+")
        f.write(f"---\n")
        f.write(f"slug: {t['id']}\n")
        f.write(f"date: {dt}\n")
        f.write(f"draft: false\n")
        f.write(f"---\n")
        f.write(f"\n")
        f.write("{" + f"{{< tweet {t['id']} >}}" + "}\n")
        f.close()


def get_last_tweet(url=None):
    f = open(f"{url}", "r")
    last_tweet = f.readline()
    f.close()

    return last_tweet


def set_last_tweet(url=None, id=None):
    f = open(f"{url}", "w+")
    f.write(f"{id}")
    f.close()


if __name__ == "__main__":
    main()
