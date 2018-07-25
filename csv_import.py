#file for importing csv file of all indian pincodes
#data downloaded from "https://data.gov.in/catalog/all-india-pincode-directory"
import csv
#sometimes there are more than one Post offices with same pincode (ex: 226021)
#so for saving them PO_list is used .
def csv_reader(pin_from_pic):
    PO_list = []
    # print("Reading CSV file")
    file1 = csv.reader(open("pincode.csv","r",encoding='latin-1'),delimiter=",")
    #i = 1
    found=0
    pincode1 = str(pin_from_pic)
    #accessing row wise data of the csv file
    for row in file1:
        if pincode1 == str(row[1]):
        	# print("Hellooo")
            found=1
            global district
            district = row[8]
            PO_list.append(row[0])
            global state
            state = row[9]
        	# print("for pincode ",number,", ", i,end="")
        	# print("th"," , Post Office name : " ,row[0],", District  is : ",row[8])
        	# i += 1
    # print(result1)
    if(found==1):
        list1 = [pincode1,district,PO_list,state]
        return(list1)
    else:
        list2 = [pincode1,"not found","not found","not found"]
        # print(list2)
        return(list2)

csv_reader("505004")