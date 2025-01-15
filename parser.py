import re
from datetime import datetime
from abc import ABC, abstractmethod

class EmailParser(ABC):
    """
    Abstract base class for email parsing functions.
    All parsers must implement the `parse` method with the defined signature.
    """

    @abstractmethod
    def parse(self, subject, sender, email_date, body):
        """
        Parse email data.
        Args:
            subject (str): The email subject.
            sender (str): The email sender.
            date (str): The email date (formatted as MM/dd/yyyy).
            body (str): The plain text body of the email.

        Returns:
            dict: Parsed data.
        """
        pass

class CapitalOneParser(EmailParser):
    def parse(self, subject, sender, email_date, body):
        regex = (
                r"As requested, we're notifying you that on ([A-Za-z]+\s\d{1,2},\s\d{4}), at ([A-Za-z0-9\s\-#\*\.,&/()!@':]+), "
                r"a pending authorization or purchase in the amount of \$(\d+\.\d{2}) was placed or charged on your Quicksilver Credit Card\."
            )

        # Search for the pattern in the email body
        match = re.search(regex, body)

        try:
            parsed_date = datetime.strptime(email_date, "%a, %d %b %Y %H:%M:%S %z").strftime("%m/%d/%Y")
        except ValueError:
            parsed_date = email_date

        if match:
            date = match.group(1)         
            store_name = match.group(2)   
            amount_str = match.group(3)       

            print(f"Date: {date}")
            print(f"Store Name: {store_name}")
            print(f"Amount: ${amount_str}")

            amount = float(amount_str)

            return [parsed_date, store_name, amount]
        else:
            print("No match found.")
            return [parsed_date, subject, sender]
        
class ChaseParser(EmailParser):
    def parse(self, subject, sender, email_date, body):      
        regex = r"Your \$(\d+\.\d{2}) transaction with (.+)"

        match = re.match(regex, subject)

        try:
            parsed_date = datetime.strptime(email_date, "%a, %d %b %Y %H:%M:%S %z (%Z)").strftime("%m/%d/%Y")
        except ValueError:
            parsed_date = email_date
        

        if match:
            amount_str = match.group(1)
            store_name = match.group(2)
            
            print(f"Store Name: {store_name}")
            print(f"Amount: {amount_str}")

            amount = float(amount_str)

            return [parsed_date, store_name, amount]
        else:
            print("No match found.")
            return [parsed_date, subject, sender]
            
