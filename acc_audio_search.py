
from googlesearch import search
import webbrowser
 
# to search
query = "Geeksforgeeks"
import speech_recognition as sr
import pyttsx3 

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to
# speech
def SpeakText(command):
    
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
    
    
# Loop infinitely for user to
# speak
pomboclatt =False
while(True):    
    
    # Exception handling to handle
    # exceptions at the runtime
    try:
        
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            #listens for the user's input 
            audio2 = r.listen(source2)
            
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print(MyText)
            if pomboclatt:
                for j in search(MyText, tld="co.in", num=1, stop=1, pause=2):
                    print(j)
                    webbrowser.open(j, new=0, autoraise=True)
                MyText = "Searching "+MyText
                SpeakText( MyText)
                pomboclatt = False

            if MyText == "search":
                pomboclatt = True

            
    except sr.RequestError as e:
        print("hi")
        
    except sr.UnknownValueError:
        print("hi")


