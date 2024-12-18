import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailClient:
    def __init__(self, smtp_server, imap_server, email_address, password):
        self.smtp_server = smtp_server
        self.imap_server = imap_server
        self.email_address = email_address
        self.password = password

    def send_message(self, subject, recipients, message):
        msg = MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        with smtplib.SMTP(self.smtp_server, 587) as ms:
            ms.ehlo()
            ms.starttls()
            ms.ehlo()
            ms.login(self.email_address, self.password)
            ms.sendmail(self.email_address, recipients, msg.as_string())

    def receive_email(self, header=None):
        with imaplib.IMAP4_SSL(self.smtp_server) as mail:
            mail.login(self.email_address, self.password)
            mail.list()
            mail.select("inbox")
            criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
            result, data = mail.uid('search', None, criterion)

            if data[0] is None:
                raise Exception('There are no letters with current header')

            latest_email_uid = data[0].split()[-1]
            result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_string(raw_email)

            return email_message


if __name__ == "__main__":
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    l = 'login@gmail.com'
    passwORD = 'qwerty'

    email_client = EmailClient(GMAIL_SMTP, GMAIL_IMAP, l, passwORD)

    # Отправка письма
    email_client.send_message(
        recipients=['vasya@email.com', 'petya@email.com'],
        subject='Subject',
        message='Message'
    )

    # Получение письма
    try:
        received_email = email_client.receive_email()
        print(f'Received email: {received_email}')
    except Exception as e:
        print(e)
