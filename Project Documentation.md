# Project Objectives

1. Set up GitHub Repo for project.
2. Design an architectural diagram for this pipeline. 
3. Implement the python application that does the data cleaning.
4. Test the python application. 
5. If there are no bugs, deploy our pipeline (CI/CD).
6. Trigger the pipeline to write to a database. 
7. Use the written data to create a PowerBI dashboard.

#Lib_Transform.py functions
#pd_read_csv
    This will clean any file given to it with optional date comparison.
    Options:
        1. Path = this should be the file path of the csv to be processed. Must be string and include file extension
        2. IdCol = this should be the name of a column used to identify a row of data (i.e no blanks) this can be a subset.
        3. DateCol1 = if there is a date to be converted, include column name here (earliest date i.e. from) if none, this should be set to False
        4. DateCol2 = if there is a second date to be converted, include column name here (latest date i.e. to) if none, this should be set to False
        5. CompareDates = if DateCol1 and DateCol2 are used, this can be set to True to create a column with number of days between (latest - earliest). Otherwise set to False
        6. BlankCheck = This should include the name(s) of critical data columns, missing data considered an error.

#write_SQL
    This will write a dataset to a database table.
    Options:
        1. Name = Name of the table to be created
        2. Server = This should be localhost if local, otherwise cloud specific
        3. database = the name of the database where the table should be created
        4. df = this is the dataframe to be writen to a table