import sys
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from PIL import ImageTk, Image
from age_estimator import age_estimator

#make frame
root = Tk()
root.geometry("600x400")
window = Toplevel()

def estimateAge():
	ages = age_estimator(filename)
	messagebox.showinfo( "Age Estimator", ages)


def loadFile():
   global filename
   filename = askopenfilename()
   showImage()

def showImage():
	my_image = Image.open(filename)
	hpercent = (300 / float(my_image.size[1]))
	wsize = int((float(my_image.size[0]) * float(hpercent)))
	my_image = my_image.resize((wsize, 300), Image.ANTIALIAS)
	my_image = ImageTk.PhotoImage(my_image)
	canvas.create_image(250, 150, anchor=CENTER, image=my_image)
	canvas.my_image = my_image

top_frame = Frame(root)
bottom_frame = Frame(root)

top_frame.pack()
bottom_frame.pack()

#headline
headline = Label(top_frame, text="Age Estimator App", bg='blue', fg='white')
headline.config(font=('Courier', 27))
headline.grid(padx=10, pady=10)

#loadfile_button
load_button = Button(bottom_frame, text="Load Image", bg='blue', fg='white', command=loadFile)
load_button.config(height = 2, width = 15)
load_button.grid(sticky = S)

#enter_button
detect_button = Button(bottom_frame, text="Go", bg='blue', fg='white', command=estimateAge)
detect_button.config(height = 2, width = 15)
detect_button.grid(sticky = S)

#quit_button
quit_button = Button(bottom_frame, text="Quit", bg="blue", fg="white", command=quit)
quit_button.config(height = 2, width = 15)
quit_button.grid(sticky = S)

canvas = Canvas(window, width = 500, height = 500)
canvas.pack()

fcanvas = Canvas(window, width = 50, height = 50)
fcanvas.pack()

root.mainloop()
