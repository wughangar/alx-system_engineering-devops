#!/usr/bin/python3
"""
0. How many subs?
"""

import requests


def number_of_subscribers(subreddit):
    """
    function that queries reddit api and returns number of subcribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'RedditSubscribersApp/1.0'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers

        elif response.status_code == 302:
            return 0
        else:
            return 0
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")
        return 0
