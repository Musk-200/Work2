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
   response=requests.post(url,headers=headers,data=payload,auth=("muskan.kumari@ibm.com","ATATT3xFfGF0NIqAWcR67jsu_sfpoT-1nfAHt8UsOsYTV7HTyvqJuYYm1Z3jx41l1ey1dXzVPRrp7ytyMJjObCTK5U4XTyDZnadpvzioupGy2e2kCIXackD_pjoHMFrpbx8MG7jitCbt5jmmiBHDsnjFMvo3LnIzyMski4zOyklPcUh_Pkdgk0E=F327DA2D"))
   data=response.json()
   print(response.text)