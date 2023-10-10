#!/usr/bin/python3
"""
2. Recurse it!
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    recursive function that queries the reddit api
    """
    if subreddit is None:
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'RedditSubscriberApp/1.0'}
    params = {'limit': 10, 'after': after} if after else {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            for post in posts:
                title = post['data']['title']
                hot_list.append(title)

            after = data['data']['after']
            if after:
                recurse(subreddit, hot_list, after)
            return hot_list
        elif response.status_code == 302:
            return None
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")
        return None
