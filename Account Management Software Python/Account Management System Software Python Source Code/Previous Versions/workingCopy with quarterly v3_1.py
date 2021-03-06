#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 00:36:10 2018

@author: ziaulchoudhury
ziaul999@gmail.com

This is a account management softwere which gives ghariphical interface
for ueser inputs and saves the inputs dynamically in MySql database.

"""

import pymysql,time,warnings,datetime,json 
import tkinter as tk
from tkinter import messagebox

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
                  " t_date DATE NOT NULL, income FLOAT NOT NULL, expense FLOAT NOT NULL,"+
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

#-------------# TAX part #-------------#
'''
NY/BOSTON
Q1 (March - May) Collection -> June 20, 2018
Q2 (June - August)	Collection -> September 20, 2018
Q3 (September - November) Collection -> December 20, 2018
Q4 (December - February) Collection -> March 20, 2019

NJ
Q1 (Jan-March) Collection -> April 20, 2018
Q2 (April-June) Collection -> July 20, 2018
Q3 (July-Sept) Collection -> October 22, 2018*
Q4 (Oct-Dec) Collection -> January 22, 2019*

IL/CHICAGO
Q1 (Jan-March) -> April 20, 2018
Q2 (April-June) -> July 20, 2018
Q3 (July-Sept) -> October 22, 2018*
Q4 (Oct-Dec) -> January 22, 2019*

CT
Q1 January 1 - March 31 -> May 1
Q2 April 1 - June 30 -> July 31 
Q3 July 1 - September 30 -> October 31
Q4 October 1 - December 31 -> January 31
'''
#fetch the data from MyQSL
def get_ny_qS(table,a,b,p):
    sql1 = max_iteams("SELECT client FROM "+table+" WHERE (t_date BETWEEN '"+a+"' AND '"+b+"');")
    sql2 = max_iteams("SELECT state FROM "+table+" WHERE (t_date BETWEEN '"+a+"' AND '"+b+"');")
    sql3 = max_iteams("SELECT t_date FROM "+table+" WHERE (t_date BETWEEN '"+a+"' AND '"+b+"');")
    sql4 = max_iteams("SELECT income FROM "+table+" WHERE (t_date BETWEEN '"+a+"' AND '"+b+"');")
    sql5 = max_iteams("SELECT tax FROM "+table+" WHERE (t_date BETWEEN '"+a+"' AND '"+b+"');")
    sql6 = max_iteams("SELECT id FROM "+table+" WHERE (t_date BETWEEN '"+a+"' AND '"+b+"');")
    return a,b,sql1,sql2,sql3,sql4,sql5,sql6,p

#find tax for NY and Boston    
def find_unpaid_underpaid_overpaid_taxes_ny(table,ny_s_p,ny_e_p,ny_payment):
    a,b,client,state,t_date,income,tax,t_id,p = get_ny_qS(table,ny_s_p,ny_e_p,ny_payment)
    t_date = flat_date(t_date)
    NY = 0.08875
    Boston = 0.0625
    begnning = "<!DOCTYPE html><html><head><meta charset='UTF-8'><title>Quarterly Tax REPORT</title>"
    style = "<style> table, th, td {border: 1px solid black;border-collapse: collapse;padding: 15px;text-align: left;background-color: #bdedc0;}</style>"
    hearder = "</head><body><h1>"+ str(table) +"Quarterly Tax Report</h1>"
    lastPart = "</body> </html>"
    strTable = "<table><tr><th>Client</th><th>State</th><th>Date</th><th>Income</th><th>Expense</th><th>ID</th><th>Tax Owe</th></tr>"
    income_list = []
    tax_list = []
    tax_owe = []
    for client_,state_,t_date_,income_,tax_,t_id_ in zip(client,state,t_date,income,tax,t_id):
        t1 = 0.0
        t2 = 0.0
        t3 = 0.0
        if state_ == "NY":
            t1 = float(income_)
            t2 = float(tax_)
            t3 = float(NY)
            total = (t1+t2) - (t1+(t1*t3))
            income_list.append(t1)
            tax_list.append(t2)
            tax_owe.append(total)
            strRW = ("<tr><td>"+str(client_)+ "</td><td>"+str(state_)+"</td><td>"+str(t_date_)+ 
                     "</td><td>"+str(income_)+"</td><td>"+str(tax_)+"</td><td>"+str(t_id_)+
                     "</td><td>"+str(total)+"</td></tr>")
            strTable = strTable+strRW
        elif state_ == "BOSTON":
            t1 = float(income_)
            t2 = float(tax_)
            t3 = float(Boston)
            total = (t1+t2) - (t1+(t1*t3))
            income_list.append(t1)
            tax_list.append(t2)
            tax_owe.append(total)
            strRW = ("<tr><td>"+str(client_)+ "</td><td>"+str(state_)+"</td><td>"+str(t_date_)+ 
                     "</td><td>"+str(income_)+"</td><td>"+str(tax_)+"</td><td>"+str(t_id_)+
                     "</td><td>"+str(total)+"</td></tr>")
            strTable = strTable+strRW
    
    strTable = (begnning + style + hearder + strTable +"</table>"+"<h2>"+" Tax period "+a+" to "+b+"<br>Payment date: "+ p
                +"</h2>"+"<h3> Total: " +str(sum(income_list)) +"<br> Total tax: " 
                +str(sum(tax_list)) +"<br>Tax owe: " + str(sum(tax_owe)) + "</h3>"+ lastPart)
     
    Html_file= open(table+" Tax period "+a+" to "+b+" NY Payment Date "+p+".html","w")
    Html_file.write(strTable)
    Html_file.close()    
    

def find_unpaid_underpaid_overpaid_taxes(table,state2,tax_rate,ny_s_p,ny_e_p,ny_payment):
    a,b,client,state,t_date,income,tax,t_id,p = get_ny_qS(table,ny_s_p,ny_e_p,ny_payment)
    t_date = flat_date(t_date)
    begnning = "<!DOCTYPE html><html><head><meta charset='UTF-8'><title>Quarterly Tax REPORT</title>"
    style = "<style> table, th, td {border: 1px solid black;border-collapse: collapse;padding: 15px;text-align: left;background-color: #bdedc0;}</style>"
    hearder = "</head><body><h1>"+ str(table) +"Quarterly Tax Report</h1>"
    lastPart = "</body> </html>"
    strTable = "<table><tr><th>Client</th><th>State</th><th>Date</th><th>Income</th><th>Expense</th><th>ID</th><th>Tax Owe</th></tr>"
    income_list = []
    tax_list = []
    tax_owe = []
    for client_,state_,t_date_,income_,tax_,t_id_ in zip(client,state,t_date,income,tax,t_id):
        t1 = 0.0
        t2 = 0.0
        t3 = 0.0
        if state_ == state2:
            t1 = float(income_)
            t2 = float(tax_)
            t3 = float(tax_rate)
            total = (t1+t2) - (t1+(t1*t3))
            income_list.append(t1)
            tax_list.append(t2)
            tax_owe.append(total)
            strRW = ("<tr><td>"+str(client_)+ "</td><td>"+str(state_)+"</td><td>"+str(t_date_)+ 
                     "</td><td>"+str(income_)+"</td><td>"+str(tax_)+"</td><td>"+str(t_id_)+
                     "</td><td>"+str(total)+"</td></tr>")
            strTable = strTable+strRW

    
    strTable = (begnning + style + hearder + strTable +"</table>"+"<h2>"+" Tax period "+a+" to "+b+"<br>Payment date: "+ p
                +"</h2>"+"<h3> Total: " +str(sum(income_list)) +"<br> Total tax: " 
                +str(sum(tax_list)) +"<br>Tax owe: " + str(sum(tax_owe)) + "</h3>"+lastPart)
     
    Html_file= open(table+" Tax period "+a+" to "+b+" "+ str(state2) +" Payment Date "+p+".html","w")
    Html_file.write(strTable)
    Html_file.close()    


def generate_ny(table,ny_s_p,ny_e_p,ny_payment):   
    for (a, b, c) in zip(ny_s_p,ny_e_p,ny_payment):
        find_unpaid_underpaid_overpaid_taxes_ny(table,a,b,c)
        
def generate_other(table,state,ny_s_p,ny_e_p,ny_payment): 
    NJ = 0.06625
    CT = 0.0635
    Chicago = 0.1025
    if state == "NJ":
        for (a, b, c) in zip(ny_s_p,ny_e_p,ny_payment):
            find_unpaid_underpaid_overpaid_taxes(table,state,NJ,a,b,c)
    if state == "CT":
        for (a, b, c) in zip(ny_s_p,ny_e_p,ny_payment):
            find_unpaid_underpaid_overpaid_taxes(table,state,CT,a,b,c)
    if state == "CHICAGO":
        for (a, b, c) in zip(ny_s_p,ny_e_p,ny_payment):
            find_unpaid_underpaid_overpaid_taxes(table,state,Chicago,a,b,c)


#-------------# HTML part #-------------#
#MySQL test code
#SELECT * FROM accountDB.master_table;
#SELECT DATE_SUB(DATE_SUB(CURDATE(),INTERVAL (DAY(CURDATE())-1) DAY), INTERVAL 1 MONTH);
#SELECT DATE_SUB(CURDATE(),INTERVAL (DAY(CURDATE())) DAY);
#SELECT * FROM accountDB.master_table
#WHERE (t_date BETWEEN '2017-01-01 00:00:00' AND '2017-01-31 00:00:00');
#SELECT * FROM accountDB.master_table
#WHERE (t_date BETWEEN DATE_SUB(DATE_SUB(CURDATE(),INTERVAL (DAY(CURDATE())-1) DAY), INTERVAL 1 MONTH) AND DATE_SUB(CURDATE(),INTERVAL (DAY(CURDATE())) DAY))

def max_iteams(tbl):
    try:
        conn, cur = (ConnectToSQL())
        
        item_id:str = []
        cur.execute(tbl) 
        tables = cur.fetchall()
        for table_name in tables:
            item_id.append(table_name)
            
        item_id = map(list,item_id)
        item_id_flat_list = [item for sublist in item_id for item in sublist]
        
        cur.close()  
        conn.close()
        return item_id_flat_list 
    except:
        print("max_iteams(tbl) error")

def validate_if_date_exists(sql, t):
    dates = max_iteams(sql)
    d = []   
    for x in dates:
        d.append(str(x))
        
    months = []
    years = []
    
    if t == "m":
        for m in d:
            m = m[:-3]
            months.append(m)
            
        m = ([datetime.datetime.today().strftime('%Y-%m')])
        matches = list(set(months).intersection(set(m)))
        return len(matches)
    else:   
        for y in d:
            y = y[:-6]
            years.append(y)
        years = [set(years)]
        return len(years)

def flat_date(dates):
    t_date_flat_list = []
    for date in dates:
        date = str(date)
        t_date_flat_list.append(date)
    return t_date_flat_list

def html_pie_chart(table,inc,expns,tx):
    inc = sum(inc)
    expns = sum(expns)
    tax = sum(tx)
    
    pie_chart = ("<div id='piechart'></div><script type='text/javascript' src='https:"+
    "//www.gstatic.com/charts/loader.js'></script><script type='text/javascript'>"
    +"google.charts.load('current', {'packages':['corechart']});google.charts.set"+
    "OnLoadCallback(drawChart);function drawChart() {  var data = google.visualization."
    +"arrayToDataTable([['Type', 'Percentage'],['Income: "+str(inc)+"', "+str(inc)+
    "],['Expense: "+str(expns)+"',"+str(expns)+"],['Tax: "+str(tax)+"', "+str(tax)+
    "]]);var options = {'title':"+"'table'"+", 'width':600, 'height':400};var chart ="
    +" new google.visualization.PieChart(document.getElementById('piechart'));"
    +"chart.draw(data, options);}</script>")
    
    return pie_chart
def html_bar_chart(dte,incm,expns,tx):
    line_chart_top = ("<script type='text/javascript' src='https://www.gstatic.com/charts/loader.js'>"+
    "</script><script type='text/javascript'>google.charts.load('current', {'packages'"+
    ":['corechart']});google.charts.setOnLoadCallback(drawChart);function drawChart()"+
    " {var data = google.visualization.arrayToDataTable([['Date', 'Net Income/growth'],")
    
    line_chart_middle = ""
    for (a, b, c, d) in zip(dte, incm, expns, tx):      
        net_income = b - (c+d)
        net_income = int(round(net_income))
        strRW = "['"+str(a)+"' ,"+ str(net_income) + "],"
        line_chart_middle = line_chart_middle+strRW    
    line_chart_middle = line_chart_middle[:-1]
         
    line_chart_buttom =(" ]); var options = { title: 'Company Performance',curveType: 'function',"+
    "legend: { position: 'bottom' }};var chart = new google.visualization.LineChart(document."+
    "getElementById('curve_chart'));chart.draw(data, options);}</script>")

    line_chart = line_chart_top + line_chart_middle + line_chart_buttom
    return line_chart
    
####Monthly####
def monthly_HTML_data(table):
    
    #--------------------------------iteam_id--------------------------------    
    sql1 = ("SELECT id FROM "+table+" WHERE (t_date BETWEEN DATE_SUB(DATE_SUB(CURDATE()"+
        ",INTERVAL (DAY(CURDATE())-1) DAY), INTERVAL 1 MONTH) AND DATE_SUB(CURDATE(),"+
        "INTERVAL (DAY(CURDATE())) DAY));")
    item_id_flat_list = max_iteams(sql1)

    #--------------------------------client--------------------------------    

    sql2 = ("SELECT client FROM "+table+" WHERE (t_date BETWEEN DATE_SUB(DATE_SUB(CURDATE()"+
        ",INTERVAL (DAY(CURDATE())-1) DAY), INTERVAL 1 MONTH) AND DATE_SUB(CURDATE(),"+
        "INTERVAL (DAY(CURDATE())) DAY));")
    client_flat_list = max_iteams(sql2)

    #--------------------------------state--------------------------------    
    sql3 = ("SELECT state FROM "+table+" WHERE (t_date BETWEEN DATE_SUB(DATE_SUB(CURDATE()"+
        ",INTERVAL (DAY(CURDATE())-1) DAY), INTERVAL 1 MONTH) AND DATE_SUB(CURDATE(),"+
        "INTERVAL (DAY(CURDATE())) DAY));")

    state_flat_list = max_iteams(sql3)

    #--------------------------------date--------------------------------    
    sql4 = ("SELECT t_date FROM "+table+" WHERE (t_date BETWEEN DATE_SUB(DATE_SUB(CURDATE()"+
        ",INTERVAL (DAY(CURDATE())-1) DAY), INTERVAL 1 MONTH) AND DATE_SUB(CURDATE(),"+
        "INTERVAL (DAY(CURDATE())) DAY));")

    temp_t_date_flat_list = max_iteams(sql4)
    month = temp_t_date_flat_list[0].strftime('%B %Y')
    t_date_flat_list = flat_date(temp_t_date_flat_list)
        
    #--------------------------------income--------------------------------    
    sql5 = ("SELECT income FROM "+table+" WHERE (t_date BETWEEN DATE_SUB(DATE_SUB(CURDATE()"+
        ",INTERVAL (DAY(CURDATE())-1) DAY), INTERVAL 1 MONTH) AND DATE_SUB(CURDATE(),"+
        "INTERVAL (DAY(CURDATE())) DAY));")
    income_flat_list = max_iteams(sql5)

    #--------------------------------expense--------------------------------    
    sql6=("SELECT expense FROM "+table+" WHERE (t_date BETWEEN DATE_SUB(DATE_SUB(CURDATE()"+
        ",INTERVAL (DAY(CURDATE())-1) DAY), INTERVAL 1 MONTH) AND DATE_SUB(CURDATE(),"+
        "INTERVAL (DAY(CURDATE())) DAY));")

    expense_flat_list =  max_iteams(sql6)

    #--------------------------------tax--------------------------------    
    sql7 = ("SELECT tax FROM "+table+" WHERE (t_date BETWEEN DATE_SUB(DATE_SUB(CURDATE()"+
        ",INTERVAL (DAY(CURDATE())-1) DAY), INTERVAL 1 MONTH) AND DATE_SUB(CURDATE(),"+
        "INTERVAL (DAY(CURDATE())) DAY));")
    tax_flat_list =  max_iteams(sql7)
    
    #---------------------close connection to the database---------------------  
    
#    return(len(item_id_flat_list),len(client_flat_list),len(state_flat_list),len(t_date_flat_list),len(income_flat_list),len(expense_flat_list),len(tax_flat_list))
    return(item_id_flat_list,client_flat_list,state_flat_list,
           t_date_flat_list,income_flat_list,expense_flat_list,tax_flat_list,str(month))


def make_monthly_html(table):
    table = str(table)
    cid,cl,st,tdt,incm,expns,tx,month = monthly_HTML_data(table)
    begnning = "<!DOCTYPE html><html><head><meta charset='UTF-8'><title>MONTHLY REPORT</title>"
    border = "body {background-color: white;margin-left: 10%;margin-right: 10%;border: 5px ridge #191970;padding: 10px 10px 10px 10px;font-family: Times New Roman;}"
    style = "<style> table, th, td {border: 1px solid black;border-collapse: collapse;padding: 15px;text-align: left;background-color: #bdedc0;}"+border+"</style>"
    hearder = "</head><body><h1>"+ table.upper() +", "+ month +"</h1>"
    lastPart = "</body> </html>"
    pie_chart = html_pie_chart(table, incm, expns, tx)
    
    strTable = "<table><tr><th>ID</th><th>Client</th><th>State</th><th>Date</th><th>Income</th><th>Expense</th><th>Tax</th></tr>"
    
    for (a, b, c, d, e, f, g) in zip(cid,cl,st,tdt,incm,expns,tx):
        strRW = "<tr><td>"+str(a)+ "</td><td>"+str(b)+"</td><td>"+str(c)+ "</td><td>"+str(d)+"</td><td>"+str(e)+ "</td><td>"+str(f)+ "</td><td>"+str(g)+"</td></tr>"
        strTable = strTable+strRW
     
    strTable = strTable+"</table>"
     
    htmlStirng = begnning + style + hearder + pie_chart + strTable + lastPart
    Html_file= open(table+" "+month+".html","w")
    Html_file.write(htmlStirng)
    Html_file.close()
    return htmlStirng

###All###
def all_HTML_data(table):
    cid = max_iteams("SELECT id FROM "+table+";")
    cl = max_iteams("SELECT client FROM "+table+";")
    st = max_iteams("SELECT state FROM "+table+";")
    tdt = max_iteams("SELECT t_date FROM "+table+";")
    tdt = flat_date(tdt)
    incm = max_iteams("SELECT income FROM "+table+";")
    expns = max_iteams("SELECT expense FROM "+table+";")
    tx = max_iteams("SELECT tax FROM "+table+";")

    begnning = "<!DOCTYPE html><html><head><meta charset='UTF-8'><title>YERALY REPORT</title>"
    border = "body {background-color: white;margin-left: 10%;margin-right: 10%;border: 5px ridge #191970;padding: 10px 10px 10px 10px;font-family: Times New Roman;}"
    style = "<style> table, th, td {border: 1px solid black;border-collapse: collapse;padding: 15px;text-align: left;background-color: #bdedc0;}"+border+"</style>"
    hearder = "</head><body><h1>"+ table.upper() +" all" +"</h1>"
    pie_chart = html_pie_chart(table, incm, expns, tx)
    lastPart = "</body> </html>"    
    strTable = "<table><tr><th>ID</th><th>Client</th><th>State</th><th>Date</th><th>Income</th><th>Expense</th><th>Tax</th></tr>"    
    
    for (a, b, c, d, e, f, g) in zip(cid,cl,st,tdt,incm,expns,tx):
        strRW = "<tr><td>"+str(a)+ "</td><td>"+str(b)+"</td><td>"+str(c)+ "</td><td>"+str(d)+"</td><td>"+str(e)+ "</td><td>"+str(f)+ "</td><td>"+str(g)+"</td></tr>"
        strTable = strTable+strRW 
    
    strTable = strTable+"</table>"
    htmlStirng = begnning + style + hearder + pie_chart + strTable + lastPart
    Html_file= open(table+" all.html","w")
    Html_file.write(htmlStirng)
    Html_file.close()

###RECENT####
def get_recent_data(table):  
       
    #--------------------------------iteam_id--------------------------------        
    tbl = ("SELECT MAX(id) FROM "+table+";")
    iteam = max_iteams(tbl)
    n = iteam[0]
        
    if n>50:        
        cid = max_iteams("SELECT id FROM "+table+" ORDER BY id DESC,t_date desc LIMIT 50;")
        cl = max_iteams("SELECT client FROM "+table+" ORDER BY id DESC,t_date desc LIMIT 50;")
        st = max_iteams("SELECT state FROM "+table+" ORDER BY id DESC,t_date desc LIMIT 50;")
        tdt = max_iteams("SELECT t_date FROM "+table+" ORDER BY id DESC,t_date desc LIMIT 50;")
        dte = []
        for date in tdt:
            date = str(date)
            dte.append(date)
        incm = max_iteams("SELECT income FROM "+table+" ORDER BY id DESC,t_date desc LIMIT 50;")
        expns = max_iteams("SELECT expense FROM "+table+" ORDER BY id DESC,t_date desc LIMIT 50;")
        tx = max_iteams("SELECT tax FROM "+table+" ORDER BY id DESC,t_date desc LIMIT 50;")
        return cid,cl,st,dte,incm,expns,tx
    else:
        try:
            cid = max_iteams("SELECT id FROM "+table+" ORDER BY id DESC,t_date desc LIMIT "+str(n)+";")
            cl = max_iteams("SELECT client FROM "+table+" ORDER BY id DESC,t_date desc LIMIT "+str(n)+";")
            st = max_iteams("SELECT state FROM "+table+" ORDER BY id DESC,t_date desc LIMIT "+str(n)+";")
            tdt = max_iteams("SELECT t_date FROM "+table+" ORDER BY id DESC,t_date desc LIMIT "+str(n)+";")
            dte = []
            for date in tdt:
                date = str(date)
                dte.append(date)
            incm = max_iteams("SELECT income FROM "+table+" ORDER BY id DESC,t_date desc LIMIT "+str(n)+";")
            expns = max_iteams("SELECT expense FROM "+table+" ORDER BY id DESC,t_date desc LIMIT "+ +";")
            tx = max_iteams("SELECT tax FROM "+table+" ORDER BY id DESC,t_date desc LIMIT "+str(n)+";")
            return cid,cl,st,dte,incm,expns,tx   
        except:
            pass

def make_recent_html(table):
    table = str(table)
    cid,cl,st,tdt,incm,expns,tx = get_recent_data(table)
    begnning = "<!DOCTYPE html><html><head><meta charset='UTF-8'><title>MONTHLY REPORT</title>"
    border = "body {background-color: white;margin-left: 10%;margin-right: 10%;border: 5px ridge #191970;padding: 10px 10px 10px 10px;font-family: Times New Roman;}"
    style = (html_bar_chart(tdt,incm,expns,tx) + "<style> table, th, td {border: 1px solid black;border-collapse: collapse;padding:"+
             " 15px;text-align: left;background-color: #bdedc0;}"+border+" </style>")
    hearder = "</head><body>"+"<div id='curve_chart' style='width: 600px; height: 400px'></div>"+"<h1>"+ table.upper() +" Recent</h1>"
    lastPart = "</body> </html>"

    strTable = "<table><tr><th>ID</th><th>Client</th><th>State</th><th>Date</th><th>Income</th><th>Expense</th><th>Tax</th></tr>"
    
    for (a, b, c, d, e, f, g) in zip(cid,cl,st,tdt,incm,expns,tx):
        strRW = "<tr><td>"+str(a)+"</td><td>"+str(b)+"</td><td>"+str(c)+"</td><td>"+str(d)+"</td><td>"+str(e)+ "</td><td>"+str(f)+ "</td><td>"+str(g)+"</td></tr>"
        strTable = strTable+strRW
     
    strTable = strTable+"</table>"
     
    htmlStirng = begnning + style + hearder + strTable + lastPart
    Html_file= open(table+" recent.html","w")
    Html_file.write(htmlStirng)
    Html_file.close()
    return htmlStirng

def generate_html():
    tables_in_DB = TableListInDB()
    # load the json data consist of tax periods and payment date
    with open('/Users/ziaulchoudhury/Desktop/taxDate.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
        ny_s_p = data['ny_s_p']
        ny_e_p = data['ny_e_p']
        ny_payment = data['ny_payment']
        nj_il_chicago_s_p = data['nj_il_chicago_s_p']
        nj_il_chicago_e_p = data['nj_il_chicago_e_p']
        nj_il_chicago_payment = data['nj_il_chicago_payment']
        ct_s_p = data['ct_s_p']
        ct_e_p = data['ct_e_p']
        ct_payment = data['ct_payment']
     
    for table in tables_in_DB:
        make_recent_html(table)
        all_HTML_data(table)
    

    for table in tables_in_DB:
        try:
            make_monthly_html(table)
        except:
            print("no monthly data found")
    
    for table in tables_in_DB:
        table = str(table)
        try:
            generate_other(table,"NJ",nj_il_chicago_s_p,nj_il_chicago_e_p,nj_il_chicago_payment)
            generate_other(table,"CHICAGO",nj_il_chicago_s_p,nj_il_chicago_e_p,nj_il_chicago_payment)
            generate_other(table,"CT",ct_s_p,ct_e_p,ct_payment)
            generate_ny(table,ny_s_p,ny_e_p,ny_payment)
        except:
            print("no monthly data found")



#-------------# GUI part #-------------#
def tick(time1=''):
    # get the current local time from the PC
    time2 = time.strftime(' %A \n %Y-%m-%d \n %I:%M:%S %p')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock_lbl.config(text=time2)
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
            messagebox.showwarning("????????? Warning!! ?????????\n", 
                                   "You need to enter valid entery for all iteams.\n\t\t\t\t?????????")
            clear_entry4()
    if iteam5 !="": 
        try:
            tasks.append(iteam5)
            iteam5 = float(iteam5)
            lis.append(str(iteam5))
        except:
            messagebox.showwarning("????????? Warning!! ?????????\n", 
                                   "You need to enter valid entery for all iteams.\n\t\t\t\t?????????")
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
            messagebox.showwarning("????????? Warning!! ?????????\n", 
                                   "You need to enter valid entery for all iteams.\n\t\t\t\t?????????")
    else:
        messagebox.showwarning("????????? Warning!! ?????????\n", 
                               "You need to enter valid entery for all iteams.\n\t\t\t\t?????????")
    
    e1.delete(0, "end")
    e2.delete(0, "end")
    e3.delete(0, "end")
    e4.delete(0, "end")
    e5.delete(0, "end")
    e6.delete(0, "end")

		
def del_all():
	confirmed = messagebox.askyesno("Please Confirm", "delete all history!")
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
                   text="  (??????????????????? ????????? Account Management System ???(?????????)????????????  ",
                   background = 'blue', foreground = 'white')
lblInfo.grid(column=0, row=0)

lbl_title = tk.Label(leftSide, text="Iteams???", font=('times', 35, 'bold'),
                     bg="#00FF7F", foreground = '#773420')
lbl_title.grid(row=0,column=0)

lbl_title2 = tk.Label(leftSide, text="Entry???", font=('times', 35, 'bold'),
                     bg="#00FF7F", foreground = '#773420')
lbl_title2.grid(row=0,column=1)

lbl_title3 = tk.Label(leftSide, text="CE???", font=('times', 35, 'bold'),
                     bg="#00FF7F", foreground = '#773420')
lbl_title3.grid(row=0,column=2)

lbl_title4 = tk.Label(leftSide, text="History???", font=('times', 35, 'bold'),
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
clear_all = tk.Button(leftSide, text=" ???\nClear\nall\n Entries ",font = ('times', 30, 'bold'), width = 7,
                highlightbackground = 'lightgray', foreground = 'red', height=4,
                command=clear_all_entries)
clear_all.grid(row=7,column=2)

btn_add_task = tk.Button(leftSide, text = 'Add Entry', font=('times', 31, 'bold'), width = 17,
                highlightbackground='lightgray', foreground = '#114ACE', height = 4, command=add_task)
btn_add_task.grid(row=7,column=0)

btn_del_all = tk.Button(leftSide, text = 'Delete All\nHistory', font = ('times', 31, 'bold'), width = 17,
                highlightbackground = 'lightgray', foreground = 'red', height=4, command=del_all)
btn_del_all.grid(row=7,column=3)

# clock
clock_lbl = tk.Label(leftSide, text = "", font=('times', 25, 'bold'), width = 14, fg = "#046666",
                 bg = 'lightgray', height = 5)
clock_lbl.grid(row = 7, column = 1)
tick()

#Start the main events loop
root.mainloop()
generate_html()
    

