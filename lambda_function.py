import json
import requests
import pandas as pd

def lambda_handler(event, context):

    print("EVENT DATA->: ", event)
    response=requests.get("https://www.google.com/")
    print("RESPONSE FORM REQUESTS GOOGLE:___", response.text)

    d={'col1':[1,2],'col2':['a','b']}
    df=pd.DataFrame(data=d)
    print("DATAFRAME",df)
    print("DONE")

