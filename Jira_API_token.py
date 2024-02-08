import requests
import json
import pandas as pd
# read by default 1st sheet of an excel file
df = pd.read_excel('Customer_And_Components_Name.xlsx')
print(df)
url="https://ibm-team-uz9mmme2.atlassian.net//rest/api/2/issue"
headers={
    "Accept": "application/json",
    "Content-Type": "application/json"
}
for index, row in df.iterrows(0,9):
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
   response=requests.post(url,headers=headers,data=payload,auth=("muskan.kumari@ibm.com","ATATT3xFfGF0uFCv02vcXggFqjNvvhAaozymJrShRLW2nrmBnzUZ1gLyl4X1AIq3pD9hRmWPDJogbufjbLSwQCfIVD8MV-DrJtXg4-9M4JqTrIKhPFWxnwNaoBlkNIy7vjR_mAOXE-pLmZvzYVpUCaC1Svt6awnHiSFA4wi0xCqjYnml2zf2Uuk=9121D468"))
   data=response.json()
   print(data["id"])