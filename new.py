import urllib.request
import requests 
import sys
import json
import base64
import os
import datetime

# Jira settings
JIRA_URL = "https://ibm-team-uz9mmme2.atlassian.net"

JIRA_USERNAME = "muskan.kumari@ibm.com"
JIRA_PASSWORD = "" # For Jira Cloud use a token generated here: https://id.atlassian.com/manage/api-tokens

JIRA_PROJECT_KEY = "TEST"
JIRA_ISSUE_TYPE = "Story"


def jira_rest_call(data):

    # Set the root JIRA URL, and encode the username and password
    url = JIRA_URL + '/rest/api/2/issue'
    base64string = base64.encodestring('%s:%s' % (JIRA_USERNAME, JIRA_PASSWORD)).replace('\n','')

    # Build the request
    restreq = requests(url)
    restreq.add_header('Content-Type', 'application/json')
    restreq.add_header("Authorization", "Basic %s" % base64string)

    # Send the request and grab JSON response
    response = urllib.request.urlopen(restreq, data)

    # Load into a JSON object and return that to the calling function
    return json.loads(response.read())


def generate_summary():
    return "Summary - " + '{date:%Y-%m-%d %H:%M}'.format(date=datetime.datetime.now())


def generate_description(data):
    return data


def generate_issue_data(summary, description):
    # Build the JSON to post to JIRA
    json_data = '''
    {
        "fields":{
            "project":{
                "key":"%s"
            },
            "summary": "%s",
            "issuetype":{
                "name":"%s"
            },
            "description": "%s"
        } 
    } ''' % (JIRA_PROJECT_KEY, summary, JIRA_ISSUE_TYPE, description)
    return json_data

def main() :
  print ("Creating Jira issue exacting features from the json file")
  json_response = jira_rest_call(generate_issue_data(generate_summary(), generate_description("TEST DESCRIPTION")))
  issue_key = json_response['key']
  print ("Created issue "), issue_key
