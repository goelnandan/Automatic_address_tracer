#program for returning a list of pincodes available in the string passed from the given Picture
import re
def pin_finder(result1):
    #regex pattern for finding 6 digits pincode with any single character 
    #before or after it negligible (character like "," or "-" before or after pincodes) 
    h = re.findall(r"\D?(\d{6})\D?",result1)
    return h
#print(h)
