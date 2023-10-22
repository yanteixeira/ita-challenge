#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import pandas as pd

BASE_URL = "http://montreal.icea.decea.mil.br:5002/api/v1"
TOKEN = "a779d04f85c4bf6cfa586d30aaec57c44e9b7173"
PARAMS = {
    "token": TOKEN,
    "idate": "2022-06-01",
    "fdate": "2023-05-12"
}
HEADERS = {
    "accept": "application/json"
}

def fetch_and_save_data(endpoint):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url, params=PARAMS, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df.to_csv(f'{endpoint}.csv', index=False)
        print(f"Data saved to {endpoint}.csv")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    endpoints = ["bimtra", "esperas", "metar", "metaf", "tc-prev", "tc-real"]
    for endpoint in endpoints:
        fetch_and_save_data(endpoint)

