from django.shortcuts import render, redirect, reverse
from . models import Amazon, Flipkart, Cowin, Help, Register, Verify
import smtplib
from email.message import EmailMessage
from .first import check_price
from .second import damn_price
from.cowin import cowin_track
from .otp import send_otp , num

# Create your views here.

def index(request):
    return render(request,"index.html")

def script(request):
    return render(request,"script.html")

def first(request):
    return render(request,"first.html")

def second(request):
    return render(request,"second.html")

def third(request):
    return render(request,"third.html")

def privacypolicy(request):
    return render(request,"privacypolicy.html")

def termsofservice(request):
    return render(request,"termsofservice.html")

def aboutus(request):
    return render(request,"aboutus.html")

def contactus(request):
    return render(request,'contactus.html')

def nigga(request):
    return render(request,'registration.html')

def register(request):
    rname=request.POST['rname']
    rage=request.POST['rage']
    rcontact=request.POST['rcontact']
    remail=request.POST['remail']
    raddress=request.POST['raddress']
    re=Register(rname=rname,rage=rage,rcontact=rcontact,remail=remail,raddress=raddress)
    re.save()
    sv=Verify(num=num)
    sv.save()
    send_otp(rname,remail)
    return render(request,'thanks.html')

def verify(request):
    rotp=request.POST['rotp']
    print("yes")
    rotp=int(rotp)
    ob=int(num)
    print(ob)
    if(rotp==ob):
        msg="Thank You we have successfully registered yo with us"+"You can download Source code from this link : https://mega.nz/folder/dmgizSgD#y3HV8gQHdcjE5JkgWDxfsA"
        print("done")
    else:
        msg="Invalid OTP Please Try Again"
    return render(request,"registration.html",{'msg':msg})

def amazon(request):
    name=request.POST['name']
    sender=request.POST['sender']
    url=request.POST['url']
    arate=request.POST['arate']
    message=request.POST['message']
    am=Amazon(name=name,sender=sender,url=url,arate=arate,message=message)
    am.save()
    check_price(name,url,arate,sender,message)
    msg=("Thank you "+name+", We will notify you when price drops ASAP!!!")
    return render(request, "first.html", {'msg': msg})


def flipkart(request):
    fname=request.POST['fname']
    femail=request.POST['femail']
    furl=request.POST['furl']
    fprice=request.POST['fprice']
    fmessage=request.POST['fmessage']
    fk=Flipkart(fname=fname,femail=femail,furl=furl,fprice=fprice,fmessage=fmessage)
    fk.save()
    damn_price(fname,furl,fprice,femail,fmessage)
    msg=("Thank you "+fname+", We will notify you when price drops ASAP!!!")
    return render(request,"second.html",{'msg':msg})

def cowin(request):
    cname=request.POST['cname']
    cemail=request.POST['cemail']
    cage=request.POST['cage']
    cpincode=request.POST['cpincode']
    cmessage=request.POST['cmessage']
    co=Cowin(cname=cname,cemail=cemail,cage=cage,cpincode=cpincode,cmessage=cmessage)
    co.save()
    cowin_track(cname, cage, cpincode, cemail, cmessage)
    msg = ("Thank you " + cname + ", We will notify you when price drops ASAP!!!")
    return render(request, "third.html", {'msg': msg})

def help(request):
    hname=request.POST['hname']
    hemail=request.POST['hemail']
    hsubject=request.POST['hsubject']
    hmessage=request.POST['hmessage']
    he=Help(hname=hname,hemail=hemail,hsubject=hsubject,hmessage=hmessage)
    he.save()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('invention.helpdesk@gmail.com', 'umair8999')
    email = EmailMessage()
    email['From'] = 'invention.helpdesk@gmail.com'
    email['To'] = 'helpdesk.invention@gmail.com'
    email['subject'] = hsubject
    email.set_content('Name : '+hname+'Sender email '+hemail+'Query message '+hmessage)
    server.send_message(email)
    msg = ("Thank you " + hname + ", We will contact you ASAP!!!")
    return render(request, "contactus.html", {'msg': msg})
