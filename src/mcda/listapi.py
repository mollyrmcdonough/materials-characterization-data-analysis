import requests
import pandas as pd
list_url = 'https://m4-2dcc.vmhost.psu.edu/list'
api_url = list_url + '/api/v2/'

def setHeaders(API_KEY):
    '''
    This function defines headers to interact with the 2DCC LiST API v2
    '''
    headers = {
    'Content-Type': 'application/json',
    'X-API-Key': API_KEY
    }
    return headers
def getSampleList(query,headers):
    response = requests.post(api_url+'samples/search', json=query, headers=headers)
    all_samples = response.json()
    dir(response)
    print(response.json())
    keys = ['id', 'sampleLabel', 'creationDate', 'materials', 'techniqueId', 'userId','instrumentId']
    data = all_samples['data']
    df = pd.DataFrame({k: [x[k] for x in data] for k in keys})
    print(df)
    return df