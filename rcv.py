import praw
import pprint
import config
import pandas as pd
from collections import Counter
from datetime import datetime
import webbrowser

def main():
    reddit = praw.Reddit(client_id=config.CLIENT_ID,
                        client_secret=config.CLIENT_SECRET,
                        username=config.USERNAME,
                        password=config.PASSWORD,
                        user_agent='Reddit Collection Viewer v1.0')


    user = reddit.user.me()
    
    df = get_collection(user)

    response = 'continue'

    while response != 'q':
        response = input('Enter 1 to look at upvoted posts, 2 for saved, [3] for all: ')

        if response == 'q':
            break
        elif response == '1':
            subset = df[df['Type'] == 'Upvoted']
        elif response == '2':
            subset = df[df['Type'] == 'Saved']
        else: 
            subset = df

        subreddit_freqs = Counter(subset['Subreddit']).most_common()
    
        for entry in subreddit_freqs:
            print(entry[1], ' posts from ', entry[0])

        return_to_main = False
        
        while not return_to_main: 
            choice = input('Enter 1 to search posts, 2 to filter by subreddit, 3 to return: ')
            
            if choice == 'q':
                break
            elif choice == '1':
                display = search_posts(subset)
            elif choice == '2':
                display = filter_subreddits(subset)
            elif choice == '3':
                return_to_main = True
                break
            else:
                print('Please enter a valid option!')
                continue

            print(display.to_string())

            open_posts = input('Enter [1] to open selected posts in browser, 2 to skip: ')

            if open_posts == 'q':
                return_to_main = True
                break
            elif open_posts == '2':
                pass
            else:
                browser_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                browser = webbrowser.get(browser_path)
                display['Link'] = 'reddit.com' + display['URL'].astype(str)
                display['Link'].apply(browser.open_new_tab)


def search_posts(df):
    query = input('Enter search string: ')
    return df[df['Title'].str.contains(query, na=False, case=False)]

def filter_subreddits(df):
    sub = input('Enter desired subreddit: r/')
    return df[df['Subreddit'].str.contains(sub, na=False, case=False)]

def get_collection(redditor):
    likes_rows = [[utc_to_local(post.created_utc), post.subreddit.display_name, post.title, post.score, post.permalink, 'Upvoted'] for post in redditor.upvoted(limit=None)]
    df = pd.DataFrame(likes_rows, columns=['Time', 'Subreddit', 'Title', 'Score', 'URL', 'Type'])

    saved_posts = []

    for post in redditor.saved(limit=None):
        if isinstance(post, praw.models.Submission):
            saved_posts.append([utc_to_local(post.created_utc), post.subreddit.display_name, post.title, post.score, post.permalink, 'Saved'])
    
    saved_df = pd.DataFrame(saved_posts, columns=['Time', 'Subreddit', 'Title', 'Score', 'URL', 'Type'])
    df = df.append(saved_df, ignore_index=True)
    df.drop_duplicates(inplace=True)

    return df

def utc_to_local(utc_dt):
    return datetime.utcfromtimestamp(utc_dt).strftime('%Y-%m-%dT%H:%M:%SZ')


if __name__ == '__main__':
    main()
