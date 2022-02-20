import phonenumbers
from phonenumbers import carrier, geocoder, timezone

# mobileNo = input("Enter Mobile Number with Country Code: ")
# mobileNo = phonenumbers.parse(mobileNo)

# #get timezone a phone number
# print("Timezone: ", timezone.time_zones_for_number(mobileNo))

# #get carrier of a phone number
# print("Carrier: ", carrier.name_for_number(mobileNo,"en"))

# #get region information
# print("Description: ", geocoder.description_for_number(mobileNo,"en"))

# #validating number
# print("Valid mobile number: ", phonenumbers.is_valid_number(mobileNo))

# #check possibility of a number
# print("Check possibility of a number: ", phonenumbers.is_possible_number(mobileNo))

def getDetails(mobileNo):
    mobileNo = phonenumbers.parse(mobileNo)
    tz = timezone.time_zones_for_number(mobileNo)
    car = carrier.name_for_number(mobileNo,"en")
    description = geocoder.description_for_number(mobileNo,"en")
    valid = phonenumbers.is_valid_number(mobileNo)
    possible = phonenumbers.is_possible_number(mobileNo)
    return tz, car, description, valid, possible