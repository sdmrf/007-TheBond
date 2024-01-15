# Imports
from email_validate import validate
import requests
import hashlib

class EmailLookup:
    def __init__(self, email) -> None:
        self.email = email
        self.lookup()
    
    def lookup(self):
        try:
            # Validate email
            self.emailValidate = validate(email_address=self.email, check_format=True, check_blacklist=True, check_dns=True, dns_timeout=10, check_smtp=False, smtp_debug=False)
            if self.emailValidate:
                haveIBeenPwned = input("You entered a valid email, would you like to check if your email has been pwned? [y/n]: ")
                if haveIBeenPwned.lower() == "y":
                    self.haveIBeenPwned()
                else:
                    pass
            else:
                print("Invalid email address.")

        except Exception as e:
            print(f"Error: {e}. Unable to make a request to Email Lookup. \n")
    
    def haveIBeenPwned(self):
        try:
            # Hash email
            hashed_email = hashlib.sha1(self.email.encode('utf-8')).hexdigest().upper()
            response = requests.get(f"https://api.pwnedpasswords.com/range/{hashed_email[:5]}").text

            if hashed_email[5:] in response:
                print(f"Your email has been pwned!")
                print(f"It has been pwned {response.split(hashed_email[5:])[1].split(':')[1].strip()[0]} times! \n")
            else:
                print("Your email has not been pwned! \n")

        except Exception as e:
            print(f"Error: {e}. Unable to make a request to Have I Been Pwned. \n")


