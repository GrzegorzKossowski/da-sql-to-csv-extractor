import colors
import pandas as pd
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import DataError


def save_csv_file(filename, query):
  # params
  hostname = 'localhost'
  port = "5432"
  database = 'northwind'
  username = 'northwind'
  password = 'northwind'

  # create URI
  database_uri = f"postgresql://{username}:{password}@{hostname}:{port}/{database}"
  engine = create_engine(database_uri)

  # get data from db to DataFrame, close connection
  try:
    df = pd.read_sql_query(query, engine)
  except:
    colors.prRed("Error occured while executing a query")
  
  csvPath = 'csv'
  isExist=os.path.exists(csvPath)
  if not isExist:
    os.makedirs(csvPath)
  
  try:
    df.to_csv(f"./{csvPath}/{filename}.csv", index=False)
    print(df)
  except:
    colors.prRed('Unable to write a file')
