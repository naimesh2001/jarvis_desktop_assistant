import subprocess 
import wolframalpha 
import pyttsx3 
import json 
import random 
import operator 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os  
import pyjokes 
import smtplib 
import ctypes 
import time  
import shutil
import requests 
import winshell
import pyaudio



from bs4 import BeautifulSoup 
import win32com.client as wincl 
from urllib.request import urlopen

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 
  
def wishMe(): 
    hour = int(datetime.datetime.now().hour) 
    if hour>= 0 and hour<12: 
        speak("Good Morning Sir !") 
   
    elif hour>= 12 and hour<18: 
        speak("Good Afternoon Sir !")    
   
    else: 
        speak("Good Evening Sir !")   
   
    assname =("Jarvis 1 point o") 
    speak("I am your Assistant") 
    speak(assname) 
      
  
def usrname(): 
    speak("What should i call you sir") 
    uname = takeCommand() 
    speak("Welcome Mister") 
    speak(uname) 
    columns = shutil.get_terminal_size().columns 
      
    print("\t\t\t#####################".center(columns)) 
    print("Welcome Mr.", uname.center(columns)) 
    print("\t\t\t#####################".center(columns)) 
      
    speak("How can i Help you, Sir") 
  
def takeCommand(): 
      
    r = sr.Recognizer() 
      
    with sr.Microphone() as source: 
          
        print("Listening...") 
        r.pause_threshold = 1
        audio = r.listen(source) 
   
    try: 
        print("Recognizing...")     
        query = r.recognize_google(audio, language ='en-in') 
        print(f"User said: {query}\n") 
   
    except Exception as e: 
        print(e)     
        print("Unable to Recognizing your voice.")   
        return "None"
      
    return query 
   
def sendEmail(to, content): 
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo() 
    server.starttls() 



    server.login('18dit031@charusat.edu.in', 'Dit_exam@2001') 
    server.sendmail('18dit031@charusat.edu.in', to, content) 
    server.close()


if  __name__ == "__main__":
    pass
    clear = lambda: os.system('cls') 
      

    clear() 
    wishMe() 
    usrname() 
      
    while True: 
          
        query = takeCommand().lower() 
          
  
        if 'open youtube' in query: 
            speak("Here you go to Youtube\n") 
            webbrowser.open("youtube.com") 
  
        elif 'open google' in query: 
            speak("Here you go to Google\n") 
            webbrowser.open("google.com") 
  
        elif 'open stackoverflow' in query: 
            speak("Here you go to Stack Over flow.Happy coding") 
            webbrowser.open("stackoverflow.com")    
  
        elif 'play music' in query or "play song" in query: 
            speak("Here you go with music") 
            music_dir = "C:\\Users\\DC\\Desktop\\SEM6\\SGP\\Jarvis\\Music"            
            songs = os.listdir(music_dir) 
            print(songs)     
            random = os.startfile(os.path.join(music_dir, songs[1])) 
  
 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
  

        elif 'email to me' in query: 
            try: 
                speak("What should I say?") 
                content = takeCommand() 
                to = "naimeshlakhara2001@gmail.com"    
                sendEmail(to, content) 
                speak("Email has been sent !") 
            except Exception as e: 
                print(e) 
                speak("I am not able to send this email") 
  
        elif 'send a mail' in query: 
            try: 
                speak("What should I say?") 
                content = takeCommand() 
                speak("whome should i send") 
                to = input()     
                sendEmail(to, content) 
                speak("Email has been sent !") 
            except Exception as e: 
                print(e) 
                speak("I am not able to send this email") 
  
        elif 'how are you' in query: 
            speak("I am fine, Thank you") 
            speak("How are you, Sir") 
  
        elif 'fine' in query or "good" in query: 
            speak("It's good to know that your fine") 
  
        elif "change my name to" in query: 
            query = query.replace("change my name to", "") 
            assname = query 
  
        elif "change name" in query: 
            speak("What would you like to call me, Sir ") 
            assname = takeCommand() 
            speak("Thanks for naming me") 
  
        elif "what's my name" in query or "What is my name" in query: 
            speak("My friends call me") 
            speak(assname) 
            print("My friends call me", assname) 
  
        elif 'exit' in query: 
            speak("Thanks for giving me your time") 
            exit() 
  
        elif "who made you" in query or "who created you" in query:  
            speak("I have been created by Charusat Stdent of IT Department.") 
              
        elif 'joke' in query: 
            speak(pyjokes.get_joke()) 
              
  
        elif 'search' in query or 'play' in query: 
              
            query = query.replace("search", "")  
            query = query.replace("play", "")           
            webbrowser.open(query)  
  
        elif "who i am" in query: 
            speak("If you talk then definately your human.") 
  
        elif "why you came to world" in query: 
            speak("Thanks to Charusat Student of further It's a secret") 
  
        elif 'powerpoint presentation' in query: 
            speak("opening Power Point presentation") 
            power = r"C:\\Users\\DC\\Desktop\\SEM6\\SGP\\SGP Presentation.pptx"  
            os.startfile(power) 
  
        elif 'is love' in query: 
            speak("It is 7th sense that destroy all other senses") 
  
        elif "who are you" in query: 
            speak("I am your virtual assistant created by Charusat student") 
  
        elif 'reason for you' in query: 
            speak("I was created as a Minor project by Mister Naimesh and Jaydip ") 
  
        elif 'change background' in query: 
            ctypes.windll.user32.SystemParametersInfoW(20,  
                                                       0,  
                                                       "Location of wallpaper", 
                                                       0) 
            speak("Background changed succesfully") 
  
        elif 'open vs code' in query: 
            appli = r"C:\\Users\\HP WORLD\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"     
            os.startfile(appli) 
  
        elif 'news' in query: 
              
            try:  
                jsonObj = urlopen('''http://newsapi.org/v2/everything?q=bitcoin&from=2020-10-02&sortBy=publishedAt&apiKey=336368eded8a411c94668574dd5b0da9''') 
                data = json.load(jsonObj) 
                i = 1
                  
                speak('here are some top news from the times of india') 
                print('''=============== TIMES OF INDIA ============'''+ '\n') 
                  
                for item in data['articles']: 
                      
                    print(str(i) + '. ' + item['title'] + '\n') 
                    print(item['description'] + '\n') 
                    speak(str(i) + '. ' + item['title'] + '\n') 
                    i += 1
            except Exception as e: 
                  
                print(str(e)) 

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
  
          
        elif 'lock window' in query: 
                speak("locking the device") 
                ctypes.windll.user32.LockWorkStation() 
  
        elif 'shutdown system' in query: 
                speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f') 
                  
        elif 'empty recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            speak("Recycle Bin Recycled") 
  
        elif "don't listen" in query or "stop listening" in query: 
            speak("for how much time you want to stop jarvis from listening commands") 
            a = int(takeCommand()) 
            time.sleep(a) 
            print(a) 
  
        elif "where is" in query: 
            query = query.replace("where is", "") 
            location = query 
            speak("User asked to Locate") 
            speak(location) 
            webbrowser.open("https://www.google.co.in/maps/place/" + location + "") 
  

  
        elif "restart" in query: 
            subprocess.call(["shutdown", "/r"]) 
              
        elif "hibernate" in query or "sleep" in query: 
            speak("Hibernating") 
            subprocess.call("shutdown / h") 
  
        elif "log off" in query or "sign out" in query: 
            speak("Make sure all the application are closed before sign-out") 
            time.sleep(5) 
            subprocess.call(["shutdown", "/l"]) 
  
        elif "write a note" in query: 
            speak("What should i write, sir") 
            note = takeCommand() 
            file = open("C:\\Users\\HP WORLD\\Desktop\\5ITSGP\\jarvis.txt", 'w') 
            
          
        elif "show me notes" in query: 
            speak("Showing Notes") 
            file = open("C:\\Users\\HP WORLD\\Desktop\\5ITSGP\\jarvis.txt", 'r')  
            print(file.read()) 
            speak(file.read(6)) 
                        
        elif "jarvis" in query: 
              
            wishMe() 
            speak("Jarvis 1 point o in your service Mister") 
            speak(assname) 
  
        
              
    
  
        elif "open Wikipedia" in query: 
            webbrowser.open("wikipedia.com") 
  
        elif "Good Morning" in query: 
            speak("A warm" +query) 
            speak("How are you Mister") 
            speak(assname) 

        elif "calculate" in query:
              
            app_id = "Wolframalpha api id" 
            client = wolframalpha.Client(app_id) 
            indx = query.lower().split().index('calculate')  
            query = query.split()[indx + 1:]  
            res = client.query(''.join(query))  
            answer = next(res.results).text 
            print("The answer is " + answer)  
            speak("The answer is " + answer)  
            
                
  
        elif "will you be my gf" in query or "will you be my bf" in query:    
            speak("I'm not sure about, may be you should give me some time") 
  
        elif "how are you" in query: 
            speak("I'm fine, glad you me that") 
  
        elif "i love you" in query: 
            speak("It's hard to understand") 

  
       
