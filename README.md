# Email Parser Application

This application parses email push notifications from credit card companies and writes the extracted data to Google Sheets.

## Prerequisites

- Python 3.6 or higher
- Access to the [Google Cloud Console](https://console.cloud.google.com/)
- Google account with Gmail and Google Sheets access

## Setup Instructions

### 1. Create a Google Cloud Project

1. Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
2. Click on the project dropdown at the top of the page and select "New Project".
3. Enter a project name and click "Create".

### 2. Enable the Gmail and Sheets APIs

1. In the [Google Cloud Console](https://console.cloud.google.com/), navigate to **APIs & Services** > **Library**.
2. Search for "Gmail API" and click on it.
3. Click "Enable" to activate the Gmail API for your project.
4. Repeat the above steps for the "Google Sheets API".

### 3. Configure the OAuth Consent Screen

1. In the [Google Cloud Console](https://console.cloud.google.com/), navigate to **APIs & Services** > **OAuth consent screen**.
2. Select the user type that best fits your application (e.g., **External** for apps used by users outside your organization).
3. Fill in the required fields, such as **App name**, **User support email**, and **Developer contact information**.
4. Click "Save and Continue".
5. If your app requires specific scopes, add them in the **Scopes** section.
6. For external applications, add test users in the **Test users** section.
7. Review and finalize the consent screen configuration.

### 4. Create OAuth Client ID and Download Credentials

1. In the [Google Cloud Console](https://console.cloud.google.com/), navigate to **APIs & Services** > **Credentials**.
2. Click on "Create Credentials" and select "OAuth client ID".
3. Choose "Desktop app" as the application type.
4. Enter a name for the client ID and click "Create".
5. After creation, a dialog will appear with your **Client ID** and **Client Secret**. Click "OK".
6. Locate the newly created OAuth 2.0 Client IDs in the credentials list and click the download icon to save the JSON file to your computer.
7. Rename the file to client_secret.json and add it to the project


## Running the Application

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the application
   ``` python main.py

## Notes

- **Gmail Account Permissions**: Ensure that the Gmail account you use has the necessary permissions to access and read emails. This is crucial for the application to function correctly.

- **Google Sheets API Access**: The Google Sheets API requires access to the specific spreadsheet where data will be written. Make sure the appropriate permissions are granted to allow data writing operations.

- **OAuth Client Credentials Security**: Keep your OAuth client credentials secure and do not share them publicly. Exposing these credentials can lead to unauthorized access to your Google services.

For more detailed information, refer to the official Google Cloud documentation:

- [Configure the OAuth consent screen and choose scopes](https://developers.google.com/workspace/guides/configure-oauth-consent)

- [Create access credentials](https://developers.google.com/workspace/guides/create-credentials)

- [Enable Google Workspace APIs](https://developers.google.com/workspace/guides/enable-apis)



