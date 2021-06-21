import smtplib
from email.message import EmailMessage
import requests
from bs4 import BeautifulSoup
import time


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}

def check_price(name,url,arate,sender,message):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    time.sleep(5)
    title = soup.find(id="productTitle").get_text()
    time.sleep(5)
    try:
        price = soup.find(id="priceblock_dealprice").get_text()
        time.sleep(5)
    except:
        price = soup.find(id="priceblock_ourprice").get_text()
        time.sleep(5)
    chck = price.replace(',', '')
    chc = chck.replace('.', '')
    ch = chc.replace('00', '')
    c = ch.replace('₹', '')
    c = int(c)
    aname = name.upper()
    rate = int(arate)
    print(price)
    print(title)
    if (c < rate):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('invention.helpdesk@gmail.com', 'umair8999')
        email = EmailMessage()
        email['From'] = 'invention.helpdesk@gmail.com'
        email['To'] = sender
        email['subject'] = ('INVENTION - Price has Dropped Of Your Product  ')
        email.set_content('Hello ' + aname + ' the price of your product ' + title + ' of which you were have been tracking with the script on our website INVENTION has came down at the price you wanted it to buy. ' + message + '  So Please be in hurry and buy it ASAP !!!. You can directly get to product page by the following link : ' + url + '  Thank you for using our service I hope you enjoyed it and finds it beneficial. Thats all we want and please do share our site as much as possible if you really appreciate our work :) , Regards Umair Nizam.')
        print("yes")
        server.send_message(email)
    else:
        print('no deal')
        time.sleep(3600)
        check_price(name,url,arate,sender,message)