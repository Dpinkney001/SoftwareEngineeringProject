This is Python application that can be used for account management. It also provides a graphical user interface that takes user inputs, access MySQL database, and add user inputs to an existing table or create the new table dynamically in the database.

To run this program, you will need:
- Python IDE (Aanaconda 3.0+ -> Spyder -> Python 3.0+ recommended. Also, please make sure your python has pymysql, time, warnings, datetime, json, os, and tkinter modules. if you don't have them you can easily install them from the terminal by googling the Anaconda command).
- Database with data (You can use the CSV data provided in the data folder for importing to your database).
- Make modification to the "def ConnectToSQL()" method accordingly to access the database from your PC.
- Make modification to the "def generate_html()" for providing the path to the JSON data where it's saved.

p.s. Since this program dynamically creates table in the database you can just run the program after creating the database to create the tables for "food_truck", "battery_company", "lagguge_company", "sandwich_shop", "bread_factory", and "master_table" . You can also find MySQL command on https://github.com/zchy/accountDB_with_mySQL_and_Python/blob/master/accountDB.sql to create the database, but don't forget to change the database name to "Account Database".

## Good Luck!!
## Ziaul
