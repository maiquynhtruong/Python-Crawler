# Python-Crawler
A crawler in Python to crawl Reddit.
Specifically, it will crawl the subreddit /r/dailyprogrammer, find all the challenges, sort them according to the difficulty level, and display the challenge in a table. The table has three columns: 'Easy', 'Intermediate', 'Hard' for the types of the challenges.

The challenge is https://www.reddit.com/r/dailyprogrammer/comments/41hp6u/20160118_challenge_250_easy_scraping/

reddit_crawler.py contains the code without using the API.

reddit_crawler_with_api.py contains the code made using API.

The output is in the file [output.md](/output.md)

# How to run
- git clone this repo to your local machine
- Install praw for the API wrapper
- Change the user-agent to your name
- ``python reddit_crawler_api.py``
- If you want to change the output filename, do so in the first line of ``show_challenges()`` function
