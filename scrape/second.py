import smtplib
from email.message import EmailMessage
import requests
from bs4 import BeautifulSoup
import time

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}

def damn_price(fname,furl,fprice,femail,fmessage):
    page = requests.get(furl, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    time.sleep(5)
    title = soup.find(class_="B_NuCI").get_text()
    time.sleep(5)
    try:
        price = soup.find(class_="_30jeq3 _16Jk6d").get_text()
        time.sleep(5)
        print(price)
    except:
        price=("00,00")
        print("Price not available")
        time.sleep(5)
    chck = price.replace(',', '')
#chc = chck.replace('.', '')
#ch = chc.replace('00', '')
    c = chck.replace('₹', '')
    c = int(c)
    fname = fname.upper()
    rate = int(fprice)
    try:
        if (c < rate):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('invention.helpdesk@gmail.com', 'umair8999')
            email = EmailMessage()
            email['From'] = 'invention.helpdesk@gmail.com'
            email['To'] = femail
            email['subject'] = ('INVENTION - Price has Dropped Of Your Product  '+title)
            email.set_content('Hello ' + fname + ' the price of your product ' + title + ' of which you were have been tracking with the script on our website INVENTION has came down at the price you wanted it to buy. ' + fmessage + '  So Please be in hurry and buy it ASAP !!!. You can directly get to product page by the following link : ' + furl + '  Thank you for using our service I hope you enjoyed it and finds it beneficial. Thats all we want and please do share our site as much as possible if you really appreciate our work :) , Regards Umair Nizam.')
            print("yes")
            server.send_message(email)


    except:
        print('no deal')
        time.sleep(3600)
        damn_price(fname, furl, fprice, femail, fmessage)