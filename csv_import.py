#file for importing csv file of all indian pincodes
#data downloaded from "https://data.gov.in/catalog/all-india-pincode-directory"
import csv
#sometimes there are more than one Post offices with same pincode (ex: 226021)
#so for saving them PO_list is used .
PO_list = []
def csv_reader(pin_from_pic):
    print("Reading CSV file")
    file1 = csv.reader(open("pincode.csv","r"),delimiter=",")
    #i = 1
    pincode = str(pin_from_pic)
    #accessing row wise data of the csv file
    for row in file1:
        if pincode == row[1]:
            global district
            district = row[8]
            PO_list.append(row[0])
            global state
            state = row[9]
            #print("for pincode ",number,", ", i,end="")
            #print("th"," , Post Office name : " ,row[0],", District  is : ",row[8])
            #i += 1
    #print(result1)
    list1 = [pincode,district,PO_list,state]
    return(list1)
    #print(pincode," ",district,"  ",PO_list , "  ", state)

#csv_reader("226021")