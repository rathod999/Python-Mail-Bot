from math import inf
import smtplib
import speech_recognition as sr #for the speech_recognition
import pyttsx3
from email.message import EmailMessage

listener= sr.Recognizer()
engine =pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()



# try block for converting voice to text;
def get_info():
    try:
        with sr.Microphone() as source:
            print("Listening......")
            voice= listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()

    except:
        pass

def send_mail(receiver,subject,message):
    # sender_mail='rathodpraveen206@gmail.com'
    # receiver_mail ='rathodpraveen206@gmail.com,neelsurve31@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your maill','your password') #Change the mail id and password
    email = EmailMessage()
    email['From'] = "your mail"   #enter ur mail id
    email['To'] =receiver
    email['Subject']= subject
    email.set_content(message)
    server.send_message(email)

    # server.sendmail(sender_mail,receiver_mail,
    #             'Respected parents your wards attendance is below norms please look into it'
    #             )
email_list={
    'neel':"neelsurve31@gmail.com",
    'praveen':'rathodpraveen206@gmail.com'
}


def get_email_info():
    talk('To whom you want to send email')
    name= get_info()
    receiver = email_list[name]
    print(receiver)
    talk('what is the subject of your email??')
    subject = get_info()
    talk('Tell me the text in your email')
    message =get_info()
    send_mail(receiver, subject, message)
get_email_info()


