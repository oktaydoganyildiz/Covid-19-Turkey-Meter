from datetime import date,timedelta
import smtplib
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://covid19.saglik.gov.tr/TR-66935/genel-koronavirus-tablosu.html")
a=browser.find_elements_by_id("TumVerileriGetir")
list=[ ]
for i in a:
    a=(i.text.split(" "))
    list.append(i.text)


tarih= str(a[ 0])+str(a[1])+str(a[2])
today_vaka= a[ 9]
today_death=a[ 11]
toplam_tr_hasta=a[ 4]
time.sleep(5)
today = date.today()-timedelta(days=1)

def sendingmail():
    gmail_user = "" #Adress
    gmail_password = "" #Password

    sent_from = gmail_user
    to = [""] #To adress
    subject = "asdasdasd"
    body = f"""


       Bugunun Tarihi : {str(today)}
       Bugun Covid-19 Vaka Sayisi: {str(today_vaka)}
       Bugun Olum Sayisi : {str(today_death)} 
       Toplam Turkiye'deki Hasta Sayisi: {str(toplam_tr_hasta)}
       
       
Saygilar Robot,  """


    email_text = """\
    From: %s
    To: %s
    Subject: 324%s
324
    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong...')
sendingmail()



