import time
from datetime import timedelta, datetime
import requests,json
import smtplib
from email.message import EmailMessage

def cowin_track(cname,cage,cpincode,cemail,cmessage):
    pincode=cpincode

    age=int(cage)

    cemail=cemail

    name=cname
    message = cmessage


    def getDate():
        tomorrow = (datetime.today() + timedelta(1)).strftime("%d-%m-%Y")
        return tomorrow


    def pincodeToStateDistrictConverter(pincode):
        district = ''
        state = ''
        india_post_url = "https://api.postalpincode.in/pincode/{pin}".format(pin = pincode)
        try:
            response = requests.get(india_post_url,headers=headers)
            parsed_response = json.loads(response.text)
            if(parsed_response[0]["Status"] == "Success"):
                district = parsed_response[0]['PostOffice'][0]['District']
                state = parsed_response[0]['PostOffice'][0]['State']
            return district,state
        except Exception as e:
            print(e)


    def getStateID(state):
        state_id = ''
        url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
        try:
            response = requests.get(url,headers=headers)
            parsed_response = json.loads(response.text)
            state_length = len(parsed_response['states'])
            for idx in range(state_length):
                if((parsed_response['states'][idx]['state_name']).lower().replace(" ", "") == state.lower().replace(" ", "")):
                    state_id = parsed_response['states'][idx]['state_id']
            return(state_id)
        except Exception as e:
            print(e)


    def getDistrictID(st_id, lookout_district):
        district_id = ''
        url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/{st}".format(st = st_id)
        try:
            response = requests.get(url,headers=headers)
            parsed_response = json.loads(response.text)
            district_length = len(parsed_response['districts'])
            for idx in range(district_length):
                if((parsed_response['districts'][idx]['district_name']).lower().replace(" ", "") == lookout_district.lower().replace(" ", "")):
                    district_id = parsed_response['districts'][idx]['district_id']
            return (district_id)
        except:
            print(gay)

    def pingCOWIN(date, district_id):
        url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district_id}&date={date}".format(district_id=district_id, date=date)
        response = requests.get(url, headers=headers)
        return json.loads(response.text)


    def checkAvailability(payload, age):
        available_centers = set()
        unavailable_centers = set()
        available_centers_str = False
        total_available_centers = 0
        if ('centers' in payload.keys()):
            length = len(payload['centers'])
            if (length > 1):
                for i in range(length):
                    sessions_len = len(payload['centers'][i]['sessions'])
                    for j in range(sessions_len):
                        if ((payload['centers'][i]['sessions'][j]['available_capacity'] > 0) and
                                (payload['centers'][i]['sessions'][j]['min_age_limit'] <= age)):
                            available_centers.add(payload['centers'][i]['name'])
                available_centers_str = ", ".join(available_centers)
                total_available_centers = len(available_centers)
        return available_centers_str, total_available_centers


    def send_mail(cemail,name,msg_body):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('invention.helpdesk@gmail.com', 'umair8999')
        email = EmailMessage()
        email['From'] = 'invention.helpdesk@gmail.com'
        email['To'] = cemail
        email['subject'] = ('INVENTION - Cowin Slot Tracker Notification')
        email.set_content('Hello ' + name + ' The slots of covid vaccine for pincode '+pincode+' of which you were have been tracking with the script on our website INVENTION. ' +message+'  So Please be in hurry and book your slot ASAP !!!. You can directly get to slot by the following info : ' +msg_body+ '  Thank you for using our service I hope you enjoyed it and finds it beneficial. Thats all we want and please do share our site as much as possible if you really appreciate our work :) , Regards Umair Nizam.')
        print("yes")
        server.send_message(email)




    headers = \
        {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}


    if(pincode!=0):
        PINCODE = pincode
        print("Pincode: ", PINCODE)
        dist, state = pincodeToStateDistrictConverter(PINCODE)
        if (state != "" and dist != ""):
             print("District: {d}\nState: {s}".format(d=dist, s=state))
             st_id = getStateID(state)
             print("State ID: ", st_id)
             if (st_id != ""):
                DISTRICT_ID = getDistrictID(st_id, dist)
                print("District ID: ", DISTRICT_ID)
                flag = True


    if (flag):
        while (True):
            date = getDate()
            data1 = pingCOWIN(date, DISTRICT_ID)
            available, total_centers = checkAvailability(data1, age)
            if available:
                msg_body = "Slots Available at {total} places.\n{available}".format(total=total_centers,available=available)
                print(msg_body)
                send_mail(cemail, name, msg_body)
                break
            else:
                print("No Available Centers")


    else:
        print("District id or pincode error. Check settings")
        print("Arguments Missing/Invalid. Check settings.json")
        time.sleep(1800)
        cowin_track(cname, cage, cpincode, cemail, cmessage)
