Lab Overview:
## This lab is about loading datas from the Cities.csv file then put it ## into a table that has a filter and aggregation functions in it then ## use the that table for tasks.

oop_lab_1/
│
├── README.md             # This file
├── Cities.csv            # The dataset
|── data_processing.py	  # The analysis code

# Design Overview:
##     DataLoader class:
###          __init__ function:
####            This function have base_path as key then contain the base_path in self.base_path if the base_path is equal to None then it will take the path from the  current directory but if not self.base_path will use that base_path using Path() from pathlib library.
###        load_csv function:
####            The function has 1 key (filename) and has 2 variables:
#####                1. filepath contains the path of the file (self.base_path / filename)
#####                2. data variable contains the data_list that read using csv.DictReader
##    Table class:
###        __init__ function:
####            has 2 keys (header, table):
#####                self.header contains header
#####                self.table contains table
###        filter function:
####            has 1 key (condition)
####            has 1 variable (temps):
#####                temps contains nested dict list of the data that have the cities that met the condition that have been given then the function return the Table that has temps as argument          
###        aggregate function:
####            has 2 keys (aggregation_function, aggregation_key)
####            has 1 variable (temps):
#####                temps is a list of the data in the table that has the same key as aggregation_key and always try to convert the data to float before append into the temps if cant just append it normally
####            then return the temps that processed through the aggreagation_function

# How to run:
##      The programs has provided 6 testers in it you can use run the program using py command  