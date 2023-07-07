import pandas as pd

try:
    df=pd.read_json("https://data.nasa.gov/resource/y77d-th95.json")
    df.drop(labels=[":@computed_region_cbhk_fwbd",":@computed_region_nnqa_25f4"],axis=1,inplace=True)
    df.dropna(inplace=True)
    df=df.convert_dtypes()# Auto convert to prefared Data type
    df.year=df.year.apply(lambda X: X.split("T")[0]) 
    df.year=pd.to_datetime(df['year'], errors = 'coerce') #converting year data to Datatime value.
    df.geolocation=df.geolocation.apply(lambda x: [int(x.get("coordinates")[0]),int(x.get("coordinates")[1])]) # converting geolocation data to int of list.
    df.to_csv("Structured_data.csv",index=False)
except Exception as e:
    raise Exception(e)