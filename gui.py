#!/usr/bin/env python
#authors :  Divya Prakash Yadav , Nandan Goel , Akhil Jain  (IET LUCKNOW )
#run this program
import extractor
import regex_import
import csv_import
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
import openpyxl
from PIL import ImageTk, Image
import os
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom


def check():
	#new underlined font
	# f = tkFont.Font(l, l.cget("font"))
	# f.configure(underline = True)
	#calling get_string function from extractor thereby passing the path of the pic to it
	result = extractor.get_string(dirname)

	#calling pin_finder in regex_import which will return list of pincodes in picture
	pincode = regex_import.pin_finder(result)[0]

	#calling csv_reader function from csv_import file
	#it will return (pincode,district,PO_list,state)
	address = csv_import.csv_reader(pincode)
	s1 = "Pin Code: "+(str(address[0]))
	s2 = "District: "+(str(address[1]))
	s3 = "Post Office(s): "+(str(address[2]))
	s4 = "State: "+(str(address[3]))
	print(address)
	# T3 = Text(root, height=1, width=8)
	# T3.pack()
	# T3.insert(END,"     ")
	gap1 = Label(root, text="              ")
	gap1.pack(fill=X,ipady=10,ipadx=3)
	result1= Label(root, text=s1,font=(7))
	result1.pack()
	gap1 = Label(root, text="              ")
	gap1.pack(fill=X,ipadx=3)
	result2= Label(root, text=s2,font=(7))
	result2.pack()
	gap1 = Label(root, text="              ")
	gap1.pack(fill=X,ipadx=3)
	result3= Label(root, text=s3,font=(7))
	result3.pack()
	gap1 = Label(root, text="              ")
	gap1.pack(fill=X,ipadx=3)
	result4= Label(root, text=s4,font=(7))
	result4.pack()


def givepath():
	root1 = Tk()
	root1.withdraw()
	global dirname
	dirname = filedialog.askopenfilename()
	print(dirname)
	root1.destroy()

def window():
	global root
	root = Tk()
	root.resizable(False,False)
	# root.geometry('380x140+500+250')
	root.geometry("1000x800")
	app = FullScreenApp(root)
	# # root.title('Automatic Address Tracer')
	# heading = Label(root,text="AUTOMATIC ADDRESS TRACER",font=("Courier", 15))
	# heading.grid(row=0,column=0,pady=4)
	# TEXT = """I tell you I have been in the editorial business going on fourteen
	# years, and it is the first time I ever heard of a man's having to know
	# anything in order to edit a newspaper. You turnip!"""
	# text = SimpleTextView(root, text=TEXT)
	# text.pack(fill=BOTH, expand=1)
	T = Text(root, height=1,width=25,font=("Courier", 15))
	T.pack()
	T.insert(END, "AUTOMATIC ADDRESS TRACER")
	# gap1 = Label(root, text="              ")
	# gap1.pack(fill=X,ipadx=3)
	T1 = Text(root, height=3, width=22,font=(7))
	T1.pack()
	T1.insert(END, '''The application traces postal pincode in the postal address and provides information regarding district/city/state.The user needs to upload image of postal address and click submit button.''')
	T1.pack(fill=X)
	instruct = Label(root, text="INSTRUCTIONS:",font=(7))
	instruct.pack(ipady=3)
	instruct1 = Label(root, text="INSTRUCTION 1:",font=(7))
	instruct1.pack(fill=X,ipady=3,ipadx=3)
	instruct2 = Label(root, text="INSTRUCTION 2:",font=(7))
	instruct2.pack(fill=X,ipady=3,ipadx=3)
	instruct3 = Label(root, text="INSTRUCTION 3:",font=(7))
	instruct3.pack(fill=X,ipady=3,ipadx=3)
	instruct3 = Label(root, text="              ",font=(7))
	instruct3.pack(fill=X,ipady=10,ipadx=3)

	pth = Button(root, text = "Select File", command=givepath)
	pth.pack(fill=X,ipady=3)
	sub = Button(root, text = "Submit", command=check)
	sub.pack(fill=X,ipady=3)
	# sub.grid(row=2, column=1, columnspan=3, sticky=W, pady=15)

	root.mainloop()

if __name__ == '__main__':
	window()