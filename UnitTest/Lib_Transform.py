## pip install pandas sqlalchemy pyodbc
import pandas as pd
from sqlalchemy import create_engine

def pd_read_csv(path,IdCol,DateCol1,DateCol2,CompareDates,BlankCheck):
    df = pd.read_csv(path)
    df = df.dropna(subset=[IdCol])
    if DateCol1:
        df[DateCol1] = pd.to_datetime(df[DateCol1], format='"%d/%m/%Y"',errors='coerce')
    if DateCol2:
        df[DateCol2] = pd.to_datetime(df[DateCol2], format='mixed',errors='coerce')
    if CompareDates:
        df["Duration"] = (df[DateCol2] - df[DateCol1]).dt.days
        dfDurationError = df[df["Duration"]<0]
        df = df[df["Duration"]>=0]
    dfError = df[df[BlankCheck].isna()]
    df = df.dropna(subset=[BlankCheck])
    if CompareDates:
        dfErrors = pd.concat([dfDurationError, dfError])
    if not CompareDates:
        dfErrors = dfError
    return df
    
def write_SQL(name,server,database,df):
    connection_string = f'mssql+pyodbc://@{server}/{database}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
    engine = create_engine(connection_string)
    df.to_sql(name,engine)
    return print("Success")

if __name__ == "__main__":
    filePath = 'C:/Users/Admin/Desktop/GitHub_Stuff/demo/03_Library SystemBook.csv'
    df = pd_read_csv(path=filePath, IdCol='Id', DateCol1='Book checkout',DateCol2='Book Returned',CompareDates=True,BlankCheck='Customer ID')
    write_SQL(name='Book_Loans_New',server='localhost',database='Library_Project',df=df)