import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print('recog..')
        query = r.recognize_google(audio, language='en-in')
        print('user said : {}'.format(query) )
    
    except Exception as e:
        print(e)
        print('say that again..')
        return 'None'


if __main__=='__main__':
takeCommand()

