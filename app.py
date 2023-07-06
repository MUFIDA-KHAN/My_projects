# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 11:49:19 2023

@author: RUPESH
"""
import tkinter as tk
from tkinter import Label, Entry, Button
import joblib
import pandas as pd

# Load the model
dst1 = joblib.load('dst1.pkl')

def show_entry_fields():
    p1 = int(e1.get())
    p2 = int(e2.get())
    p3 = float(e3.get())
    p4 = int(e4.get())
    p5 = int(e5.get())

    input_data = [[p1, p2, p3, p4, p5]]

    result = segment_customers(input_data)
    Label(master, text=result).grid(row=7)

def segment_customers(input_data):
    prediction = dec1.predict(pd.DataFrame(input_data, columns=['Recency', 'Total Expenses', 'Income',
                                                                       'Total Acc Cmp', 'Total Purchases']))
    pred_1 = ''
    if prediction == 0:
        pred_1 = 'Cluster 0'
    elif prediction == 1:
        pred_1 = 'Cluster 1'
    elif prediction == 2:
        pred_1 = 'Cluster 2'
    elif prediction == 3:
        pred_1 = 'Cluster 3'
    return pred_1

master = tk.Tk()
master.title("Customer Segmentation Analysis")

label = Label(master, text='Customer Segmentation Analysis', bg='black', fg='white')
label.grid(row=0, columnspan=2)

Label(master, text="Recency").grid(row=1)
Label(master, text="Total Expenses").grid(row=2)
Label(master, text="Income").grid(row=3)
Label(master, text="Total Acc Cmp").grid(row=4)
Label(master, text="Total Purchases").grid(row=5)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)

Button(master, text='Submit', command=show_entry_fields).grid(row=6, columnspan=2)

master.mainloop()
if __name__ == '__main__':
    main()
