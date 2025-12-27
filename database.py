
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from urllib.parse import quote_plus
from sqlalchemy import create_engine
import urllib
import os
#Step 1:Create the session 
#To do that call the sessionmaker function from sqlalchemy.orm


# 1. Load the variables from the .env file
load_dotenv() 

# 2. Get the password from the .env variable
raw_password = os.getenv("DB_PASSWORD")

encoded_password=urllib.parse.quote_plus(raw_password)

db_url=f"postgresql://postgres:{encoded_password}@localhost:5432/telusko" #Step 2: write the Database URL

engine=create_engine(db_url)  #Step 3: Creating the engine also import it from sqlalchemy

session=sessionmaker(autocommit=False,autoflush=False,bind=engine)  #Step 4: Creating the session
