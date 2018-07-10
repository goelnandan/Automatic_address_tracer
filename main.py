#authors :  Divya Prakash Yadav , Nandan Goel , Akhil Jain  (IET LUCKNOW )
#run this program
import extractor
import regex_import
import csv_import

print('--- importing image for recognizing text ---')

#calling get_string function from extractor thereby passing the path of the pic to it
result = extractor.get_string("screenshots/3.png")

#calling pin_finder in regex_import which will return list of pincodes in picture
pincode = regex_import.pin_finder(result)[0]

#calling csv_reader function from csv_import file
#it will return (pincode,district,PO_list,state)
address = csv_import.csv_reader(pincode)

print(address[0]," ",address[1],"  ",address[2] , "  ",address[3])

print("------ Done -------")