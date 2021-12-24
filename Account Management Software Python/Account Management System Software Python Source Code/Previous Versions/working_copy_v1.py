#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 00:36:10 2018

@author: ziaulchoudhury
"""

import pymysql  


def inputValtoSQL(lis):
    # open connection to the database  
    conn = pymysql.connect(host='localhost',  
                           port=3306,  
                           user='root',  
                           passwd='',  
                           db='accountDB',  
                           charset='utf8')  
    cur = conn.cursor()  
    #Client Name & ID, State, Date, Income, Expense, Tax
    #INSERT INTO `accounts`.`food truck` (`client`, `state`, `date`, `income`) VALUES ('food truck', 'NY', '2018-03-27', '1900.0');
    #sql="INSERT INTO new_table VALUES ('123','y', '2019-2-2');"
#    lis = ['newTable','NY','2019-3-23','1','.09']
    sq = ("INSERT INTO " + (lis[0]) + " VALUES " + "(" + "'" + (lis[0]) + "','" + (lis[1]) +  "','" + (lis[2]) +  "','" + (lis[3]) +  "','" + (lis[4]) + "'" + ")")
    #sql =  "INSERT INTO food_truck VALUES ('food_truck','NY','2019-3-23','1','.09');"***
    #sql = "SELECT Date FROM food_truck WHERE STATE = 'NY'"  
    sql = sq
    cur.execute(sql)
    #rez = cur.fetchall()
    #
    #for el in rez:
    #    print(el)
    
    #tables
    tbl = "SHOW TABLES"
    cur.execute(tbl) 
    tables = cur.fetchall()
    for (table_name,) in tables:
           print(table_name)
    
    conn.commit()
    # close connection to the database  
    cur.close()  
    conn.close()





import tkinter as tk
from tkinter import messagebox
#import random

#Create root window
root = tk.Tk()

#Change root window background color
root.configure(bg="white")

#Change the title
root.title("Acounting Softwere")

#Change the window size
root.geometry("855x550+50+50")
topFrame = tk.Frame(root, width = 855, height = 50, bg = "#F3492A")
topFrame.pack(side=tk.TOP)

#left
leftSide = tk.Frame(root, width = 855, height = 500)
leftSide.pack(side=tk.LEFT)

#Create an empty list
tasks = []

#For testing purposes use a default list
tasks = ["Iteams"]

#Create functions
def update_listbox():
	#Clear the current list	
	clear_listbox()
	#Populate the listbox
	for task in tasks:
		lb_tasks.insert("end", task)

def clear_listbox():
	lb_tasks.delete(0, "end")
    
# saprate for each, togather doesn't work 
def clear_entry1():
    e1.delete(0, "end")
def clear_entry2():
    e2.delete(0, "end")
def clear_entry3():
    e3.delete(0, "end")
def clear_entry4():
    e4.delete(0, "end")
def clear_entry5():
    e5.delete(0, "end")
def clear_all_entries():
    e1.delete(0, "end")
    e2.delete(0, "end")
    e3.delete(0, "end")
    e4.delete(0, "end")
    e5.delete(0, "end")


def add_task():
    lis = []
    iteam1 = e1.get()
    iteam2 = e2.get()
    iteam3 = e3.get()
    iteam4 = e4.get()
    iteam5 = e5.get()
    
    if iteam1 !="":
        tasks.append(iteam1)
        lis.append(iteam1)
    if iteam2 !="":
        tasks.append(iteam2)
        lis.append(iteam2)
    if iteam3 !="":
        tasks.append(iteam3)
        lis.append(iteam3)
    if iteam4 !="":
        tasks.append(iteam4)
        lis.append(iteam4)
    if iteam5 !="":
        tasks.append(iteam5)
        lis.append(iteam5)
        update_listbox()
        inputValtoSQL(lis)
        print(lis)
        lis.clear()
    else:
        messagebox.showwarning("Warning", "You need to valid entery for all iteams.")
    e1.delete(0, "end")
    e2.delete(0, "end")
    e3.delete(0, "end")
    e4.delete(0, "end")
    e5.delete(0, "end")

		
def del_all():
	confirmed = messagebox.askyesno("Please Confirm", "Do you really want to delete all?")
	if confirmed == True:
		#Since we are changing the list, it needs to be global.
		global tasks
		#Clear the tasks list
		tasks = []
		#Update the listbox
		update_listbox()




#titles
lblInfo = tk.Label(topFrame, font=('times', 28, 'bold'), 
                   text="  (╯°□°）╯︵ ┻━┻ Account Management System ヘ(´°□°)ヘ┳━┳  ",
                   background = 'blue', foreground = 'white')
lblInfo.grid(column=0, row=0)

lbl_title = tk.Label(leftSide, text="Iteams", bg="white", foreground = '#FF7F00')
lbl_title.grid(row=0,column=0)

lbl_title2 = tk.Label(leftSide, text="Entry", bg="white", foreground = '#FF7F00')
lbl_title2.grid(row=0,column=1)

lbl_title3 = tk.Label(leftSide, text="History", bg="white", foreground = '#FF7F00')
lbl_title3.grid(row=0,column=3)

#labels
l1 = tk.Label(leftSide, text ="client_name_#: ", font=('times', 25, 'bold'), fg = "#046666")
l1.grid(row = 1, column = 0)

l2 = tk.Label(leftSide, text ="State(NY,NJ,CT): ", font=('times', 25, 'bold'), fg = "#046666")
l2.grid(row = 2, column = 0)

l3 = tk.Label(leftSide, text ="Date(YYYY-MM-DD): ", font=('times', 25, 'bold'), fg = "#046666")
l3.grid(row = 3, column = 0)

l4 = tk.Label(leftSide, text ="Income: ", font=('times', 25, 'bold'), fg = "#046666")
l4.grid(row = 4, column = 0)

l5 = tk.Label(leftSide, text ="Tax: ", font=('times', 25, 'bold'), fg = "#046666")
l5.grid(row = 5, column = 0)


#Entry Box

e1 = tk.Entry(leftSide, bg = "#D2F5F7")
e1.grid(row = 1, column = 1)

e2 = tk.Entry(leftSide, bg = "#D2F5F7")
e2.grid(row = 2, column = 1)

e3 = tk.Entry(leftSide, bg = "#D2F5F7")
e3.grid(row = 3, column = 1)

e4 = tk.Entry(leftSide, bg = "#D2F5F7")
e4.grid(row = 4, column = 1)

e5 = tk.Entry(leftSide, bg = "#D2F5F7")
e5.grid(row = 5, column = 1)

#list box
lb_tasks = tk.Listbox(leftSide, height = 12, width = 30)
lb_tasks.grid(row=1,column=3, rowspan=6)

#clear buttons
c1 = tk.Button(leftSide, text="Clear", font = ('times', 15, 'bold'), width = 10,
                highlightbackground = 'lightgray', foreground = 'red', command=clear_entry1)
c1.grid(row=1,column=2)

c2 = tk.Button(leftSide, text="Clear",font = ('times', 15, 'bold'), width = 10,
                highlightbackground = 'lightgray', foreground = 'red', command=clear_entry2)
c2.grid(row=2,column=2)

c3 = tk.Button(leftSide, text="Clear",font = ('times', 15, 'bold'), width = 10,
                highlightbackground = 'lightgray', foreground = 'red', command=clear_entry3)
c3.grid(row=3,column=2)

c4 = tk.Button(leftSide, text="Clear", font = ('times', 15, 'bold'), width = 10,
                highlightbackground = 'lightgray', foreground = 'red', command=clear_entry4)
c4.grid(row=4,column=2)

c5 = tk.Button(leftSide, text="Clear", font = ('times', 15, 'bold'), width = 10,
                highlightbackground = 'lightgray', foreground = 'red', command=clear_entry5)
c5.grid(row=5,column=2)


c_all = tk.Button(leftSide, text="CE",font = ('times', 31, 'bold'), width = 6,
                highlightbackground = 'lightgray', foreground = 'red', height=2, command=clear_all_entries)
c_all.grid(row=7,column=2)


#task and delete all button
btn_add_task = tk.Button(leftSide, text = 'Add Entry', font=('times', 31, 'bold'), width = 15,
                highlightbackground='lightgray', foreground = '#114ACE', height = 2, command=add_task)
btn_add_task.grid(row=7,column=0)

btn_del_all = tk.Button(leftSide, text = 'Delete All', font = ('times', 31, 'bold'), width = 17,
                highlightbackground = 'lightgray', foreground = 'red', height=2, command=del_all)
btn_del_all.grid(row=7,column=3)


#Start the main events loop
root.mainloop()