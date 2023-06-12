
import os
import pandas as pd
import pathlib
import requests
from dotenv import load_dotenv

script_grandparent_path = pathlib.Path(__file__).parent.parent
dotenv_path = pathlib.Path(script_grandparent_path, ".env")
load_dotenv(dotenv_path)

LIST_API_KEY = os.getenv("LIST_API_KEY")

list_url = 'https://m4-2dcc.vmhost.psu.edu/list'
api_url = list_url + '/api/v2/'

headers = {
    'Content-Type': 'application/json',
    'X-API-Key': LIST_API_KEY
}

query = {'instrumentId': 'MBE1'}

def getSampleList(query=query,headers=headers):
    response = requests.post(api_url+'samples/search', json=query, headers=headers)

    all_samples = response.json()
    dir(response)
    print(response.json())
    keys = ['id', 'sampleLabel', 'creationDate', 'materials', 'techniqueId', 'userId']
    data = all_samples['data']
    df = pd.DataFrame({k: [x[k] for x in data] for k in keys})
    print(df)
    return df
