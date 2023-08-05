import logging
import smtplib
from email.message import EmailMessage


class SenderConfig:
    def __init__(self, config, format=None):
        self.config = {key.lower(): value for key, value in config.items()}
        self.logger = logging.getLogger('Sending Email')
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        self.format = format

    def send_email(self, body, recipients, subject=None, header=None, footer=None, sender=None, format=None):
        email = EmailMessage()
        email['Subject'] = subject or self.config['subject']
        email['From'] = sender or self.config['sender']
        email['To'] = recipients
        head = (header or self.config['header']) + "\n\n"
        foot = "\n\n" + (footer or self.config['footer'])
        if (str(self.format).lower() == "html"):
            message = f'''
                    <!DOCTYPE html>
                    <html>
                        <body>
                            <div>
                                <div>
                                    <div style="text-align:left;">
                                        <h3 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;">{str(head)}</h3>
                                        <br>
                                        <p>{str(body)}</p>
                                        <br>
                                        <h4>{str(foot)}</h4>
                                    </div>
                                </div>
                            </div>
                        </body>
                    </html>
                    '''
            email.set_content(message, subtype='html')
        elif format == "custom":
            message = body
            email.set_content(message)
        else:
            message = str(head + body + foot)
            email.set_content(message)

        try:
            with smtplib.SMTP(self.config['server'], self.config['port']) as smtp:
                if self.config.get('username') and self.config.get('password'):
                    smtp.login(self.config['username'],
                               self.config['password'])
                smtp.send_message(email)
            self.logger.info("Email sent successfully!")
        except smtplib.SMTPException as e:
            self.logger.error(f"Error sending email: {str(e)}")


config = {
    'EmailConfig': {
        "Server": "smtp-relay.brevo.com",
        "Port": "587",
        "Username": "datalakealert@gmail.com",
        "Password": "qACM2wgT7QnmRcLU",
        "sender": "sample@email.com",
        'subject': "Hello from the SenderConfig module!",
        'header': "<strong>Error Alert</strong> from the AgriSompo Data Lake Processing System:",
        'footer': "This is the footer"
    }
}
