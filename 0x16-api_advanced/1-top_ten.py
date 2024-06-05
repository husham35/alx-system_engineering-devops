#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Gets the titles of the top 10 hot posts
    Args:
        subreddit (str): subreddit
    Returns:
        (str): if valid subreddit, titles of the top 10 posts, else None
    """
    headers = {'User-agent': 'Custom'}
    params = {
        'limit': 10
    }

    try:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        res = requests.get(url, headers=headers,
                           params=params, allow_redirects=False)

        results = res.json()['data']['children']
        for post in results:
            print(post['data']['title'])
    except Exception:
        print(None)
