import pandas as pd
import json
from datetime import datetime
import numpy as np
import openpyxl
import requests

response_API = requests.get('https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json')
data =json.loads(response_API.text)
df=pd.DataFrame(data["pokemon"])
df.num=df.num.astype("int64")
df=df.convert_dtypes()
df.type=df.type.astype("string") 
df.height=df.height.apply(lambda X: X.split(" ")[0]).astype("float64") # changing height column to float
df.weight=df.weight.apply(lambda X: X.split(" ")[0]).astype("float64")
value_dict={"Not in Eggs": "0" ,"5 km":"5","10 km":"10","2 km":"2","Omanyte Candy":"5"}
df.egg=df.egg.replace(value_dict).astype("float64")
df.avg_spawns=df.avg_spawns*10. # Number of this pokemon on 10.000 spawns so multiplyed by 10
df.avg_spawns=df.avg_spawns.astype("int64")
df.spawn_time.replace({"N/A":"00:00","<NA>": "00:00"},inplace=True)
df.spawn_time=df.spawn_time.astype("datetime64[ms]")
df.spawn_time=df.spawn_time.apply(lambda X: X.strftime("%M:%S")) # transforming the time to minute and second format as Datetime 

df.multipliers.replace(np.nan,"0",inplace=True)
def change(n):
        try:
            if n == 0:
                return np.nan
            else:
                lis=[]
                for j in n:
                    lis.append(int(round(float(j))))
                return lis
        except Exception as e:
                 raise Exception(e)
        
df.multipliers=df.multipliers.apply(change)
df.to_excel("Structured_Data.xlsx",index=False) # structured data  output in xlsx format







