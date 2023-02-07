import speech_recognition as sr

r = sr.Recognizer()
with sr.AudioFile('test.wav') as source:
    audio = r.record(source)

# recoginize_google() method will throw a request error if the API is unreachable probably due to bad network, hence using exception handling
    try:
        
        # using google speech recognition
        text = r.recognize_google(audio)
        print('Converting audio transcripts into text ...')
        print(text)
     
    except:
         print('Sorry.. run again...')

with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        # using google speech recognition
        print("Text: "+r.recognize_google(audio_text))
    except:
         print("Sorry, I did not get that")