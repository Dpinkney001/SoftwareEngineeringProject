#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 00:36:10 2018

@author: ziaulchoudhury
ziaul999@gmail.com

This is a account management softwere which gives ghariphical interface
for ueser inputs and saves the inputs dynamically in MySql database.

"""

import pymysql, time
import warnings  
import tkinter as tk
from tkinter import messagebox
#import random


#-------------# SQL part #-------------#
# Connect to accountDB database
def ConnectToSQL():
    # open connection to the database  
    conn = pymysql.connect(host='localhost',  
                           port=3306,  
                           user='root',  
                           passwd='',  
                           db='accountDB',  
                           charset='utf8')  
    cur = conn.cursor()  
    return(conn,cur)

# for getting all the tables in DB
def TableListInDB():
    tables_list:str = []
    conn, cur = (ConnectToSQL())
        
    tbl = "SHOW TABLES"
    cur.execute(tbl) 
    tables = cur.fetchall()
    for table_name in tables:
        tables_list.append(table_name)
        
    tables_list = map(list,tables_list)
    flat_list = [item for sublist in tables_list for item in sublist]

    # print(flat_list)
    # close connection to the database  
    cur.close()  
    conn.close()
    
    return(flat_list)

# Input values or create values dynamically
def inputValtoSQL(lis):
    # open connection to the database  
    conn, cur = ConnectToSQL()
    #calliing the to get the table list 
    tables_in_DB = TableListInDB() 
    matches = set(lis).intersection(set(tables_in_DB))
    print(matches)
    print(len(matches))
    
    try:
        # if the table exist in DB insert the values else create new table
        if len(matches) != 0:
            sql = ("INSERT INTO " + (lis[0]) + " VALUES " + "(" + "'" + (lis[0]) +
                                    "','" + (lis[1]) +  "','" + (lis[2]) +  "','" +
                                    (lis[3]) + "','" + (lis[4]) + "','" + (lis[5])+ "',''" + ")")
            #sql =  "INSERT INTO food_truck VALUES ('food_truck','NY','2019-3-23','1','.09');"#test
            #sql = "SELECT Date FROM food_truck WHERE STATE = 'NY'" 
            warnings.filterwarnings("ignore") # ignore warning since id is auto incemented by mysql
            cur.execute(sql)
        else:
            sql2 = ("CREATE TABLE IF NOT EXISTS " + (lis[0]) +
                  " (client VARCHAR(45) NOT NULL, state VARCHAR(45) NOT NULL,"+
                  " date DATE NOT NULL, income FLOAT NOT NULL, expense FLOAT NOT NULL,"+
                  " tax FLOAT NOT NULL, id INT NOT NULL AUTO_INCREMENT, PRIMARY KEY (id));")
            cur.execute(sql2)
            sql2 = ("INSERT INTO " + (lis[0]) + " VALUES " + "(" + "'" + (lis[0]) +
                                     "','" + (lis[1]) +  "','" + (lis[2]) +  "','" +
                                     (lis[3]) +  "','" + (lis[4]) + "','" + (lis[5])+ "',''" + ")")
            warnings.filterwarnings("ignore") # ignore warning since id is auto incemented by mysql
            cur.execute(sql2)
            messagebox.showwarning("Info","New table added to the database!!")
    except:
            messagebox.showwarning("ERROR!!","Invalid inputs or SYNTEX ERROR!!")

    # commit changes and close connection to the database     
    conn.commit() 
    cur.close()  
    conn.close()






#-------------# GUI part #-------------#
def tick(time1=''):
    # get the current local time from the PC
    time2 = time.strftime(' %A \n %Y-%m-%d \n %I:%M:%S %p')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock_lbl.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    clock_lbl.after(200, tick)


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
def clear_entry6():
    e6.delete(0, "end")
def clear_all_entries():
    e1.delete(0, "end")
    e2.delete(0, "end")
    e3.delete(0, "end")
    e4.delete(0, "end")
    e5.delete(0, "end")
    e6.delete(0, "end")


def add_task():
    lis = []
    iteam1 = e1.get()
    iteam2 = e2.get()
    iteam3 = e3.get()
    iteam4 = e4.get()
    iteam5 = e5.get()
    iteam6 = e6.get()
    
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
        try:
            tasks.append(iteam4)
            iteam4 = float(iteam4)
            lis.append(str(iteam4))
        except:
            messagebox.showwarning("⚠⚠⚠ Warning!! ⚠⚠⚠\n", 
                                   "You need to enter valid entery for all iteams.\n\t\t\t\t☠⚠☠")
            clear_entry4()
    if iteam5 !="": 
        try:
            tasks.append(iteam5)
            iteam5 = float(iteam5)
            lis.append(str(iteam5))
        except:
            messagebox.showwarning("⚠⚠⚠ Warning!! ⚠⚠⚠\n", 
                                   "You need to enter valid entery for all iteams.\n\t\t\t\t☠⚠☠")
            clear_entry5()
    if iteam6 !="":
        try:
            tasks.append(iteam6)
            iteam6 = float(iteam6)
            lis.append(str(iteam6))
            update_listbox()
            inputValtoSQL(lis)
            print(lis)
            lis.clear()
        except:
            messagebox.showwarning("⚠⚠⚠ Warning!! ⚠⚠⚠\n", 
                                   "You need to enter valid entery for all iteams.\n\t\t\t\t☠⚠☠")
    else:
        messagebox.showwarning("⚠⚠⚠ Warning!! ⚠⚠⚠\n", 
                               "You need to enter valid entery for all iteams.\n\t\t\t\t☠⚠☠")
    e1.delete(0, "end")
    e2.delete(0, "end")
    e3.delete(0, "end")
    e4.delete(0, "end")
    e5.delete(0, "end")
    e6.delete(0, "end")

		
def del_all():
	confirmed = messagebox.askyesno("Please Confirm", "Do you really want to delete all?")
	if confirmed == True:
		#Since we are changing the list, it needs to be global.
		global tasks
		#Clear the tasks list
		tasks = []
		#Update the listbox
		update_listbox()


#Create root window
root = tk.Tk()

#Change root window background color
root.configure(bg="#00FF7F")

#Change the title
root.title("Acounting Softwere")

#Change the window size
root.geometry("855x550+275+150")
topFrame = tk.Frame(root, width = 855, height = 50, bg = "#F3492A")
topFrame.pack(side=tk.TOP)

#left
leftSide = tk.Frame(root, width = 855, height = 500)
leftSide.pack(side=tk.LEFT)
leftSide.configure(bg="#00FF7F")
#Create an empty list
tasks = []

#For testing purposes use a default list
tasks = ["Iteams added to DB:"]

#titles
lblInfo = tk.Label(topFrame, font=('times', 28, 'bold'), 
                   text="  (╯°□°）╯︵ ┻━┻ Account Management System ヘ(´°□°)ヘ┳━┳  ",
                   background = 'blue', foreground = 'white')
lblInfo.grid(column=0, row=0)

lbl_title = tk.Label(leftSide, text="Iteams⤵", font=('times', 35, 'bold'),
                     bg="#00FF7F", foreground = '#773420')
lbl_title.grid(row=0,column=0)

lbl_title2 = tk.Label(leftSide, text="Entry⤵", font=('times', 35, 'bold'),
                     bg="#00FF7F", foreground = '#773420')
lbl_title2.grid(row=0,column=1)

lbl_title3 = tk.Label(leftSide, text="CE⤵", font=('times', 35, 'bold'),
                     bg="#00FF7F", foreground = '#773420')
lbl_title3.grid(row=0,column=2)

lbl_title4 = tk.Label(leftSide, text="History⤵", font=('times', 35, 'bold'),
                     bg="#00FF7F", foreground = '#773420')
lbl_title4.grid(row=0,column=3)

#labels
l1 = tk.Label(leftSide, text ="client_name_#: ", font=('times', 25, 'bold'), 
              bg = "#00FF7F", fg = "#046666")
l1.grid(row = 1, column = 0)

l2 = tk.Label(leftSide, text ="State(NY, NJ, CT): ", font=('times', 25, 'bold'), 
              bg = "#00FF7F", fg = "#046666")
l2.grid(row = 2, column = 0)

l3 = tk.Label(leftSide, text ="Date(YYYY-MM-DD): ", font=('times', 25, 'bold'), 
              bg = "#00FF7F", fg = "#046666")
l3.grid(row = 3, column = 0)

l4 = tk.Label(leftSide, text ="Income: ", font=('times', 25, 'bold'), 
              bg = "#00FF7F", fg = "#046666")
l4.grid(row = 4, column = 0)

l5 = tk.Label(leftSide, text ="Expense: ", font=('times', 25, 'bold'), 
              bg = "#00FF7F", fg = "#046666")
l5.grid(row = 5, column = 0)

l6 = tk.Label(leftSide, text ="Tax: ", font=('times', 25, 'bold'), 
              bg = "#00FF7F", fg = "#046666")
l6.grid(row = 6, column = 0)


#Entry Box

e1 = tk.Entry(leftSide, font = ('times', 18, 'bold'), bg = "#D2F5F7")
e1.grid(row = 1, column = 1)

e2 = tk.Entry(leftSide, font = ('times', 18, 'bold'), bg = "#D2F5F7")
e2.grid(row = 2, column = 1)

e3 = tk.Entry(leftSide, font = ('times', 18, 'bold'), bg = "#D2F5F7")
e3.grid(row = 3, column = 1)

e4 = tk.Entry(leftSide, font = ('times', 18, 'bold'), bg = "#D2F5F7")
e4.grid(row = 4, column = 1)

e5 = tk.Entry(leftSide, font = ('times', 18, 'bold'), bg = "#D2F5F7")
e5.grid(row = 5, column = 1)

e6 = tk.Entry(leftSide, font = ('times', 18, 'bold'), bg = "#D2F5F7")
e6.grid(row = 6, column = 1)

#list box
lb_tasks = tk.Listbox(leftSide, font = ('times', 18, 'bold'), height = 12, width = 30, 
              bg = "yellow", fg = "#046666")
lb_tasks.grid(row=1,column=3, rowspan=6, padx=5, pady=5)

#clear buttons
cb1 = tk.Button(leftSide, text="Clear", font = ('times', 15, 'bold'), width = 10, height = 2,
                highlightbackground = 'lightgray', foreground = 'red', command=clear_entry1)
cb1.grid(row=1,column=2)

cb2 = tk.Button(leftSide, text="Clear",font = ('times', 15, 'bold'), width = 10, height = 2,
                highlightbackground = 'lightgray', foreground = 'red', command=clear_entry2)
cb2.grid(row=2,column=2)

cb3 = tk.Button(leftSide, text="Clear",font = ('times', 15, 'bold'), width = 10, height = 2,
                highlightbackground = 'lightgray', foreground = 'red', command=clear_entry3)
cb3.grid(row=3,column=2)

cb4 = tk.Button(leftSide, text="Clear", font = ('times', 15, 'bold'), width = 10, height = 2,
                highlightbackground = 'lightgray', foreground = 'red', command=clear_entry4)
cb4.grid(row=4,column=2)

cb5 = tk.Button(leftSide, text="Clear", font = ('times', 15, 'bold'), width = 10, height = 2,
                highlightbackground = 'lightgray', foreground = 'red', command=clear_entry5)
cb5.grid(row=5,column=2)

cb6 = tk.Button(leftSide, text="Clear", font = ('times', 15, 'bold'), width = 10, height = 2,
                highlightbackground = 'lightgray', foreground = 'red', command=clear_entry5)
cb6.grid(row=6,column=2)

# clear all, task, and delete all buttons
clear_all = tk.Button(leftSide, text=" ✗\nClear\nall\n Entries ",font = ('times', 30, 'bold'), width = 7,
                highlightbackground = 'lightgray', foreground = 'red', height=4,
                command=clear_all_entries)
clear_all.grid(row=7,column=2)

btn_add_task = tk.Button(leftSide, text = 'Add Entry', font=('times', 31, 'bold'), width = 17,
                highlightbackground='lightgray', foreground = '#114ACE', height = 4, command=add_task)
btn_add_task.grid(row=7,column=0)

btn_del_all = tk.Button(leftSide, text = 'Delete All', font = ('times', 31, 'bold'), width = 17,
                highlightbackground = 'lightgray', foreground = 'red', height=4, command=del_all)
btn_del_all.grid(row=7,column=3)

# clock
clock_lbl = tk.Label(leftSide, text = "", font=('times', 25, 'bold'), width = 14, fg = "#046666",
                 bg = 'lightgray', height = 5)
clock_lbl.grid(row = 7, column = 1)
tick()

#Start the main events loop
root.mainloop()