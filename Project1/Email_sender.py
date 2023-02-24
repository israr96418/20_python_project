# do this step before sending email otherwise your can,t be send
# 1:go to over your gmail account and set 2 step-verification
# 2: generate app password
# 3: create a function to send email


# setup a secure connection using  SMTP_SSL AND .STARTTLS
# use python built-in smtplib library to send basic email
# if you want to send fancy email (with html content and attachment ) use email packages
#########################################################################################

# import neccessary library for Email sending

# EmailMessage is a package that built our email(Email_sender, Email_receiver, Email_subjecct, Email_body)
from email.message import EmailMessage
from passwordStoreHere import password,My_Email
import ssl
import smtplib




email_sender ="isrardawar485@gmail.com"
email_password = password
email_receiver = "macok89993@ezgiant.com"
# for ssl:
port =  465
email_subject = "Request for subscribtion"
email_body = """If you link my video please subscribe my channel"""
smtp_server = 'smtp.gmail.com'


# Create instance/object of EmailMessage
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = email_subject
em.set_content(email_body)

# Create Secure SSl context
context = ssl.create_default_context()

# login to our email and send email to receiver
with smtplib.SMTP_SSL(smtp_server, port, context=context) as smpt:
    smpt.login(email_sender, email_password)
    smpt.sendmail(email_sender, email_receiver, em.as_string())