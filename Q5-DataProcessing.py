import pandas as pd
import requests
import json
from datetime import datetime
import re



response_API = requests.get('http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes')
data =json.loads(response_API.text)     # convert json object to text format
df=pd.DataFrame(data["_embedded"]["episodes"]) #Creat Dataframe for Data processing
df=df.convert_dtypes() # Auto format data for already cleand Columns
df.airdate=df.airdate.astype("datetime64[ns]") # Convert to date time format
df.airtime=df.airtime.apply(lambda X: datetime.strptime(X, "%H:%M").strftime("%I:%M%p")) # convert 24 hour time to 12 hour time format.
df.runtime=df.runtime.astype(float)  #convert to float data type
df["average rating"]=df.rating.apply(lambda X: X.get("average")).astype(float)  # clean avarage colunm and rename column
df.drop(columns=["rating"],axis=1,inplace=True)
pattern = re.compile('<.*?>') 
df.summary=df.summary.apply(lambda X: re.sub(pattern,"",X)).astype("string") # use regex to remove any HTML tag from Data string.
df["medium image link"]=df.image.apply(lambda X: X.get("medium")).astype("string") # conver image column to two sapare column.
df["Original image link"]=df.image.apply(lambda X: X.get("original")).astype("string")
df.drop(columns=["image","_links","airstamp"],inplace=True)
df.to_csv("Cleaned_data.csv",index=False)
