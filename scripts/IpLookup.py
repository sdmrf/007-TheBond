# Imports
import requests

class IpLookup:
    def __init__(self, ip) -> None:
        self.ip = ip
        self.lookup()
    
    def lookup(self):
        try:
            self.lookup = requests.get(f"http://ip-api.com/json/{self.ip}").json()
            self.print_data()
        except Exception as e:
            print(f"Error: {e}. Unable to make a request to Ip-API.")
    
    def print_data(self):
        print("\n Ip Lookup Results: \n")
        print(f"IP: {self.lookup['query']}")
        print(f"Status: {self.lookup['status']}")
        print(f"Country: {self.lookup['country']}")
        print(f"Country Code: {self.lookup['countryCode']}")
        print(f"Region: {self.lookup['region']}")
        print(f"Region Name: {self.lookup['regionName']}")
        print(f"City: {self.lookup['city']}")
        print(f"Zip Code: {self.lookup['zip']}")
        print(f"Time Zone: {self.lookup['timezone']}")
        print(f"Isp: {self.lookup['isp']}")
        print(f"Organization: {self.lookup['org']}")
        print(f"AS: {self.lookup['as']}")
        print("\n Search Completed! \n")