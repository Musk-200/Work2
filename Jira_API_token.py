import requests
import json
import pandas as pd
# read by default 1st sheet of an excel file
df = pd.read_excel('Untitled spreadsheet.xlsx')
print(df)
df= df.drop('UserId', axis = 1)
url="https://ibm-team-uz9mmme2.atlassian.net//rest/api/2/issue"
headers={
    "Accept": "application/json",
    "Content-Type": "application/json"
}
for index, row in df.iterrows():
   user_issue = row['UserName']
   user_description = row['User_location']
   payload=json.dumps(
   {
      "fields": {
         "project":
         {
            "key": "TUA"
         },
         "summary": user_issue ,
         "description": user_description,
         "issuetype": {
            "name": "Task"
         }
      }
   }
   )
   response=requests.post(url,headers=headers,data=payload,auth=("muskan.kumari@ibm.com","ATATT3xFfGF07mPLpPoNcUU91HNt3kZ34FPgXpDULINWmMIk3vCCcfNxt8TLAE0Zo3Lkxsd1bx1EeWI7ngHZ6IpKqxUIy8YVdQuWVtHC6HXURhLxrZEWJpXIzWsj3FQJwuZF4R4CwPSltrll6ReTOJvPmxPBn2lWywvAsUHrEm9XG5G4yHsb1fs=5672298C"))
   data=response.json()
   print(data["id"])