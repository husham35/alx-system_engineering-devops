#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Gets a list containing the titles of all hot
    articles for a given subreddit.
    Args:
        subreddit (str): subreddit
        hot_list (list): hot list
    Returns:
        (str): titles of top 10 posts for a valid subreddit, else None
    """
    headers = {'User-agent': 'Custom'}
    params = {
        'after': after,
        'count': count,
        'limit': 100
    }
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    res = requests.get(url, headers=headers,
                       params=params, allow_redirects=False)

    if res.status_code == 404:
        return None

    results = res.json().get("data")
    after_data = results.get("after")
    count += results.get("dist")

    for post in results.get("children"):
        hot_list.append(post.get("data").get("title"))

    if after_data is not None:
        return recurse(subreddit, hot_list, after_data, count)
    return hot_list
