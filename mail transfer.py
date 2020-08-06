import smtplib
import pyttsx3
import speech_recognition as sr



engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[23].id)
engine.setProperty('rate',220)
engine.setProperty('volume',1)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source,duration=0.50)
        print('listening...')
        r.pause_threshold = 1
        r.energy_threshold = 400
        spp = r.listen(source)

    try:
        a= r.recognize_google(spp, language='en-in')
        print('You said : {}'.format(a))

    except Exception as e:
        # print(e)
        # print('beg your pardon..')
        # speak('beg your pardon')
        return 'None'
    return a



def sendMail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('YOUR_EMAIL@gmail.com','YOUR_GMAIL_PASSWORD')
    server.sendmail(email_s,to,content)
    server.close()



if __name__ == '__main__':

    speak('send email to whome ?')
    to = input("sender's email id:  ")
    if 'leave' in to:

        speak('okay , not sending email to anybody')
    else:
        try:
            speak('speak your message?')
            print('your message: ')
            content = takeCommand()
            email_s = 'YOUR_EMAIL@gmail.com'
            print('From: YOUR_EMAIL@gmail.com')
            print('To:', email_s)
            print('send material:', content)
            sendMail(to, content)
            speak('email has been send')
        except Exception as e:
            print(e)
            speak('sorry,problem occured while sending mail')
