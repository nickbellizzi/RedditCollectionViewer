# Reddit Collection Viewer

## Motivation
Often times, one recalls the content of a Reddit post, but unfortunately there is no simple way to sort through posts one has either upvoted or saved. This was created to crawl through a user's upvoted and saved posts to quickly extract submissions that match a certain subreddit or search term.

## Set up
The driver code for this function is in `rcv.py` and configuration information can be placed in the file `config.py`. This requires a client id, secret, and username and password set up from a Reddit account [here].

## How to use
Reddit Collection Viewer was created with a simple CLI which can be run with `python rcv.py`. First, users choose whether they would like to search through posts they've upvoted or those they've saved (or the default option of all submissions). Next, a list of all subreddits involved is displayed, ranked by the number of relevant posts from each. Users may either then filter by a term in the subreddit name or term in the post title. Once retrieved, users can then open all selected posts in a browser to quickly examine them. Users can exit an option at anytime by entering `q`.

## Tools
The main package used in this project was the Python Reddit API Wrapper ([PRAW]) to scrape data from Reddit; [pandas] was also used in organizing data.

## Future improvements
Users may also want to save all selected posts to csv file for later reference. This project is also open to any suggestions.


[//]: # (add hyperlinks)

   [here]: <https://www.reddit.com/prefs/apps>
   [PRAW]: <https://praw.readthedocs.io/en/latest/>
   [pandas]: <https://pandas.pydata.org/>