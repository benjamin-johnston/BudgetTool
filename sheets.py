# Google Sheet details
RANGE_NAME = "Sheet1!A1"

def write(service, data, sheet):
    # Append to the Google Sheet
    body = {"values": data}
    service.spreadsheets().values().append(
        spreadsheetId=sheet,
        range=RANGE_NAME,
        valueInputOption="RAW",
        body=body
    ).execute()

    print("Data written to Google Sheet.")