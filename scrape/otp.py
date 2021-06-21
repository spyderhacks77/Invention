import smtplib
from email.message import EmailMessage
import random

n = random.random()
nu = (n * 100000000)
t=int(nu)
num=str(t)
num = (num[0:6])

def send_otp(rname,remail):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('invention.helpdesk@gmail.com', 'umair8999')
    email = EmailMessage()
    email['From'] = 'invention.helpdesk@gmail.com'
    email['To'] = remail
    email['subject'] = ('INVENTION - OTP For Registration Confirmation !!! ')
    email.set_content('Hello ' + rname + 'Your OTP for Verification of Registration is : '+num+' \n\nWe trust you have had a great day so far! \n\nCongratulations! You have been registered successfully in Invention!\n'
        'Our team will contact ASAP to inform you about further formalities!\n Stay healthy and safe! All the best! :) \n'
        'Have a fabulous day ahead! \n\n' '  Thank you for registering with our service I hope you will enjoy it and finds it beneficial.\n Thats all we want and please do share our site as much as possible if you really appreciate our work :) , \n Regards Umair Nizam.')
    print("yes")
    server.send_message(email)