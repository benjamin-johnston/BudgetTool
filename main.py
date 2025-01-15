import os
from dotenv import load_dotenv

from googleapiclient.discovery import build

from auth import authenticate
from email_util import get_emails
from sheets import write
from parser import CapitalOneParser, ChaseParser

load_dotenv()

# Define scopes for Gmail and Google Sheets
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/spreadsheets"
]

def main():
    creds = authenticate(SCOPES)

    gmail_service = build("gmail", "v1", credentials=creds)
    sheets_service = build("sheets", "v4", credentials=creds)

    capitalone_query = 'from:notification.capitalone.com subject:"A new transaction was charged to your account" newer_than:14d'
    capitalone_data = get_emails(gmail_service, CapitalOneParser(), capitalone_query)
    write(sheets_service, capitalone_data, os.getenv("CAPITAL_ONE_SPREADSHEET_ID"))

    chase_query = 'from:no.reply.alerts@chase.com subject:"Your $" subject:"transaction with" newer_than:14d'
    chase_data = get_emails(gmail_service, ChaseParser(), chase_query)
    write(sheets_service, chase_data, os.getenv("CHASE_SPREADSHEET_ID"))
if __name__ == "__main__":
    main()
