import smtplib
from email.message import EmailMessage


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('adithyaaaibot@gmail.com', '@diG489840')
    email = EmailMessage()
    email['From'] = 'adithyaaaibot@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'black': 'adithyaasankar2@gmail.com',
    'shiny mam': 'shiny.suresh@gmail.com'

}
