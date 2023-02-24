# do this step before sending email otherwise your can,t be send
# 1:go to over your gmail account and set 2 step-verification
# 2: generate app password
# 3: create a function to send email


# setup a secure connection using  SMTP_SSL AND .STARTTLS
# use python built-in smtplib library to send basic email
# if you want to send fancy email (with html content and attachment ) use email packages
#########################################################################################

# Fancy Email : if you want to images, hyperlink, responsive content then html comes in very handy
# Today most common types of email is of MIME(multipupose internet mail extension)
# Multipart email , combing html and plantext ,
# MIME message are handle by pythons "email.mime" moduel



# import neccessary library for Email sending

# EmailMessage is a package that built our email(Email_sender, Email_receiver, Email_subjecct, Email_body)
from passwordStoreHere import password, My_Email
from email.mime.text import MIMEText                #MIMETEXt()--> instance/object will contain HTML and plain-text of our message
from email.mime.multipart import MIMEMultipart      #MIMEMulipart('alternative')-->instance/object comibes these into a
                                                        # single message with two alternative rendering option
from Project.Html_content_for_verification import html
import ssl
import smtplib




email_sender ="isrardawar485@gmail.com"
email_password = password
email_receiver = My_Email
# for ssl:
port =  465
email_subject = "Please verify your Email address"
email_body = """Please verify your email for successful login"""
smtp_server = 'smpt.gmail.com'


# mememulipart --> instance/object cominbes these into a single message
mememulitpart = MIMEMultipart('alternative')
mememulitpart['From'] = email_sender
mememulitpart['To'] = email_receiver
mememulitpart['subject'] = email_subject

# create hmtl content and plain text for our message

text = """\
Please verify your email"""
html = html

# Hmtl content/ plaintext --> turn into MIMETEXT object/instance
plaintext = MIMEText(text, 'plain')
htmlcontent = MIMEText(html, 'html')

# Add html content and plain text part into MIMEMultipart message
# email client will try to render the last part
mememulitpart.attach(plaintext)
mememulitpart.attach(htmlcontent)




# Create Secure SSl context
context = ssl.create_default_context()

# login to our email and send email to receiver
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_receiver, mememulitpart.as_string())