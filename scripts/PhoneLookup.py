# Imports
import phonenumbers as Pn
from phonenumbers import geocoder, carrier, timezone

class Lookup:
    def __init__(self, phoneNo) -> None:
        self.phoneNo = phoneNo
        self.parse_phoneNo()

    # Function to parse the phone no.
    def parse_phoneNo(self):
        try:
            self.phoneNo = Pn.parse(self.phoneNo, None)
            self.validate_phoneNo()
        except Exception as e:
            print(f"Error: {e}. Unable to parse the phone no.")
    
    # Function to validate the phone no.
    def validate_phoneNo(self):
        try:
            self.valid = Pn.is_valid_number(self.phoneNo)
            self.get_carrier()
        except Exception as e:
            print(f"Error: {e}. Unable to validate the phone no.")
    
    # Function to get the carrier name.
    def get_carrier(self):
        try:
            carrier_info = carrier.name_for_number(self.phoneNo, "en")
            self.carrier = carrier_info if carrier_info else "Unknown"
            self.get_region()
        except Exception as e:
            print(f"Error: {e}. Unable to get the carrier name.")
    
    # Function to get the region.
    def get_region(self):
        try:
            self.region = geocoder.description_for_number(self.phoneNo, "en")
            self.get_timeZone()
        except Exception as e:
            print(f"Error: {e}. Unable to get the region.")
    
    # Function to get the time zone.
    def get_timeZone(self):
        try:
            self.timeZone = timezone.time_zones_for_number(self.phoneNo)
            self.print_data()
        except Exception as e:
            print(f"Error: {e}. Unable to get the time zone.")
    
    # Function to print the data.
    def print_data(self):
        print("\n Phone No. Lookup Results: \n")
        print(f"Phone No: {self.phoneNo}")
        print(f"Valid: {self.valid}")
        print(f"Carrier: {self.carrier}")
        print(f"Region: {self.region}")
        print(f"Time Zone: {self.timeZone}")
        print("\n Search Completed! \n")
