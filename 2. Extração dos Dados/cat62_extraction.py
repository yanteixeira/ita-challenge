#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime, timedelta
import requests
import pandas as pd

def extract_cat62_data():
    dfs = []

    base_url = "http://montreal.icea.decea.mil.br:5002/api/v1/{}"
    endpoints = ['cat-62']
    token = "a779d04f85c4bf6cfa586d30aaec57c44e9b7173"
    headers = {"accept": "application/json"}

    start_date = datetime(2022, 6, 1)
    end_date = datetime(2023, 5, 12)
    step = timedelta(days=1)

    date_format = "%Y-%m-%d %H:%M:%S.000"

    for endpoint in endpoints:
        current_date = start_date

        while current_date <= end_date:
            params = {
                "token": token,
                "idate": current_date.strftime(date_format),
                "fdate": (current_date + step).strftime(date_format)
            }

            response = requests.get(base_url.format(endpoint), params=params, headers=headers)

            try:
                if response.status_code == 200:
                    data = response.json()
                    if data:
                        df_temp = pd.DataFrame(data)
                        dfs.append(df_temp)
            except requests.RequestsJSONDecodeError:
                print(f"Error decoding JSON for date {current_date.strftime(date_format)}")
                # Save the erroneous response for examination
                with open("error_response.txt", "w") as file:
                    file.write(response.text)
            except Exception as e:
                print(f"Unexpected error for date {current_date.strftime(date_format)}: {e}")

            current_date += step

        df_endpoint = pd.concat(dfs, ignore_index=True)
        df_endpoint.to_csv(f'df_{endpoint}.csv', index=False)
        dfs.clear()

if __name__ == "__main__":
    extract_cat62_data()

