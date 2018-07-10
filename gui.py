#!/usr/bin/env python
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
import openpyxl
from PIL import ImageTk, Image
import os
# def Webcam():
# 	cap = cv2.VideoCapture(0)

# 	while(True):
# 		ret, frame = cap.read()
# 		frame = cv2.flip( frame, 1)

# 		cv2.imshow("Webcam (Click 'C' to capture)", frame)
# 		if cv2.waitKey(1) & 0xFF == ord('c'):
# 			out = cv2.imwrite('capture.jpg', frame)
# 			break

# 	cap.release()
# 	cv2.destroyAllWindows()
def check():
	print("Hello")

def givepath():
	root1 = tkinter.Tk()
	root1.withdraw()
	global dirname
	dirname = filedialog.askopenfilename()
	root1.destroy()

def window():
	global root
	root = Tk()
	root.resizable(False,False)
	# root.geometry('380x140+500+250')
	root.geometry("700x700")
	# # root.title('Automatic Address Tracer')
	# heading = Label(root,text="AUTOMATIC ADDRESS TRACER",font=("Courier", 15))
	# heading.grid(row=0,column=0,pady=4)
	# TEXT = """I tell you I have been in the editorial business going on fourteen
	# years, and it is the first time I ever heard of a man's having to know
	# anything in order to edit a newspaper. You turnip!"""
	# text = SimpleTextView(root, text=TEXT)
	# text.pack(fill=BOTH, expand=1)
	T = Text(root, height=1, width=25,font=("Courier", 15))
	T.pack()
	T.insert(END, "AUTOMATIC ADDRESS TRACER")

	T1 = Text(root, height=3, width=22,font=(7))
	T1.pack()
	T1.insert(END, '''The application traces postal pincode in the postal address and provides information regarding district/city/state.The user needs to upload image of postal address and click submit button.''')
	T1.pack(fill=X)
	instruct = Label(root, text="INSTRUCTIONS:",font=(7))
	instruct.pack()
	instruct1 = Label(root, text="INSTRUCTION 1:",font=(7))
	instruct1.pack(fill=X)
	instruct2 = Label(root, text="INSTRUCTION 2:",font=(7))
	instruct2.pack(fill=X)
	instruct3 = Label(root, text="INSTRUCTION 3:",font=(7))
	instruct3.pack(fill=X)

	pth = Button(root, text = "Select File", command=givepath)
	pth.pack(fill=X)
	sub = Button(root, text = "Submit", command=check)
	sub.pack(fill=X)
	# sub.grid(row=2, column=1, columnspan=3, sticky=W, pady=15)

	root.mainloop()

if __name__ == '__main__':
	window()