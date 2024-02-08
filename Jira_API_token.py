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
   response=requests.post(url,headers=headers,data=payload,auth=("muskan.kumari@ibm.com","ATATT3xFfGF0Z0MnmIOXuiDwP-LHr2hM0hNBJ2-pCNYc0-we7SNCHbo4H2zmAv3qbfeJav6CRDxBiAvbTBgiOPL_CpSAKaTx0Xig7JkE7JVvBG2pM1pp6K3UOg1RbYvPIglT3aL9d4PnMV45LSqQEY4MYK65Nf8H1MJKUqjdoD5rDQKSlQPXj3U=38CE73EB"))
   data=response.json()
   print(data["response.text"])