import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from dotenv import load_dotenv

load_dotenv()

def authenticate(scopes):
    """
    Authenticate and return credentials for Gmail and Google Sheets without running a local server.
    """
    creds = None
    # Check if the token file exists
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", scopes)
    
    # If no valid credentials, perform authentication
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Refresh the token using an HTTP request
            creds.refresh(Request())
        else:
            # Perform manual console-based authentication
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secret.json", scopes, redirect_uri=None
            )

            creds = flow.run_local_server(port=8082)
        # Save the credentials for the next run
        with open("token.json", "w") as token_file:
            token_file.write(creds.to_json())
    
    return creds