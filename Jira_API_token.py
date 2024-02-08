import requests
import json
import pandas as pd
# read by default 1st sheet of an excel file
df = pd.read_excel('Book3.xlsx')
print(df)
url="https://ibm-team-uz9mmme2.atlassian.net//rest/api/2/issue"
headers={
    "Accept": "application/json",
    "Content-Type": "application/json"
}
for index, row in df.iterrows():
   user_issue = row['Components']
   user_description = row['Customer_name']
   payload=json.dumps(
   {
      "fields": {
         "project":
         {
            "key": "JN"
         },
         "summary": user_issue ,
         "description": user_description,
         "issuetype": {
            "name": "Task"
         }
      }
   }
   )
   response=requests.post(url,headers=headers,data=payload,auth=("muskan.kumari@ibm.com","ATATT3xFfGF003rEHb0o0ENunjYcuvCqCXoJVFr9rl295r4YghXs0WgKkIZgcnl2D-q0yucpuYMjRnYgcLYeCGzHYJNDPRBjoFlIJRHyhi6Od_H6bewKlaFSY5bH8f2B1cMOLMhoiSu0yqxzli_3VIr4x9of6cy5EJ_N71IA8rGWRWprCYVmE9Q=A63757C6"))
   data=response.json()
   print(data[response.text])