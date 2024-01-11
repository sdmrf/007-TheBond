# Imports
from googlesearch import search

class WebSearch:
        def __init__(self, query) -> None:
            self.query = query
            print("Searching...")
            self.search()
    
        def search(self):
            try:
                for i in search(self.query, tld="com", num=10, stop=10, pause=2):
                    print(i)
                print("\n Search Completed! \n")
            except Exception as e:
                print(f"Error: {e}. Unable to make a request to Google Search API.")
        
