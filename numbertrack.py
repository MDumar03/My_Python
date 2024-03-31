
import phonenumbers
from phonenumbers import geocoder

number_1=phonenumbers.parse("+447826367522")
print(geocoder.description_for_number(number_1,"en"))
