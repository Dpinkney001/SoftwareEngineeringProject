#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 13:28:26 2018

@author: ziaulchoudhury
"""

import random,csv
import numpy as np
from itertools import zip_longest
import datetime


shortRangeClient = ['food_truck','bread_factory','sandwich_shop']
longRangeUSClinet = ['lagguge_company','battery_company']
shortRangeLocation = ['NY','NJ','CT']
longRangeLocation = ['NY','NJ','CT','BOSTON', 'CHICAGO']

#localOrIntClinet = ['Lagguge Company: 4']
#localAndIntLocation = ['NY','NJ','CT','Boston', 'Chicago', 'International']



#pick random client
def randomID(clientID):
    cliID = (clientID)
    return (cliID)

#random tax with deciaml interger
def randomIncome(minimun,maximum):
    r = random.randint(minimun,maximum)
    income = (random.randint(0,100))/10 + r
    return float(income)

#enpense based on income
def expenses(income):
    expense = []
    expnsPCT = float(random.randrange(30, 75))/100
    for expns in income:
        k = float(expns)*expnsPCT
        expense.append(k)
    return (expense)
    

#random state
def randomState(loaction):
    l = random.choice(loaction)
    return str(l)

#random date
def random_date_generator(start_date, range_in_days):
    days_to_add = np.arange(0, range_in_days)
    random_date = np.datetime64(start_date) + np.random.choice(days_to_add)
    return random_date

def randomDate():
    date = random_date_generator('2017-01-01', 435)
    return str(date) 

#Calcualte tax
def calculateTax(location,income):
    NY = 0.08875
    NJ = 0.06625
    CT = 0.0635
    Chicago = 0.1025
    Boston = 0.0625
    international = 0.18
    tax=[]
    
    for l,i in list(zip(location, income)):
        if l == "NY":
            tax.append(i*NY)
        elif l == "NJ":
            tax.append(i*NJ)
        elif l == "CT":
            tax.append(i*CT)
        elif l == "CHICAGO":
            tax.append(i*Chicago)
        elif l == "BOSTON":
            tax.append(i*Boston)
        elif l == "INTERNATIONAL":
            tax.append(i*Boston)
        else :
            tax.append(i*international)
    return tax

# find indeces containing string
def find_indices(value, qlist):
    indices = []
    idx = -1
    while True:
        try:
            idx = qlist.index(value, idx+1)
            indices.append(idx)
        except ValueError:
            break
    return (indices)

# Fill random data  
def generateData(buisnessName,location,maxitr,minimun,maximum):  
    clnt=[]
    st=[]
    dte=[]
    incm=[]
    tx=[]
    expns=[]
    for number in range(0,maxitr):
        dte.append(randomDate())
    
    dte = list(set(dte))
    dte.sort()
        
    for number in range(0, len(dte)):
        clnt.append(randomID(buisnessName))  
        st.append(randomState(location))
        incm.append(randomIncome(minimun,maximum))
        
    expns = expenses(incm)
    tx = calculateTax(st,incm)
    
    
    return clnt, st, dte, incm, expns, tx

#get today's date
def getToday():
    return datetime.date.today().strftime("%Y%m%d")

# save data as csv
def save_result_as_csv(name,a,b,c,d,e,f):
    filename = "%s_%s.%s" % (name, getToday() ,"csv")
    with open(filename, 'w') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(["client_name", "state", "date", "income", "expense", "tax"])
        for row in zip_longest(a,b,c,d,e,f): # writing to csv with longest list index
            writer.writerow(row)
    
    outcsv.close()

#1
#Call the function to generate Food Truck:1 data
clnt, st, dte, incm, expns, tx = generateData(shortRangeClient[0],shortRangeLocation,450,300,2000)
save_result_as_csv('food_truck',clnt, st, dte, incm, expns, tx)

clientFT=clnt
loactionFT=st 
incomeFT=incm
expenseFT=expns
taxAmmountFT=tx
dateFT=dte

food_truck_ny = (find_indices("NY", loactionFT)) 
food_truck_nj = (find_indices("NJ", loactionFT)) 
food_truck_ct = (find_indices("CT", loactionFT)) 

#print(food_truck_ct)

#2
#Call the function to generate Bread Factory: 3 data
clntBF, stBF, dteBF, incmBF, expnsBF, txBF = generateData(shortRangeClient[1],shortRangeLocation,450,3000,10000)
save_result_as_csv('bread_factory',clntBF, stBF, dteBF, incmBF, expnsBF, txBF)

clientBF=clntBF
loactionBF=stBF 
incomeBF=incmBF
expenseBF=expnsBF
taxAmmountBF=txBF
dateBF=dteBF

bread_factory_ny = (find_indices("NY", loactionBF)) 
bread_factory_nj = (find_indices("NJ", loactionBF)) 
bread_factory_ct = (find_indices("CT", loactionBF)) 

#print(bread_factory_ct)

#3
#Call the function to generate Sandwich Shop: 3 data
clntSS, stSS, dteSS, incmSS, expnsSS, txSS = generateData(shortRangeClient[2],shortRangeLocation,450,2000,5000)
save_result_as_csv('sandwich_shop',clntSS, stSS, dteSS, incmSS, expnsSS, txSS)

clientSS=clntSS
loactionSS=stSS 
incomeSS=incmSS
expenseSS=expnsSS
taxAmmountSS=txSS
dateSS=dteSS

sandwich_shop_ny = (find_indices("NY", loactionSS)) 
sandwich_shop_nj = (find_indices("NJ", loactionSS)) 
sandwich_shop_ct = (find_indices("CT", loactionSS)) 

#print(sandwich_shop_ct)

#4
#Call the function to generate Lagguge Company: 4 data
clntLC, stLC, dteLC, incmLC, expnsLC, txLC = generateData(longRangeUSClinet[0],longRangeLocation,450,10000,75000)
save_result_as_csv('lagguge_company',clntLC, stLC, dteLC, incmLC, expnsLC, txLC)

clientLC=clntLC
loactionLC=stLC 
incomeLC=incmLC
expenseLC=expnsLC
taxAmmountLC=txLC
dateLC=dteLC

lagguge_company_ny = (find_indices("NY", loactionLC)) 
lagguge_company_nj = (find_indices("NJ", loactionLC)) 
lagguge_company_ct = (find_indices("CT", loactionLC)) 
lagguge_company_boston = (find_indices("BOSTON", loactionLC)) 
lagguge_company_chicago = (find_indices("CHICAGO", loactionLC)) 

#print(lagguge_company_ct)

#5
#Call the function to generate Battery Company: 5 data
clntBC, stBC, dteBC, incmBC, expnsBC, txBC = generateData(longRangeUSClinet[1],longRangeLocation,450,15000,100000)
save_result_as_csv('battery_company',clntBC, stBC, dteBC, incmBC, expnsBC, txBC)

clientBC=clntBC
loactionBC=stBC 
incomeBC=incmBC
expenseBC=expnsBC
taxAmmountBC=txBC
dateBC=dteBC

battery_company_ny = (find_indices("NY", loactionBC)) 
battery_company_nj = (find_indices("NJ", loactionBC)) 
battery_company_ct = (find_indices("CT", loactionBC)) 
battery_company_boston = (find_indices("BOSTON", loactionBC)) 
battery_company_chicago = (find_indices("CHICAGO", loactionBC))

#print(battery_company_ct)

#Putting all the data togather as csv
allClient=clientFT+clientBF+clientSS+clientLC+clientBC
allLocation=loactionFT+loactionBF+loactionSS+loactionLC+loactionBC
allIncome=incomeFT+incomeBF+incomeSS+incomeLC+incomeBC
allExpense=expenseFT+expenseBF+expenseSS+expenseLC+expenseBC
allTaxAmmount = taxAmmountFT+taxAmmountBF+taxAmmountSS+taxAmmountLC+taxAmmountBC
allDate = dateFT+dateBF+dateSS+dateLC+dateBC

#print(len(allDate))
save_result_as_csv('all_data',allClient,allLocation,allDate,allIncome,allExpense,allTaxAmmount)
