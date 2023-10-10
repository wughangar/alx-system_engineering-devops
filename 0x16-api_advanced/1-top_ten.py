#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    function that queries subredit hot topics
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'RedditSubscriberApp/1.0'}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            posts = data['data']['children']
            for i, post in enumerate(posts[:10], 1):
                title = post['data']['title']
                print(f"{title}")

        elif reponse.status_code == 302:
            return 0
        else:
            return 0

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")
        return 0
