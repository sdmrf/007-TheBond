# Imports
from email_validate import validate

class EmailLookup:
    def __init__(self, email) -> None:
        self.email = email
        self.lookup()
    
    def lookup(self):
        try:
            self.emailValidate = validate(email_address= self.email, check_format=True, check_blacklist=True, check_dns=True,dns_timeout=10, check_smtp=False, smtp_debug=False)
            print(self.emailValidate)
        except Exception as e:
            print(f"Error: {e}. Unable to make a request to Email Lookup.")
    

