import phonenumbers
from test import number

from phonenumbers import geocoder
# C - Country
# H- History

ch_number = phonenumbers.parse(number, "CH")
print("Your Country is : " + geocoder.description_for_number(ch_number, "en"))


# to see the service provider
# building function

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print("Your Service Provider is :  " + carrier.name_for_number(service_number, "en"))