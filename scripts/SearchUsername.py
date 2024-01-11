# Imports
import requests

class SearchUsername:
    def __init__(self, username) -> None:
        self.username = username
        self.lookup()

    def lookup(self):
        try:
            self.lookup_instagram()
            self.lookup_twitter()
            self.lookup_facebook()
            self.lookup_youtube()
            self.lookup_snapchat()
            self.lookup_spotify()
            self.lookup_pinterest()
            self.lookup_reddit()
            self.lookup_tinder()
            self.lookup_github()
            self.lookup_linkedin()


        except Exception as e:
            print(f"Error: {e}. Unable to make a request to one or more platforms.")

    def lookup_instagram(self):
        try:
            instagram_url = f"https://www.instagram.com/{self.username}" 
            self.print_url(instagram_url, "Instagram")
        except Exception as e:
            print(f"Error: {e}. Unable to make a request to Instagram.")
    
    def lookup_twitter(self):
        try:
            twitter_url = f"https://www.x.com/{self.username}/"
            self.print_url(twitter_url, "Twitter")
        except Exception as e:
            print(f"Error: {e}. Unable to make a request to Twitter.")
    
    def lookup_facebook(self):
        try:
            facebook_url= f"https://www.facebook.com/{self.username}/"
            self.print_url(facebook_url, "Facebook")
        except Exception as e:
            print(f"Error: {e}. Unable to make a request to Facebook.")
    
    def lookup_youtube(self):
        try:
            youtube_url = f"https://www.youtube.com/{self.username}/"
            self.print_url(youtube_url, "Youtube")
        except Exception as e:
            print(f"Error: {e}. Unable to make a request to Youtube.")
    
    def lookup_snapchat(self):
        try:
            snapchat_url = f"https://story.snapchat.com/@{self.username}/"
            self.print_url(snapchat_url, "Snapchat")
        except Exception as e:
            print(f"Error: {e}. Unable to make a request to Snapchat.")

    def lookup_spotify(self):
        try:
            spotify_url = f"https://open.spotify.com/user/{self.username}/"
            self.print_url(spotify_url, "Spotify")
        except Exception as e:
            print(f"Error: {e}. Unable to make a request to Spotify.")  
    
    def lookup_pinterest(self):
        try:
            pinterest_url = f"https://www.pinterest.com/{self.username}/"
            self.print_url(pinterest_url, "Pinterest")
        except Exception as e:
            print(f"Error: {e}. Unable to make a request to Pinterest.")
    
    def lookup_reddit(self):
        try:
            reddit_url = f"https://www.reddit.com/{self.username}/"
            self.print_url(reddit_url, "Reddit")
        except Exception as e:
            print(f"Error: {e}. Unable to make a request to Reddit.")
    
    def lookup_tinder(self):
        try:
            tinder_url = f"https://www.tinder.com/@{self.username}/"
            self.print_url(tinder_url, "Tinder")
        except Exception as e:
            print(f"Error: {e}. Unable to make a request to Tinder.")
    
    
    def lookup_github(self):
        try:
            github_url = f"https://www.github.com/{self.username}/"
            self.print_url(github_url, "Github")
        except Exception as e:
            print(f"Error: {e}. Unable to make a request to Github.")
    
    def lookup_linkedin(self):
        try:
            linkedin_url = f"https://www.linkedin.com/{self.username}/"
            self.print_url(linkedin_url, "Linkedin")
        except Exception as e:
            print(f"Error: {e}. Unable to make a request to Linkedin.")

    def print_url(self, url, platform):
                print(f"Link for {platform}: {url}")
