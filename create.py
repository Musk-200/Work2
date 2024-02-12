from jira import JIRA
import requests 
import json
import sys 
from requests.auth import HTTPBasicAuth
from jira import JIRA, JIRAError
from jira.exceptions import JIRAError




def generate_issue(json_obj):
   url="https://ibm-team-uz9mmme2.atlassian.net//rest/api/2/issue"
   headers={
     "Accept": "application/json",
     "Content-Type": "application/json"
}
   payload=json.dumps(
   {
      "fields": {
         "project":
         {
            "key": "JN"
         },
         "summary": json_obj['title'] ,
         "description": json_obj['description'] ,
         "issuetype": {
            "name": json_obj['issuetype']
         } ,
         "priority": {
            "name" : json_obj['Priority']
          } ,
          "labels": ["patch_750UP7IF04"]
      }
   }
   )
   response=requests.post(url,headers=headers, data=payload, auth=("muskan.kumari@ibm.com","ATATT3xFfGF0EiI0DiJCqvm6KS0Npwr51fLKxlLvX5VgB8jlRADoEIS3AB6cBZcpYehvLxS0rH3Ogr-fJBHIByAZvwkG-V8wY2Lme_jn57SORc-DVFDFhIL4jlTiUQoOmZ8NUa4k4PbrK8KyXd8iQAsSIzrukVke59oJkMGsawjl737WKrR1-R8=86F72FFE"))
   data=response.json()
   print(response.text)
   print ('Issue generated successfully')
    
   

def get_authenticated(response):
    if response.status_code == 200:
      print ('Data retrieved successfully')
      print (response.status_code)
      return response.status_code

    else:
      print('Error retrieving data:', response.text)

# def check_issuetype(jira_obj,json_obj):
#     if(issue_type == "story"):
#         new_issue = jira_obj.generate_issue(json_obj)
#     elif(issue_type == "epic"):
#         new_issue = jira_obj.generate_issue(json_obj)
#     elif(issue_type == "bug"):
#         new_issue = jira_obj.generate_issue(json_obj)
#     elif(issue_type == "task")
#         new_issue = jira_obj.generate_issue(json_obj)

#     jira_obj.assign_issue(new_issue, None)
      
'''' Function  posting notification on slack'''


def post_slack_notification( json_data):
    slack_message = {"text": f"New jira issue has been created\n Key :{json_data['title']}\n Summary: {json_data['description']}"}

    try:
        webhook_url = "https://ibm.slack.com/team/U06B63UAKAS"    
        response = requests.post(webhook_url, data=json.dumps(slack_message), headers={'Content-Type': 'application/json'})

        if response.status_code == 200:
            print("Slack notification sent successfully.")
        else:
            print(f"Failed to send Slack notification. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error sending Slack notification: {str(e)}")



def main():
    # print ("Generating JIRA issue from the JSON data")
    # Authenticate to the JIRA server
    email = "mskan.kumari@ibm.com"
    api_key = "ATATT3xFfGF0EiI0DiJCqvm6KS0Npwr51fLKxlLvX5VgB8jlRADoEIS3AB6cBZcpYehvLxS0rH3Ogr-fJBHIByAZvwkG-V8wY2Lme_jn57SORc-DVFDFhIL4jlTiUQoOmZ8NUa4k4PbrK8KyXd8iQAsSIzrukVke59oJkMGsawjl737WKrR1-R8=86F72FFE"
    # JIRA_ISSUE_TYPE = "Task"
    # jira_obj = JIRA(url,(email, api_key))
    url1= "https://ibm-team-uz9mmme2.atlassian.net/jira/servicedesk/projects/JN/queues/custom/1"
    response = requests.get(url1, auth = HTTPBasicAuth(email,api_key))
     
     # validating the response for the request made
    
    '''if response.status_code == 200:
      print ('Data retrieved successfully')

    else:
      print('Error retrieving data:', response.text)'''
    
    json_obj= get_authenticated(response)
    print(json.dumps(json_obj,indent=3))


    #  Taking values of different fields for creating jira issue from the programmer
    
    json_data = {'title': 'Sample Issue', 'description': 'This is a sample issue.', 'issuetype': 'Task' , 'Priority': 'High'}
         
    # generating new issue on jira taking all the information and passing under the given function

    generate_issue(json_data)

    # posting notification on slack about the generation of new jira issue

    post_slack_notification(json_data)

    # new_issue = check_issuetype(jira_obj, json_obj)

if __name__=="__main__": 
    main()






   
   
   
  
  