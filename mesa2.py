
import random
import time
import wikipedia                                        #allow to access information from wikipedia.
import pyttsx3                                          #allow text-to-speech.
import webbrowser                                       #allow to access websites and URL's from internet.
import datetime                                         #allows the code to access current date and time from the system.
# import getpass                                        #provides secure way to handle the password prompts,(i'm still working and studing on it).
from translate import Translator                        #help in translating the input.
import smtplib
import speech_recognition as sr


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[23].id)
engine.setProperty('rate',220)
engine.setProperty('volume',1)




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



# def Brow():
# browser=webdriver.Chrome('/Users/saurabhmehanti/Downloads/chromedriver')




def sendMail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('YOUR_EMAIL_ID@GMAIL@COM','PASSWORD')
    server.sendmail(email_s,to,content)
    server.close()




def tran():
    print('translating..')
    speak('translating..')
    yo = Translator(from_lang=lann, to_lang=lann1)
    word = yo.translate(give)
    print(word)
    speak(word)



def Shop():
    speak('tell me which product ?')
    shoo=takeCommand()
    if shoo in neg:
        speak('okay , not opening your online product ')

    else:
        speak('opening , ' + shoo + ' , in amazon .com ')
        webbrowser.open('https://www.amazon.in/s?k=' + shoo + '&ref=nb_sb_noss_2')
    time.sleep(2)




def Wiki_is():
    try:
        about = a.split('is ')
        result = wikipedia.summary(about[1], sentences=2)
        print(result)
        speak(result)
        speak('shall i open the page ?')

        page = takeCommand()
        see = ['yes', 'sure', 'yup', 'open', 'open it', 'ya']
        if page in see:
            speak('opening.')
            webbrowser.open('https://en.wikipedia.org/wiki/' + about[1])
        else:
            while True:
                speak('i want you to answer in yes or no!')
                page1 = takeCommand()
                if page1 in neg:
                    speak('not opening')
                    break
                elif page1 in see:
                    speak('opening')
                    webbrowser.open('https://en.wikipedia.org/wiki/' + about[1])
                    break
                else:
                    continue
    except:
        speak('i found something on web about ' , about[1])





while(True):
    password=input('password:- ')


    if password =='Saurabh':
        speak('welcome , tell me your name ?')
        namee=takeCommand()
        if namee=='Saurabh':
            speak('hello sir, what can i do for you ?')
        else:
            speak('hello '+namee)


    elif password in gui1:
        book = open('mesa guide.txt')
        book1 = book.read()
        print(book1)
        speak('the user manual of meesa will show you ,how you can use this assistant to perform things.......please read it carefully.'
              'and then enter the password')
        continue

    else:

        speak('access denied')
        continue


    while(True):

        a=takeCommand().lower()


            #the user input.


        if 'search google' in a:
            speak('what you want to search?')
            dal1=['nothing','leave it','leave']
            dal=takeCommand()
            if dal in dal1:
                speak('okay, i will not search anything')
            else:
                speak('searching about'+ dal)

                webbrowser.open('https://www.google.com/search?q='+dal)
        elif 'what is ' in a:
            Wiki_is()



         elif 'online shopping' in a:
            Shop()

        elif 'online products' in a:
            Shop()

        elif 'products' in a:
            Shop()


         elif 'translate' in a:
            la=a.split()
            lann=la[2]
            lann1=la[4]
            speak('tell me the sentance or word in '+ lann)
            give=takeCommand()
            tran()



         elif 'send email' in a:
            speak('send email to whome ?')
            to=input("sender's email id:  ")
            if 'leave' in to:

                speak('okay , not sending email to anybody')
            else:
                try:
                    speak('speak your message?')
                    print('your message: ')
                    content = takeCommand()
                    email_s='YOUR_EMAIL_ID@GMAIL.COM'
                    print('From:YOUR_EMAIL_ID')
                    print('To:',email_s)
                    print('send material:',content)
                    sendMail(to, content)
                    speak('email has been send')
                except Exception as e:
                    print(e)
                    speak('sorry,problem occured while sending mail')


         elif 'time' in a:
                 
                 print(time.ctime())
                 speak('The time is, '+ time.ctime())


            
        else:
            pass

          



        


            









        
  
