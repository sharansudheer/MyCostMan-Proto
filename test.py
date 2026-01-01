import pandas as pd
import numpy as np


df=pd.read_csv('')
df.head()

df['Mileage']=df['Mileage'].astype(str)
df['Engine']=df['Engine'].astype(str)
df['Power']=df['Power'].astype(str)
df['Mileage']=df['Mileage'].str.replace('kmpl','')
df['Mileage']=df['Mileage'].str.replace('km/kg','')
df['Engine']=df['Engine'].str.replace('CC','')
df['Power']=df['Power'].str.replace('bhp','')
