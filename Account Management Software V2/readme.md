# The versoin 2 of the AMS.

## This version contians:
- Error and bug fixes (won't show warnning message after valid input provided, table title renamed to 'Tax' previously worng title provided for the tax).
- Numbers are now rounded (client requested in the last presentation).
- As a reminder: don't forget put all HTML files in one folder and change the database name accordingly.

## Info:
This is a Python application that can be used for account management. It also provides a graphical user interface that takes user inputs, access MySQL database, and add user inputs to an existing table or create the new table dynamically in the database.

### To run this program, you will need:
- Python IDE (Aanaconda 3.0+ -> Spyder -> Python 3.0+ recommended. Also, please make sure your python has pymysql, time, warnings, datetime, json, os, and tkinter modules. if you don't have them you can easily install them from the terminal by googling the Anaconda command).
- Database with data (You can use the CSV data provided in the data folder for importing to your database).
- Make modification to the "def ConnectToSQL()" method accordingly to access the database from your PC.
- Make modification to the "def generate_html()" for providing the path to the JSON data where it's saved.
###### p.s. Since this program dynamically creates table in the database you can just run the program after creating the database to create the tables for "food_truck", "battery_company", "lagguge_company", "sandwich_shop", "bread_factory", and "master_table" . You can also find MySQL command on https://github.com/zchy/accountDB_with_mySQL_and_Python/blob/master/accountDB.sql to create the database, but don't forget to change the database name to "Accounts Database".


## Some of Key Points.

### Requirements:
- The client wants to be able to manage the sales tax of his client companies.
- The sales tax needs to paid to each state based on the peroid and by collection dates.
- Track the amount of transactions in the sales account and the amount of sales tax in the Escrow account for every client.
- Send or display a statement to the client for monthly transactions.
- 5 clients and 5 different POS( point-of-sales).

### Desagin:
- UML diagram using a single class to hold the accounting information per each client/company.
- 5 Companies, 5 buisness and escorw accounts for income, expenses, and taxes(NY, NJ, CT, Chicago, Boston).
- Data Analytics. The gathered tables, charts and graphs of the income, expenses and the sales tax collected as HTML reports.
- Expenses gets debited from the income account and NOT the tax accounts.
- Statements get generated out as HTML file for each clients' and admin's homepage where you can access recent, monthly, tax reports based on tax period and payment dates for each states, all, and summary reports for each client.

### This model of solution provides:
- Python Program.
- Connects to the database.
- Reads client(s)’ data.
- Provides Graphical User Interface for the user inputs.
- Adds new data to database from the user inputs.
- Access JSON data file which contaions tax period dates and payment dates for each state.
- Process the HTML pages and reports(homepage, recent, monthly, quarterly tax, all, and summary) for each client and admin.

### How to access the HTML reports:
For each client the homepages are named "Client_Name Home". Once client opens its homepage in the web browser, the client will be able to access all the reports from the homepage. For admin, the homepage is named "Home Home". Once the admin opens in the web browser, the admin will have access to all clients homepages and the reports. The admin homepage also have a summary page which contains summary report where the admin can see overall account summary for all the 5 clients, and "master_table homepage" if the admin wish to see all the transactions in one place. 

# Documantation link: https://docs.google.com/document/d/1461nRt6sxTG2U2MwdWIaMmRoIS7vBMk2D1cvPZ7lXsI/edit?usp=sharing

# All the files and the code can be found backedup on the link below. If anything missing, please refer to the provided link.
# Link: https://github.com/zchy/accountDB_with_mySQL_and_Python/blob/master/Version%202-Updated/

