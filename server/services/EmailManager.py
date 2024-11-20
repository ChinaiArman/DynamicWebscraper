"""
"""

# IMPORTS
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


# EMAIL MANAGER CLASS
class EmailManager:
    """
    Handles email operations using Gmail SMTP
    """
    def __init__(self, email_address: str, email_password: str, client_url: str):
        """
        Initialize EmailManager with Gmail credentials
        
        Args:
            gmail_user (str): Gmail email address
            gmail_password (str): Gmail app password
            client_url (str): Base URL of your application
        """
        self.email_address = email_address
        self.email_password = email_password
        self.client_url = client_url

    def send_verification_email(self, to_email: str, username: str, verification_code: str) -> None:
        """
        Send verification email with confirmation link
        
        Args:
            to_email (str): Recipient's email address
            username (str): Username of the new user
            verification_code (str): Verification code for the user
        """
        msg = MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = to_email
        msg['Subject'] = "DynamicWebscraper Verification"
        
        # Ensure we're using the React app URL
        body = f"""
        Hello {username},

        Thank you for creating an account with DynamicWebscraper. 

        Your one time verification code is: {verification_code}

        To verify your account, please click the link below:

        {self.client_url}/verify

        Note: If you did not request this account, please ignore this email.

        Best regards,
        DynamicWebscraper Team
        """
        msg.attach(MIMEText(body, 'plain'))
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(self.email_address, self.email_password)
            server.send_message(msg)
            server.close()
        except Exception as e:
            raise Exception(f"Failed to send email: {str(e)}")
        
    def forgot_password_email(self, to_email: str, reset_code: str) -> None:
        """
        """
        msg = MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = to_email
        msg['Subject'] = "DynamicWebscraper Password Reset"
        
        body = f"""
        Hello,

        You have requested to reset your password at DynamicWebscraper.

        Your one time reset code is: {reset_code}

        Note: If you did not request this reset, please ignore this email.

        Best regards,
        DynamicWebscraper Team
        """
        msg.attach(MIMEText(body, 'plain'))
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(self.email_address, self.email_password)
            server.send_message(msg)
            server.close()
        except Exception as e:
            raise Exception(f"Failed to send email: {str(e)}")
