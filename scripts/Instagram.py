# Imports
import requests
import json
from six.moves.urllib.request import urlopen

class SearchInsta:
    def __init__(self, username) -> None:
        self.username = username
        self.lookup()
    
    def lookup(self):
        try:
            #self.lookup = requests.get(f"https://www.instagram.com/{self.username}/?__a=1").json()
            self.lookup = urlopen(f"https://www.instagram.com/{self.username}/?__a=1")
            self.lookup = "".join(map(chr, self.lookup.read()))
            self.lookup = json.loads(self.lookup)
            self.print_data()
        except Exception as e:
            print(f"Error: {e}. Unable to make a request to Instagram.")
    
    def print_data(self):
        print("\n Instagram Lookup Results: \n")
        print(f"Username: {self.lookup['graphql']['user']['username']}")
        print(f"Full Name: {self.lookup['graphql']['user']['full_name']}")
        print(f"Bio: {self.lookup['graphql']['user']['biography']}")
        print(f"Followers: {self.lookup['graphql']['user']['edge_followed_by']['count']}")
        print(f"Following: {self.lookup['graphql']['user']['edge_follow']['count']}")
        print(f"Business Account: {self.lookup['graphql']['user']['is_business_account']}")
        print(f"Business Category: {self.lookup['graphql']['user']['business_category_name']}")
        print(f"Private Account: {self.lookup['graphql']['user']['is_private']}")
        print(f"Verified Account: {self.lookup['graphql']['user']['is_verified']}")
        print(f"Profile Pic: {self.lookup['graphql']['user']['profile_pic_url_hd']}")
        print("\n Search Completed! \n")    

