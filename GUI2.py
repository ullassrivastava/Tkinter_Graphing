from tkinter import *
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename


root = Tk()
root.title("Graph application")
root.geometry("640x640+0+0")

heading = Label(root, text="Graphing Software", font=("arial", 40, "bold"), fg="steelblue").pack()
label1 = Label(root, text="Choose a .csv file:", font=("arial", 18, "bold"), fg="black").place(x=10, y=200)

label2 = Label(root, text="Your graph has been generated in projects folder\n as myPlot.png", font=("arial", 18, "bold"), fg="black").place(x=10, y=300)
label2 = Label(root, text="How to use this:\n 1. Upload a .csv file with two headers\n 2. This app will generate the two line graphs\n Note: This app was used for learning Tkinter and drawing graphs ", font=("arial", 12, "bold"), fg="black").place(x=10, y=400)

#label2 = Label(root, text="Graphing:", font=("arial", 18, "bold"), fg="black").place(x=10, y=240)


text_trial = label1
#graph_label = Label(root, text="kkkk", font=("arial", 18, "bold"), fg="black").place(x=300, y=200)


name = StringVar()


def open_upload():
    filepath = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    print(filepath)

    filename = os.path.basename(filepath)
    data_file = pd.read_csv(filename)

    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            break
            # print(row)

    print(row)
    heading0 = row[0]
    heading1 = row[1]
    heading2 = row[2]

    print(row[0])
    print(row[1])
    print(row[2])

    distance1 = data_file[heading0]
    distance2 = data_file[heading1]

    plt.figure(1)
    plt.plot(distance1, 'r-')
    plt.plot(distance2, 'b-')

    plt.xlabel(heading0)
    plt.ylabel(heading1)
    plt.savefig('myPlot.png')


upload_button = Button(root, text="Upload and run", width=20, height=1, bg="Lightblue", command=open_upload).place(x=250, y=210)


root.mainloop()
