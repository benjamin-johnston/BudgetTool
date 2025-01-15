import base64
from datetime import datetime
from parser import EmailParser

def get_emails(gmail_service, parser: EmailParser, query=""):
    """
    Search for emails in Gmail matching the given query.
    """
    results = gmail_service.users().messages().list(userId="me", q=query).execute()
    messages = results.get("messages", [])
    email_data = []

    for message in messages:
        msg = gmail_service.users().messages().get(userId="me", id=message["id"]).execute()
        payload = msg["payload"]
        headers = payload.get("headers", [])
        
        # Extract subject and sender from headers
        subject = next((header["value"] for header in headers if header["name"] == "Subject"), "No Subject")
        sender = next((header["value"] for header in headers if header["name"] == "From"), "Unknown Sender")
        date = next((header["value"] for header in headers if header["name"] == "Date"), "Unknown Date")
        
        # Decode body content (plain text if available)
        body = extract_body(payload)

        parsed_data = parser.parse(subject, sender, date, body)
        email_data.append(parsed_data)

    email_data.reverse()

    return email_data

def extract_body(payload):
    body = ""
    if "parts" in payload:
        for part in payload["parts"]:
            if part["mimeType"] == "text/plain" and "data" in part["body"]:
                body = base64.urlsafe_b64decode(part["body"]["data"]).decode("utf-8")
                break
    elif "body" in payload and "data" in payload["body"]:
        body = base64.urlsafe_b64decode(payload["body"]["data"]).decode("utf-8")
    return body

