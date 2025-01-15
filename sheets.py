def write(service, data, sheet, range="Sheet1!A1"):
    # Append to the Google Sheet
    body = {"values": data}
    service.spreadsheets().values().append(
        spreadsheetId=sheet,
        range=range,
        valueInputOption="RAW",
        body=body
    ).execute()

    print("Data written to Google Sheet.")