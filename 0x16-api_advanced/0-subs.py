#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Query the Reddit API to return the number of subscribers for a given subreddit.
    If an invalid subreddit is given, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get('data', {}).get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0

# Testing the function with the provided examples
print(number_of_subscribers("programming"))  # Expected: Some positive integer
print(number_of_subscribers("this_is_a_fake_subreddit")) 