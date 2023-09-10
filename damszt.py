from kivy.config import Config
Config.set('graphics','resizable',False)
from kivy.utils import platform
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.clock import mainthread,Clock
import threading
import os
import wave
import math
import threading
import pyaudio
import speech_recognition as sr
from datetime import date
import numpy as np
import sympy as sp
from sympy import *
from win32com.client import Dispatch
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty

class ScrollableLabel(ScrollView):
    text = StringProperty('')
class Damszt(MDApp):
    def build(self):
        #self.icon = 'rspllc.png'
        if (platform == 'android' or platform == 'ios'):
            Window.maximize()
        else:
            Window.size = (300,578)        
        return Builder.load_file("dams.kv")        
    def on_start(self):
        Clock.schedule_once(self.intro, 0)        
    def intro(self,dt):
        # start of app
        b="welcome to dams', your handfree calsee"
        threading.Thread(target=self.sayans, args=(b,)).start()
        self.h = 0
        self.w = 0
        today = str(date.today())
        today=" "+ today
        self.recording = False

        self.root.ids.inp.cursor=(1,0)
        self.root.ids.inp.cursor_color = 1,1,1,1
        self.root.ids.ans.cursor=(1,0)
        self.root.ids.ans.cursor_color = 1,1,1,1
        self.root.ids.inp2.cursor=(1,0)
        self.root.ids.inp2.cursor_color = 1,1,1,1
        self.root.ids.ans2.cursor=(1,0)
        self.root.ids.ans2.cursor_color = 1,1,1,1
        self.root.ids.inp3.cursor=(1,0)
        self.root.ids.inp3.cursor_color = 1,1,1,1
        self.root.ids.ans3.cursor=(1,0)
        self.root.ids.ans3.cursor_color = 1,1,1,1

        self.root.ids.todate.cursor=(1,0)
        self.root.ids.todate.cursor_color = 1,1,1,1
        self.root.ids.todate.text = today
        self.root.ids.dob.cursor=(1,0)
        self.root.ids.dob.cursor_color = 1,1,1,1
        self.root.ids.dob.hint_text_color = 0.5, 0.5, 0.5, 1.0
        self.root.ids.urage.cursor=(1,0)
        self.root.ids.urage.cursor_color = 1,1,1,1
        self.root.ids.urage1.cursor=(1,0)
        self.root.ids.urage1.cursor_color = 1,1,1,1
        self.root.ids.con.cursor=(1,0)
        self.root.ids.con.cursor_color = 1,1,1,1
    def clean(self):
        # clean the trash
        self.root.ids.his.text = "Successfully Cleared your Calculation History"
        self.root.ids.his.cursor=(1,0)
        if os.path.exists("history.txt"):
            os.remove("history.txt")
    def pop(self,number):
        # Popup screen
        if number == 1:
            lbl = ScrollableLabel(text="1) Tap on Damszt MicroPhone and say your calculations.\n\n2) Tap again to get your results.\n\n3) Please be audible and use headphones for better experience.\n\n4) You can perform the five basic operations as follows:\n\ni} Addition - e.g. two plus two (2+2)\n\nii} Subtraction - e.g. two minus two (2-2)\n\niii} Multiplication - e.g. two into two (or) two multiplied by two (2x2)\n\niv} Division - e.g. two by two (or) two divided by two (2/2)\n\nv} Modulus (remainder) - e.g. two mod three (2%3)\n\n5) You can also perform the six trigonometric functions by saying as follows:\n\ni} sin() - e.g. sine 20 parenthesis sin(20)\n\nii} cos() - e.g. kaas 20 parenthesis cos(20)\n\niii} tan() - e.g. tan 20 parenthesis tan(20)\n\niv} cosec() - e.g. cosecant 20 parenthesis cosec(20)\n\nv} sec() - e.g. secant 20 parenthesis sec(20)\n\nvi} cot() - e.g. caught 20 parenthesis cot(20)\n\n6) Note that, the keyword \"parenthesis\" is very important for the Calc to recognize your input expression.\n\n7) Placement of parenthesis also makes difference in the recognization of expression.\n\ne.g. sine kaas 20 parenthesis\nsin(cos(20))\ne.g. sin 20 parenthesis plus kaas 20 parenthesis\nsin(20) + cos(20)\ne.g. sine 20 plus kaas 20 parenthesis\nsin(20 + cos(20))\n\nSo, Please be careful with parenthesis\n\n8) Please do select any one of the modes i.e. \'Radians\' or \'Degrees\' before using trigonometric functions.\n\n9) You can also perform \"log\", \"ln\", \"power\" and \"factorial\" functions as follows.\n\ni} log 10 parenthesis - log(10)\n\nii} ln (lon) 10 parenthesis - ln(10)\n\niii} two power three - 2^3\n\niv} two factorial - 2!\n\n10) To do calculations with \'pi\', just say \"pi\" or \"m-pi\" (empi) which means \"maths pi\".\n")        
            popup = Popup(title='Damszt - Super Calc  (Tips Corner)', title_font="bold",content=lbl,size_hint=(None, None),size=(300, 530), pos_hint = {"center_x": .50, "center_y": .450})
            popup.open()
        elif number == 2:
            lbl = ScrollableLabel(text="1) Tap on Damszt MicroPhone and say your calculations.\n\n2) Tap again to get your results.\n\n3) Please be audible and use headphones for better experience.\n\n4) You can perform differentiation as follows:\n\ni} Addition - e.g. two plus x (2+x)\n\nii} Subtraction - e.g. thirty two minus x (32-x)\n\niii} Multiplication - e.g. two into x (or) two multiplied by x (2.x)\n\niv} Division - e.g. two by x (or) two divided by x (2/x)\n\nv} sin() - e.g. sine x parenthesis sin(x)\n\nvi} cos() - e.g. kaas x parenthesis cos(x)\n\nvii} tan() - e.g. tan x parenthesis tan(x)\n\nviii} cosec() - e.g. cosecant x parenthesis cosec(x)\n\nix} sec() - e.g. secant x parenthesis sec(x)\n\nx} cot() - e.g. caught x parenthesis cot(x)\n\n5) Note that, the keyword \"parenthesis\" is very important for the Calc to recognize your input expression.\n\n6) Placement of parenthesis also makes difference in the recognization of expression.\n\ne.g. sine kaas x parenthesis\nsin(cos(x))\ne.g. sin x parenthesis plus kaas x parenthesis\nsin(x) + cos(x)\ne.g. sine x plus kaas x parenthesis\nsin(x + cos(x))\n\nSo, Please be careful with parenthesis.\n\n7) Note that, you can perform differention only with respect to \"x\".\n\n8) No need of saying \"differentiation\".\n")
            popup = Popup(title='Damszt - Derivative Calc  (Tips Corner)', title_font="bold",content=lbl,size_hint=(None, None),size=(300, 530), pos_hint = {"center_x": .50, "center_y": .450})
            popup.open()     
        elif number == 3:
            lbl = ScrollableLabel(text="1) Tap on Damszt MicroPhone and say your calculations.\n\n2) Tap again to get your results.\n\n3) Please be audible and use headphones for better experience.\n\n4) You can perform integration as follows:\n\ni} Addition - e.g. two plus x (2+x)\n\nii} Subtraction - e.g. thirty two minus x (32-x)\n\niii} Multiplication - e.g. two into x (or) two multiplied by x (2.x)\n\niv} Division - e.g. two by x (or) two divided by x (2/x)\n\nv} sin() - e.g. sine x parenthesis sin(x)\n\nvi} cos() - e.g. kaas x parenthesis cos(x)\n\nvii} tan() - e.g. tan x parenthesis tan(x)\n\nviii} cosec() - e.g. cosecant x parenthesis cosec(x)\n\nix} sec() - e.g. secant x parenthesis sec(x)\n\nx} cot() - e.g. caught x parenthesis cot(x)\n\n5) Note that, the keyword \"parenthesis\" is very important for the Calc to recognize your input expression.\n\n6) Placement of parenthesis also makes difference in the recognization of expression.\n\ne.g. sine kaas x parenthesis\nsin(cos(x))\ne.g. sin x parenthesis plus kaas x parenthesis\nsin(x) + cos(x)\ne.g. sine x plus kaas x parenthesis\nsin(x + cos(x))\n\nSo, Please be careful with parenthesis.\n\n7) Note that, you can perform integration only with respect to \"x\".\n\n8) No need of saying \"integration\".\n")   
            popup = Popup(title='Damszt - Integral Calc  (Tips Corner)', title_font="bold",content=lbl,size_hint=(None, None),size=(300, 530), pos_hint = {"center_x": .50, "center_y": .450})
            popup.open() 
        elif number == 4:
            lbl = ScrollableLabel(text="1) Tap on Damszt MicroPhone and say your Date Of Birth.\n\n2) Tap again to get your Age.\n\n3) Please be audible and use headphones for better experience.\n\n4) Please say your DOB in the below given format.\n\n             \"yyyy/mm/dd\"\n\ne.g. thirteen twenty slash two slash four (or) one three two zero slash two slash four\n\n                (1320/2/4)\n\n5) Note that, the keyword \'slash\' is very important to recognize your DOB.\n\n6) So, please do say it without fail.\n")
            popup = Popup(title='Damszt - Age Calc  (Tips Corner)', title_font="bold",content=lbl,size_hint=(None, None),size=(300, 530), pos_hint = {"center_x": .50, "center_y": .450})
            popup.open()
        elif number == 5:
            lbl = ScrollableLabel(text="1) Please select any one of the systems that you want.\n\n2) Then, click on the \"weight box\", say your weight and again tap on it to enter your weight.\n\n3) Click on the \"height box\", say your height and again tap on it to enter your weight.\n\n4) After entering the required data, please do click on the \"BMI box\" to get your BMI value.\n\n5) You need to mention the units accordingly, to get better results.\ne.g. twenty kilogram (20 kg), ten centimeter (10 cm), forty pounds (40 lb) and thirty five inches (35 in).\n")
            popup = Popup(title='Damszt - BMI Calc  (Tips Corner)', title_font="bold",content=lbl,size_hint=(None, None),size=(300, 470), pos_hint = {"center_x": .50, "center_y": .400})
            popup.open() 
        else:
            lbl = ScrollableLabel(text="1) To recover your calculations history, please do atleast one calcuation, once you enter the application.\n\n2) Your history is saved along with the date, that you have performed that particular calculation.\n\n3) You can delete your history permanently by using \"Damszt Trashman\".\n\n4) Please clear your history often to make your storage free.\n")
            popup = Popup(title='Damszt - History  (Tips Corner)', title_font="bold",content=lbl,size_hint=(None, None),size=(300, 470), pos_hint = {"center_x": .50, "center_y": .400})
            popup.open()
    def speak(self,num):
        # app speak
        if num==1:
            s="this is, dams microphone, this records, your calculation, recognizes it, and gives the result. to use dams microphone, tap on it, say your calculation, and tap again, to get the result. thank you"
            threading.Thread(target=self.sayans, args=(s,)).start()
        elif num==2:
            s="this is,dams navigator, this helps you to navigate, across different calculators, without swiping. to use dams navigator, tap on it, say the name of the calculator, and tap again, to reach that particular calculator. you can also, exit the application using dams navigator, by saying quit, or exit. thank you"
            threading.Thread(target=self.sayans, args=(s,)).start()
        elif num==3:
            s="this is, dams informant, this gives information about, each and every calculator, and also guides you, how to use them. to use dams informant, just tap on it. thank you"
            threading.Thread(target=self.sayans, args=(s,)).start()
        elif num==4:
            s="this is,dams trashman, this deletes, your past calculation's history. note that, you cannot recover your history afterwards. to use damszt trashman, just tap on it. thank you"
            threading.Thread(target=self.sayans, args=(s,)).start()
    def ch(self,e):
        # upper buttons 
        if e==10:
            self.root.ids.deg.md_bg_color = 245/255, 252/255, 245/255
            self.root.ids.rad.md_bg_color = 222/255, 242/255, 250/255
            self.pee = "rad"
        elif e==11:
            self.root.ids.rad.md_bg_color = 245/255, 252/255, 245/255
            self.root.ids.deg.md_bg_color = 222/255, 242/255, 250/255
            self.pee = "deg" 
        elif e==12:
            self.root.ids.imperial.md_bg_color = 245/255, 252/255, 245/255
            self.root.ids.metric.md_bg_color = 215/255, 255/255, 199/255
            self.pee = "metric" 
            self.root.ids.w.text="Weight (kg)"
            self.root.ids.h.text="Height (cm)"
            self.root.ids.urage1.text=" Body Mass Index"
            self.root.ids.con.text=" "
        elif e==13:
            self.root.ids.metric.md_bg_color = 245/255, 252/255, 245/255
            self.root.ids.imperial.md_bg_color = 215/255, 255/255, 199/255
            self.pee = "imperial"                 
            self.root.ids.w.text="Weight (lb)"
            self.root.ids.h.text="Height (in)"
            self.root.ids.urage1.text=" Body Mass Index"
            self.root.ids.con.text=" "
    def click(self,t):
        # record of voice
        if self.recording:
            self.recording = False
            if t==100:
                self.type = "n" 
                self.root.ids.nav.source = "navi.png"
            elif t==101:
                self.type = "n" 
                self.root.ids.nav1.source = "navi.png"
            elif t==102:
                self.type = "n" 
                self.root.ids.nav2.source = "navi.png"
            elif t==103:
                self.type = "n" 
                self.root.ids.nav3.source = "navi.png"
            elif t==104:
                self.type = "n" 
                self.root.ids.nav4.source = "navi.png"
            elif t==105:
                self.type = "n" 
                self.root.ids.nav5.source = "navi.png"
            elif t==106:
                self.type = "n" 
                self.root.ids.nav6.source = "navi.png"
            elif t==107:
                self.type = "n" 
                self.root.ids.nav7.source = "navi.png"
            elif t==108:
                self.type = "n" 
                self.root.ids.nav8.source = "navi.png"
            elif t==4:
                self.type = "calc"
                self.root.ids.img.source = "dams.png"
                self.root.ids.inp.text="Recognizing..."
            elif t==5:
                self.type = "deri"
                self.root.ids.img1.source = "dams.png"
                self.root.ids.inp2.text="Recognizing..."
            elif t==6:
                self.type = "anti"
                self.root.ids.img2.source = "dams.png"
                self.root.ids.inp3.text="Recognizing..."
            elif t==7:
                self.type = "age"
                self.root.ids.img3.source = "dams.png"
                self.root.ids.dob.text="Recognizing..."   
            elif t==8 or t==9:
                self.pra = "bmi"                      
        else:            
            if t==100:
                self.type = "n" 
                self.root.ids.nav.source = "navi after.png"
            elif t==101:
                self.type = "n" 
                self.root.ids.nav1.source = "navi after.png"
            elif t==102:
                self.type = "n" 
                self.root.ids.nav2.source = "navi after.png"
            elif t==103:
                self.type = "n" 
                self.root.ids.nav3.source = "navi after.png"
            elif t==104:
                self.type = "n" 
                self.root.ids.nav4.source = "navi after.png"
            elif t==105:
                self.type = "n" 
                self.root.ids.nav5.source = "navi after.png"
            elif t==106:
                self.type = "n" 
                self.root.ids.nav6.source = "navi after.png"
            elif t==107:
                self.type = "n" 
                self.root.ids.nav7.source = "navi after.png"
            elif t==108:
                self.type = "n" 
                self.root.ids.nav8.source = "navi after.png"
            elif t==4:
                self.type = "calc"
                self.root.ids.img.source = "dams after.png"
                self.root.ids.inp.text="Listening..."
                self.root.ids.ans.text=""
            elif t==5:
                self.type = "deri"
                self.root.ids.img1.source = "dams after2.png"
                self.root.ids.inp2.text="Listening..."
                self.root.ids.ans2.text=""
            elif t==6:
                self.type = "anti"
                self.root.ids.img2.source = "dams after3.png"
                self.root.ids.inp3.text="Listening..."
                self.root.ids.ans3.text=""
            elif t==7:
                self.type = "age"
                self.root.ids.img3.source = "dams after4.png"
                self.root.ids.dob.text="Listening..."
                self.root.ids.urage.text=" "
                self.root.ids.what.text=" "
                self.root.ids.what.background_color = (1,1,1,1)
            else:
                if t==8:                    
                    self.type = "weight"
                    self.root.ids.w.text="Listening..."
                elif t==9:
                    self.type = "height"
                    self.root.ids.h.text="Listening..."
            self.recording = True
            threading.Thread(target=self.record).start()
    def record(self):
        # actual record of user's voice
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        frames = []
        while self.recording:
            data = stream.read(1024)
            frames.append(data)
        stream.stop_stream()
        stream.close()
        audio.terminate()
        sf = wave.open(f"rec.wav","wb")
        sf.setnchannels(1)
        sf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sf.setframerate(44100)
        sf.writeframes(b''.join(frames))
        sf.close()
        if self.type == "age":
            threading.Thread(target=self.update1).start()
        elif self.type == "weight" or self.type == "height":
            threading.Thread(target=self.update2, args = (self.type,)).start()
        else:
            threading.Thread(target=self.update, args=(self.type,)).start()
    @mainthread
    def update(self,t):
        # check of calz
        Speak = Dispatch('SAPI.Spvoice')
        Speak.Voice = Speak.GetVoices().Item(2)
        Speak.Rate = 1
        Speak.Volume = 90
        try:
            filename = "rec.wav"
            r = sr.Recognizer()
            with sr.AudioFile(filename) as source:
                audi = r.record(source)
                s = r.recognize_google(audi,language="en-us")
                s = s.lower()     
                if "mp" in s:
                    s=s.replace("mp","pi")      
                if "mi" in s:
                    s=s.replace("mi","pi")                 
                if "pai" in s:
                    s=s.replace("pai","pi")       
                    
                if "thank you" in s or "thank" in s:
                    s = "you are welcome!please do support us!!!"
                    Speak.Speak(s) 
                    if t == "calc":
                        self.root.ids.inp.text=""
                        self.root.ids.ans.text=""
                    elif t == "deri":
                        self.root.ids.inp2.text=""
                        self.root.ids.ans2.text=""
                    elif t == "anti":
                        self.root.ids.inp3.text=""
                        self.root.ids.ans3.text=""
                elif t == "deri":
                    threading.Thread(target=self.check2, args=(s,t,)).start()
                elif t == "anti":
                    threading.Thread(target=self.check2, args=(s,t,)).start()
                elif t == "n":
                    threading.Thread(target=self.check3, args=(s,)).start()
                else:
                    threading.Thread(target=self.check, args=(s,t,)).start()
        except:
            if t == "calc":
                self.root.ids.inp.text="Unable to recognize.\nPlease try again!!!"
                self.root.ids.ans.text=""
            elif t == "deri":
                self.root.ids.inp2.text="Unable to recognize.\nPlease try again!!!"
                self.root.ids.ans2.text=""
            elif t == "anti":
                self.root.ids.inp3.text="Unable to recognize.\nPlease try again!!!"
                self.root.ids.ans3.text=""            
            elif t=="n":
                s="please, try again"
                Speak.Speak(s)
    @mainthread   
    def update2(self,typ):
        Speak = Dispatch('SAPI.Spvoice')
        Speak.Voice = Speak.GetVoices().Item(2)
        Speak.Rate = 1
        Speak.Volume = 90
        try:
            filename = "rec.wav"
            r = sr.Recognizer()
            with sr.AudioFile(filename) as source:
                audi = r.record(source)
                s = r.recognize_google(audi,language="en-us")
                s = s.lower()    
                if "kilogram" in s:
                    s=s.replace("kilogram","")
                if "party" in s:
                    s=s.replace("party","40")
                if "kilograms" in s:
                    s=s.replace("kilograms","")
                if "pounds" in s:
                    s=s.replace("pounds","")
                if "pound" in s:
                    s=s.replace("pound","")
                if "centimeter" in s:
                    s=s.replace("centimeter","")
                if "centimeters" in s:
                    s=s.replace("centimeters","")
                if "inches" in s:
                    s=s.replace("inches","")
                if "inch" in s:
                    s=s.replace("inch","")
                if "means" in s:
                    s=s.replace("means","")
                if "kg" in s:
                    s=s.replace("kg","")
                if "cm" in s:
                    s=s.replace("cm","")
                if typ == "weight":
                    try:
                        self.w = float(s)
                        if self.pee == "metric":
                            l=s+" kg"
                        else:
                            l=s+" lb"
                        self.root.ids.w.text=l
                        self.root.ids.con.text=" "
                        self.root.ids.urage1.text=" Body Mass Index"
                    except:
                        self.root.ids.w.text=s
                        self.root.ids.con.text="Please enter your weight properly!!!"    
                else:
                    try:
                        self.h = int(s)
                        if self.pee == "metric":
                            j=s+" cm"
                        else:
                            j=s+" in"
                        self.root.ids.h.text=j
                        self.root.ids.con.text=" "
                        self.root.ids.urage1.text=" Body Mass Index"
                    except:
                        self.root.ids.h.text=s
                        self.root.ids.con.text="Please enter your height properly!!!"          
        except:
            if typ == "weight": 
                if self.pee == "metric":
                    self.root.ids.w.text="Weight (kg)"
                    self.root.ids.con.text="Unable to recognize.\nPlease try again!!!"
                elif self.pee == "metric":
                    self.root.ids.w.text="Weight (lb)"
                    self.root.ids.con.text="Unable to recognize.\nPlease try again!!!"
            elif typ == "height":
                if self.pee == "imperial":
                    self.root.ids.h.text="Height (cm)"
                    self.root.ids.con.text="Unable to recognize.\nPlease try again!!!"
                elif self.pee == "imperial":
                    self.root.ids.h.text="Height (in)"
                    self.root.ids.con.text="Unable to recognize.\nPlease try again!!!"
    def ev(self):
        try:
            bmi = 0
            w=self.w
            h=self.h
            if self.pee == "metric":
                bmi=w/(h/100)**2
                bmi=round(bmi,2)
                bmi = str(bmi)
                self.root.ids.urage1.text=bmi 
                bmi = float(bmi)
            else:
                bmi=w/(h**2)*703
                bmi=round(bmi,2)
                bmi = str(bmi)
                self.root.ids.urage1.text=bmi 
                bmi = float(bmi)

            if bmi<18.5:
                self.root.ids.con.text="Ooops! You are underweight!"
                self.root.ids.con.background_color = (255/255,160/255,122/255)
                bmi = 0
                w=0
                h=0
            elif 18.5<=bmi<24.99:
                self.root.ids.con.text="Hurray! You are healthy!"
                self.root.ids.con.background_color = (173/255,255/255,47/255)
                bmi = 0
                w=0
                h=0
            elif 25<=bmi<29.99:
                self.root.ids.con.text="Hmmm! You are overweight!"
                self.root.ids.con.background_color = (255/255,215/255,0/255)
                bmi = 0
                w=0
                h=0
            else:
                self.root.ids.con.text="Sorry! You are Obese"    
                self.root.ids.con.background_color = (255/255,99/255,71/255)
                bmi = 0
                w=0
                h=0
        except:
            if  self.w==0:
                self.root.ids.con.text="Please enter your weight!!!"
            elif self.h==0:
                self.root.ids.con.text="Please enter your height!!!"
            else:
                self.root.ids.con.text = "Please try agin!!!"    
    @mainthread  
    def update1(self):
        try:
            filename = "rec.wav"
            r = sr.Recognizer()
            with sr.AudioFile(filename) as source:
                audi = r.record(source)
                s = r.recognize_google(audi,language="en-us")
                s = s.lower()
                if "thank you" in s or "thanks" in s:
                    Speak = Dispatch('SAPI.Spvoice')
                    Speak.Voice = Speak.GetVoices().Item(2)
                    Speak.Rate = 1
                    Speak.Volume = 90
                    s = "you are welcome!please do support us!!!"
                    Speak.Speak(s)
                    self.root.ids.dob.text=""
                    self.root.ids.urage.text=""
                else:
                    if "not" in s:
                        s=s.replace("not","0") 
                    if "to" in s:
                        s=s.replace("to","2")
                    if "slash" in s:
                        s=s.replace("slash","/")
                    y,m,d = s.split("/")
                    yrs = float(y)
                    today = date.today()
                    yr = today.year
                    if yrs <= yr:
                        try:
                            self.check1(date(int(y),int(m),int(d)),s)
                        except:
                            self.root.ids.dob.text="Invalid Date Of Birth"
                            self.root.ids.urage.text="Please try again!!!"
                    else:
                        self.root.ids.dob.text="Invalid Date Of Birth"
                        self.root.ids.urage.text="Please try again!!!"
        except:
            self.root.ids.dob.text="Unable to recognize."
            self.root.ids.urage.text="Please try again!!!"
    @mainthread
    def check1(self,born,s):
        today = date.today()
        self.root.ids.dob.text=s
        try:
            birthday = born.replace(year = today.year)
        except ValueError:
            birthday = born.replace(year = today.year,month = born.month + 1, day = 1)

        if birthday > today:
            dat = today.year - born.year - 1
            dat=str(dat)
            dat=" "+dat
            self.root.ids.urage.text=dat
        else:
            dat = today.year - born.year
            dat=str(dat)
            dat=" "+dat
            self.root.ids.urage.text=dat
        dat = float(dat)
        if dat < 0:
            self.root.ids.dob.text="Invalid Date Of Birth"
            self.root.ids.urage.text="Please try again!!!"
        elif 0 <= dat <= 1:
            self.root.ids.what.text="You're an Infant!"
            self.root.ids.what.background_color = (192/255, 227/255, 250/255)
        elif 2 <= dat <= 4:
            self.root.ids.what.text="You're a Toddler!"
            self.root.ids.what.background_color = (247/255, 131/255, 164/255)
        elif 5 <= dat <= 12:
            self.root.ids.what.text="You're a Child!"
            self.root.ids.what.background_color = (253/255, 255/255, 163/255)
        elif 13 <= dat <= 19:
            self.root.ids.what.text="You're a Teen!"
            self.root.ids.what.background_color = (196/255, 164/255, 252/255)
        elif 20 <= dat <= 39:
            self.root.ids.what.text="You're an Adult!"
            self.root.ids.what.background_color = (247/255, 209/255, 148/255)
        elif 40 <= dat <= 59:
            self.root.ids.what.text="You're a Middle Aged Adult!"
            self.root.ids.what.background_color = (207/255, 211/255, 212/255)
        else:
            self.root.ids.what.text="You're a Senior Adult!"
            self.root.ids.what.background_color = (255/255, 107/255, 107/255)
    @mainthread
    def check3(self,s):
        # navigator speech
        Speak = Dispatch('SAPI.Spvoice')
        Speak.Voice = Speak.GetVoices().Item(2)
        Speak.Rate = 1
        Speak.Volume = 90
        print(s)
        if "page" in s:
            s=s.replace("page","")
        if "thank you" in s or "thanks" in s:
            s = "you are welcome!please do support us!!!"
            Speak.Speak(s)
        if "about" in s or "abort" in s:
            s = "ok, sure"
            Speak.Speak(s)
            self.root.ids.carousel.load_slide(self.root.ids.carousel.slides[1])         
        elif "instruction" in s or "instructions" in s:
            s = "ok, sure"
            Speak.Speak(s)
            self.root.ids.carousel.load_slide(self.root.ids.carousel.slides[2])
        elif "main" in s or "main" in s or "home" in s or "ome" in s:
            s = "ok, sure"
            Speak.Speak(s)
            self.root.ids.carousel.load_slide(self.root.ids.carousel.slides[3])
        elif "super" in s or "standard" in s or "scientific"in s or "sooper" in s:
            s = "ok, sure"
            Speak.Speak(s)
            self.root.ids.carousel.load_slide(self.root.ids.carousel.slides[4])
        elif "deri" in s or "differentiation" in s or "diff" in s or "der" in s:
            s = "ok, sure"
            Speak.Speak(s)
            self.root.ids.carousel.load_slide(self.root.ids.carousel.slides[5])
        elif "anti" in s or "integration" in s or "inte" in s or "in" in s:
            s = "ok, sure"
            Speak.Speak(s)
            self.root.ids.carousel.load_slide(self.root.ids.carousel.slides[6])
        elif "his" in s or "h" in s or "story" in s:
            s = "ok, sure"
            Speak.Speak(s)
            self.root.ids.carousel.load_slide(self.root.ids.carousel.slides[9])
        elif "bmi" in s or "bpi" in s or "body" in s or "mass" in s or "index" in s or "emi" in s:
            s = "ok, sure"
            Speak.Speak(s)
            self.root.ids.carousel.load_slide(self.root.ids.carousel.slides[8])
        elif "age" in s:
            s = "ok, sure"
            Speak.Speak(s)
            self.root.ids.carousel.load_slide(self.root.ids.carousel.slides[7])
        elif "quit" in s or "exit" in s or "cute" in s:
            s = "ok, byeee. please do come again "
            Speak.Speak(s)
            exit()
        else:
            s="please, try again"
            Speak.Speak(s)
    @mainthread
    def check(self,s,t):    
        # super calz  
        if "factorial" in s:
            s=s.replace("factorial","!")
        if "x" in s:
            s=s.replace("x"," *")
        if "secund" in s:
            s=s.replace("secund","sec ")             
        if "one" in s:
            s=s.replace("one","1 ")             
        if "zero" in s:
            s=s.replace("zero","0 ")             
        if "hero" in s:
            s=s.replace("hero","0 ")             
        if "two" in s:
            s=s.replace("two","2")             
        if "free" in s:
            s=s.replace("free","3")             
        if "nayan" in s:
            s=s.replace("nayan","9")             
        if "plus" in s:
            s=s.replace("plus","+")             
        if "does" in s:
            s=s.replace("does","+")  
        if "%" in s:
            s=s.replace("%"," %")            
        if "percentage" in s:
            s=s.replace("percentage","%")             
        if "percent" in s:
            s=s.replace("percent","%")                     
        if "modulus" in s:
            s=s.replace("modulus","mod")             
        if "modi" in s:
            s=s.replace("modi","mod")             
        if "model" in s:
            s=s.replace("model","mod")             
        if "mode" in s:
            s=s.replace("mode","mod")             
        if "modified" in s:
            s=s.replace("modified","mod 5")             
        if "by" in s:
            s=s.replace("by","/")                     
        if "bi" in s:
            s=s.replace("bi","/")                     
        if "x" in s:
            s=s.replace("x","*")             
        if "10,000" in s:
            s=s.replace("10,000","10000")             
        if "tree" in s:
            s=s.replace("tree","3")             
        if "into" in s:
            s=s.replace("into","*")             
        if "to" in s:
            s=s.replace("to","2")             
        if "tu" in s:
            s=s.replace("tu","2")             
        if "bhai" in s:
            s=s.replace("bhai","/")                     
        if "why" in s:
            s=s.replace("why","y")             
        if "power" in s:
            s=s.replace("power","**")             
        if "four" in s:
            s=s.replace("four","4")             
        if "cube root" in s:
            s=s.replace("cube root","hukum")               
        if "square root" in s:
            s=s.replace("square root","sqrt")             
        if "route" in s:
            s=s.replace("route","sqrt")             
        if "root" in s:
            s=s.replace("root","sqrt")             
        if "cube" in s:
            s=s.replace("cube","** 3")             
        if "b" in s:
            s=s.replace("b","/")             
        if "square" in s:
            s=s.replace("square","** 2")             
        if "for" in s:
            s=s.replace("for","4")             
        if "2 kyln" in s:
            s=s.replace("2 kyln","2 ** 3")             
        if "sign" in s:
            s=s.replace("sign","sin ")             
        if "science" in s:
            s=s.replace("science","sin ")             
        if "shine" in s:
            s=s.replace("shine","sin ")             
        if "ten" in s:
            s=s.replace("ten","10")             
        if "loan" in s:
            s=s.replace("loan","ln ")             
        if "learn" in s:
            s=s.replace("learn","ln ")             
        if "cars" in s:
            s=s.replace("cars","cos ")             
        if "qrs" in s:
            s=s.replace("qrs","cos ")             
        if "cause" in s:
            s=s.replace("cause","cos")             
        if "you2/e" in s:
            s=s.replace("you2/e","e ** 3")             
        if "loggy" in s:
            s=s.replace("loggy","log e")             
        if "du/ai" in s:
            s=s.replace("du/bai","2 /")             
        if "and 2" in s:
            s=s.replace("and 2","* 2")             
        if "land" in s:
            s=s.replace("land","ln")             
        if "lan" in s:
            s=s.replace("lan","ln")             
        if "lock" in s:
            s=s.replace("lock","log")             
        if "lawn" in s:
            s=s.replace("lawn","ln")             
        if "loan" in s:
            s=s.replace("loan","ln")             
        if "logi" in s:
            s=s.replace("logi","log e")             
        if "how" in s:
            s=s.replace("how","log")             
        if "ready for" in s:
            s=s.replace("ready for","34")             
        if "loni" in s:
            s=s.replace("loni","ln e")             
        if "long" in s:
            s=s.replace("long","ln ")             
        if "lon" in s:
            s=s.replace("lon","ln ")             
        if "dog" in s:
            s=s.replace("dog","log ")             
        if "lock" in s:
            s=s.replace("lock","log ")             
        if "lan" in s:
            s=s.replace("lan","ln ")             
        if "fore" in s:
            s=s.replace("fore","4")             
        if "log10" in s:
            s=s.replace("log10","log 10")             
        if "shiny" in s:
            s=s.replace("shiny","sin e")              
        if "tany" in s:
            s=s.replace("tany","tan e")              
        if "tani" in s:
            s=s.replace("tani","tan e")              
        if "dani" in s:
            s=s.replace("dani","tan e")             
        if "kashi" in s:
            s=s.replace("kashi","cos e")              
        if "kasi" in s:
            s=s.replace("kasi","cos e")             
        if "cosy" in s:
            s=s.replace("cosy","cos e")             
        if "11 10" in s:
            s=s.replace("11 10","ln 10")             
        if "helen" in s:
            s=s.replace("helen","ln ")             
        if "ellen" in s:
            s=s.replace("ellen","ln ")             
        if "on" in s:
            s=s.replace("on","ln ")             
        if "minus" in s:
            s=s.replace("minus","-")             
        if "curse" in s:
            s=s.replace("curse","cos ")             
        if "cost" in s:
            s=s.replace("cost","cos ")                
        if "three" in s:
            s=s.replace("three","3")                
        if "launch" in s:
            s=s.replace("launch","ln ")                     
        if "caught" in s:
            s=s.replace("caught","cot ")             
        if "hot" in s:
            s=s.replace("hot","cot ")             
        if "got" in s:
            s=s.replace("got","cot ")             
        if "ekant" in s:
            s=s.replace("ekant","sec ")             
        if "cottage" in s:
            s=s.replace("cottage","cot ")                     
        if "kota agent" in s:
            s=s.replace("kota agent","cotangent ")             
        if "check" in s :
            s=s.replace("check","sec ")             
        if "point" in s:
            s=s.replace("point",".")
        if "call" in s:
            s=s.replace("call","cos ")             
        if "sin0" in s:
            s=s.replace("sin0","sin 0")            
        if "and" in s:
            s=s.replace("and","")             
        if "kottayam" in s:
            s=s.replace("kottayam","cotangent ")              
        if "agent" in s:
            s=s.replace("agent"," ")             
        if "kaushik" in s:
            s=s.replace("kaushik","cosec ")              
        if "srikanth" in s:
            s=s.replace("srikanth","sec ")                       
        if "cotan" in s:
            s=s.replace("cotan","cot")    
        if "cosine" in s:
            s=s.replace("cosine","cos")
        if "sine" in s:
            s=s.replace("sine","sin")
        if "tangent" in s:
            s=s.replace("tangent","tan")
        if "cosecant" in s:
            s=s.replace("cosecant","cosec")
        if "secant" in s:
            s=s.replace("secant","sec")
        if "cotangent" in s:
            s=s.replace("cotangent","cot")
        if "sin inverse" in s:
            s=s.replace("sin inverse","asin ")
        if "cos inverse" in s:
            s=s.replace("cos inverse","acos ")
        if "tan inverse" in s:
            s=s.replace("tan inverse","atan ")
        if "cosec inverse" in s:
            s=s.replace("cosec inverse","acosec ")
        if "sec inverse" in s:
            s=s.replace("sec inverse","asec ")
        if "cot inverse" in s:
            s=s.replace("cot inverse","acot ")
        if "hukum" in s:
            s=s.replace("hukum","cbrt")    
        else:
            print(s)
            if "parenthesis" in s:
                s=s.replace("parenthesis","packet")
            if "differentiatiln" in s:
                s=s.replace("differentiatiln","packet")
            if "franchises" in s:
                s=s.replace("franchises","packet")
            if "differences" in s:
                s=s.replace("differences","packet")
            if "/ranches" in s:
                s=s.replace("/ranches","packet") 
            if "franchise" in s:
                s=s.replace("franchise","packet") 
            if "characteristics" in s:
                s=s.replace("characteristics","packet")             
            if "francis" in s:
                s=s.replace("francis","packet") 
            if "/races" in s:
                s=s.replace("/races","packet") 
            if "parents is" in s:
                s=s.replace("parents is","packet") 
            if "parents is" in s:
                s=s.replace("parents","packet")
            if "rameses" in s:
                s=s.replace("rameses","packet")
            if "france" in s:
                s=s.replace("france","packet") 
            if t == "calc":
                try:
                    if "log" in s or "!" in s or "tan" in s or "sin" in s or "cos" in s or "tan" in s or "e" in s or "ln" in s or "sqrt" in s or "cbrt" in s or "pi" in s:                                                     
                        if "**" in s:
                            s=s.replace("**","^ ")
                        if "*" in s:
                            s=s.replace("*","x")
                        t = s.split()
                        def num(n):
                            try:
                                p = float(n)
                                return True
                            except:
                                return False
                        def goat(n):
                            if "." in n:
                                return "float"
                            elif num(n) == True:
                                return "int"
                            elif num(n) == False:
                                return "other"
                        i = 0
                        s = ""
                        for word in t:                            
                            if word == "sin":
                                s = s+" sin ("
                                i+=1                                          
                            elif goat(word) == "int":  
                                x = t.index(word)   
                                try:
                                    x-=1
                                    chkword = t[x]
                                    if goat(chkword) == "int" or goat(chkword) == "float": 
                                        x+=1
                                        word = t[x]
                                        s = s.rstrip()
                                        s = s+word+" "   
                                    else:
                                        s = s+" "+word+" "
                                except:
                                    pass
                            elif word == "cos":
                                s = s+" cos ("
                                i+=1
                            elif word == "tan":
                                s = s+" tan ("
                                i+=1
                            elif word == "cosec":
                                s = s+" cosec ("
                                i+=1
                            elif word == "sec":
                                s = s+" sec ("
                                i+=1
                            elif word == "cot":
                                s = s+" cot ("
                                i+=1
                            elif word == "asin":
                                s = s+" asin ("
                                i+=1
                            elif word == "acos":
                                s = s+" acos ("
                                i+=1
                            elif word == "atan":
                                s = s+" atan ("
                                i+=1
                            elif word == "acosec":
                                s = s+" acosec ("
                                i+=1
                            elif word == "asec":
                                s = s+" asec ("
                                i+=1
                            elif word == "acot":
                                s = s+" acot ("
                                i+=1
                            elif word == "log":
                                s = s+" log ("
                                i+=1
                            elif word == "ln":
                                s = s+" ln ("
                                i+=1
                            elif word == "packet":
                                z=0
                                g = ""
                                for z in range(0,i,1):
                                    g = g+")"
                                s = s+g
                                i = 0
                            else:
                                s=s+" "+word+" "
                        k = list(s.split())                      
                        def call(i):            
                            if k[i] == "(":
                                i+=1
                                p,i = call(i)
                                return p,i                
                            elif k[i] == "sin":
                                i+=1                                
                                try:
                                    p,i = call(i)
                                    if self.pee == "deg":
                                        p = np.deg2rad(p)
                                    else:
                                        p = p
                                    a = math.sin(p)
                                    return a,i
                                except:
                                    pass
                            elif k[i] == "cos":
                                i+=1                                
                                try:
                                    p,i = call(i)
                                    if self.pee == "deg":
                                        p = np.deg2rad(p)
                                    else:
                                        p = p
                                    a = math.cos(p)
                                    return a,i
                                except:
                                    pass
                            elif k[i] == "tan":
                                i+=1                                
                                try:
                                    p,i = call(i)
                                    if self.pee == "deg":
                                        p = np.deg2rad(p)
                                    else:
                                        p = p
                                    a = math.tan(p)
                                    return a,i
                                except:
                                    pass
                            elif k[i] == "cosec":
                                i+=1                                
                                try:
                                    p,i = call(i)
                                    if self.pee == "deg":
                                        p = np.deg2rad(p)
                                    else:
                                        p = p
                                    a = math.sin(p)                                    
                                    a = 1/a
                                    return a,i
                                except:
                                    pass
                            elif k[i] == "sec":
                                i+=1                                
                                try:
                                    p,i = call(i)
                                    if self.pee == "deg":
                                        p = np.deg2rad(p)
                                    else:
                                        p = p
                                    a = math.cos(p)
                                    a = 1/a
                                    return a,i
                                except:
                                    pass
                            elif k[i] == "cot":
                                i+=1                                
                                try:
                                    p,i = call(i)
                                    if self.pee == "deg":
                                        p = np.deg2rad(p)
                                    else:
                                        p = p
                                    a = math.tan(p)
                                    a = 1/a
                                    return a,i
                                except:
                                    pass
                            elif k[i] == "asin":
                                i+=1                                
                                try:
                                    p,i = call(i)
                                    a = np.arcsin(p)
                                    return a,i
                                except:
                                    pass
                            elif k[i] == "acos":
                                i+=1                                
                                try:
                                    p,i = call(i)
                                    a = np.arccos(p)
                                    return a,i
                                except:
                                    pass
                            elif k[i] == "atan":
                                i+=1                                
                                try:
                                    p,i = call(i)
                                    a = np.arctan(p)
                                    return a,i
                                except:
                                    pass
                            elif k[i] == "acosec":
                                i+=1                                
                                try:
                                    p,i = call(i)
                                    a = np.arcsin(p)
                                    a = 1/a
                                    return a,i
                                except:
                                    pass
                            elif k[i] == "asec":
                                i+=1                                
                                try:
                                    p,i = call(i)
                                    a = np.arccos(p)
                                    a = 1/a
                                    return a,i
                                except:
                                    pass
                            elif k[i] == "acot":
                                i+=1                                
                                try:
                                    p,i = call(i)
                                    a = np.arctan(p)
                                    a = 1/a
                                    return a,i
                                except:
                                    pass
                            elif k[i] == "log":
                                i+=1                                
                                try:
                                    p,i = call(i)
                                    a = math.log10(p)
                                    return a,i
                                except:
                                    pass
                            elif k[i] == "ln":
                                i+=1                                
                                try:
                                    p,i = call(i)
                                    a = math.log(p)
                                    return a,i
                                except:
                                    pass                            
                            elif k[i] == "sqrt":
                                i+=1                                
                                try:
                                    p,i = call(i)
                                    a = math.sqrt(p)
                                    return a,i
                                except:
                                    pass
                            elif k[i] == "cbrt":
                                i+=1                                
                                try:
                                    p,i = call(i)
                                    a = p**(1/3)
                                    return a,i
                                except:
                                    pass
                            elif k[i] == "e":
                                a = math.e
                                try:
                                    i+=1
                                    def ont(a,i):
                                        if k[i] == "+":
                                            i+=1                                
                                            try:
                                                p,i = call(i)
                                                a = a+p
                                                i+=1
                                                a,i = ont(a,i)
                                            except:
                                                pass
                                        elif k[i] == "-":
                                            i+=1                                
                                            try:
                                                p,i = call(i)
                                                a = a-p
                                                i+=1
                                                a,i = ont(a,i)
                                            except:
                                                pass
                                        elif k[i] == "x":
                                            i+=1                                
                                            try:
                                                p,i = call(i)
                                                a = a*p
                                                i+=1
                                                a,i = ont(a,i)
                                            except:
                                                pass
                                        elif k[i] == "/":
                                            i+=1                                
                                            try:
                                                p,i = call(i)
                                                a = a/p
                                                i+=1
                                                a,i = ont(a,i)
                                            except:
                                                pass
                                        elif k[i] == "^":
                                            i+=1                                
                                            try:
                                                p,i = call(i)
                                                a = a**p
                                                i+=1
                                                a,i = ont(a,i)
                                            except:
                                                pass
                                        elif k[i] == "!":   
                                            try:
                                                a = math.gamma(a+1)
                                                i+=1
                                                a,i = ont(a,i)
                                            except:
                                                pass    
                                        else:
                                            i-=1
                                        return a,i
                                    a,i = ont(a,i)
                                    return a,i
                                except:
                                    return a,i            
                            elif k[i] == "pi":
                                a = 3.14159265359
                                try:
                                    i+=1
                                    def otn(a,i):
                                        if k[i] == "+":
                                            i+=1                                
                                            try:
                                                p,i = call(i)
                                                a = a+p
                                                i+=1
                                                a,i = otn(a,i)
                                            except:
                                                pass
                                        elif k[i] == "-":
                                            i+=1                                
                                            try:
                                                p,i = call(i)
                                                a = a-p
                                                i+=1
                                                a,i = otn(a,i)
                                            except:
                                                pass
                                        elif k[i] == "x":
                                            i+=1                                
                                            try:
                                                p,i = call(i)
                                                a = a*p
                                                i+=1
                                                a,i = otn(a,i)
                                            except:
                                                pass
                                        elif k[i] == "/":
                                            i+=1                                
                                            try:
                                                p,i = call(i)
                                                a = a/p
                                                i+=1
                                                a,i = otn(a,i)
                                            except:
                                                pass
                                        elif k[i] == "^":
                                            i+=1                                
                                            try:
                                                p,i = call(i)
                                                a = a**p
                                                i+=1
                                                a,i = otn(a,i)
                                            except:
                                                pass
                                        elif k[i] == "!":   
                                            try:
                                                a = math.gamma(a+1)
                                                i+=1
                                                a,i = otn(a,i)
                                            except:
                                                pass  
                                        elif k[i] == ")":
                                            pass
                                        else:
                                            i-=1
                                        return a,i
                                    a,i = otn(a,i)
                                    return a,i
                                except:
                                    return a,i                              
                            elif num(k[i]) == True:
                                a = float(k[i])
                                try:
                                    i-=1
                                    if k[i] == "^":
                                        i+=1 
                                        return a,i
                                    elif k[i] == "sqrt":
                                        i+=1
                                        return a,i
                                    else:
                                        i+=1
                                        try:
                                            i+=1
                                            def ton(a,i):
                                                if k[i] == "+":
                                                    i+=1                                
                                                    try:
                                                        p,i = call(i)
                                                        a = a+p
                                                        i+=1
                                                        a,i = ton(a,i)
                                                    except:
                                                        pass
                                                elif k[i] == "mod":
                                                    i+=1                                
                                                    try:
                                                        p,i = call(i)
                                                        a = a%p
                                                        i+=1
                                                        a,i = ton(a,i)
                                                    except:
                                                        pass
                                                elif k[i] == "%":
                                                    i-=1                                
                                                    try:
                                                        a = float(k[i])
                                                        a = a/100
                                                        i+=2
                                                        a,i = ton(a,i)
                                                    except:
                                                        pass
                                                elif k[i] == "-":
                                                    i+=1                                
                                                    try:
                                                        p,i = call(i)
                                                        a = a-p
                                                        i+=1
                                                        a,i = ton(a,i)
                                                    except:
                                                        pass
                                                elif k[i] == "x":
                                                    i+=1                                
                                                    try:
                                                        p,i = call(i)
                                                        a = a*p
                                                        i+=1
                                                        a,i = ton(a,i)
                                                    except:
                                                        pass
                                                elif k[i] == "/":
                                                    i+=1                                
                                                    try:
                                                        p,i = call(i)
                                                        a = a/p
                                                        i+=1
                                                        a,i = ton(a,i)
                                                    except:
                                                        pass
                                                elif k[i] == "^":
                                                    i+=1                                
                                                    try:
                                                        p,i = call(i)
                                                        a = a**p
                                                        i+=1
                                                        a,i = ton(a,i)
                                                    except:
                                                        pass
                                                elif k[i] == "!":   
                                                    i-=1
                                                    try:
                                                        a = float(k[i])
                                                        a = math.gamma(a+1)
                                                        i+=2
                                                        a,i = ton(a,i)
                                                    except:
                                                        pass
                                                elif k[i] == ")":
                                                    pass    
                                                else:
                                                    i-=1
                                                return a,i
                                            a,i = ton(a,i)
                                            return a,i
                                        except:
                                            return a,i          
                                except:
                                    try:
                                        i+=1
                                        def ton(a,i):
                                            if k[i] == "+":
                                                i+=1                                
                                                try:
                                                    p,i = call(i)
                                                    a = a+p
                                                    i+=1
                                                    a,i = ton(a,i)
                                                except:
                                                    pass
                                            elif k[i] == "mod":
                                                i+=1                                
                                                try:
                                                    p,i = call(i)
                                                    a = a%p
                                                    i+=1
                                                    a,i = ton(a,i)
                                                except:
                                                    pass
                                            elif k[i] == "%":
                                                i-=1                                
                                                try:
                                                    a = float(k[i])
                                                    a = a/100
                                                    i+=2
                                                    a,i = ton(a,i)
                                                except:
                                                    pass
                                            elif k[i] == "-":
                                                i+=1                                
                                                try:
                                                    p,i = call(i)
                                                    a = a-p
                                                    i+=1
                                                    a,i = ton(a,i)
                                                except:
                                                    pass
                                            elif k[i] == "x":
                                                i+=1                                
                                                try:
                                                    p,i = call(i)
                                                    a = a*p
                                                    i+=1
                                                    a,i = ton(a,i)
                                                except:
                                                    pass
                                            elif k[i] == "/":
                                                i+=1                                
                                                try:
                                                    p,i = call(i)
                                                    a = a/p
                                                    i+=1
                                                    a,i = ton(a,i)
                                                except:
                                                    pass
                                            elif k[i] == "^":
                                                i+=1                                
                                                try:
                                                    p,i = call(i)
                                                    a = a**p
                                                    i+=1
                                                    a,i = ton(a,i)
                                                except:
                                                    pass
                                            elif k[i] == "!":   
                                                i-=1
                                                try:
                                                    a = float(k[i])
                                                    a = math.gamma(a+1)
                                                    i+=2
                                                    a,i = ton(a,i)
                                                except:
                                                    pass  
                                            elif k[i] == ")":
                                                pass   
                                            else:
                                                i-=1
                                            return a,i
                                        a,i = ton(a,i)
                                        return a,i
                                    except:
                                        return a,i             
                        def ok(a,i):
                            if k[i] == "+":
                                i+=1
                                b,i = call(i)
                                ans = a + b
                                a = ans
                            elif k[i] == "-":
                                i+=1
                                b,i = call(i)
                                ans = a - b
                                a = ans
                            elif k[i] == "x":
                                i+=1
                                b,i = call(i)
                                ans = a*b
                                a = ans
                            elif k[i] == "/":
                                i+=1
                                b,i = call(i)
                                ans = a/b
                                a = ans    
                            elif k[i] == "^":
                                i+=1
                                b,i = call(i)
                                ans = a**b
                                a = ans  
                            elif k[i] == "!":
                                i+=1
                                a = float(a)
                                ans = math.gamma(a+1)
                                a = ans          
                            elif k[i] == "sqrt":
                                i+=1
                                a = float(a)
                                ans = math.sqrt(a)
                                a = ans     
                            elif k[i] == "cbrt":
                                i+=1
                                a = float(a)
                                ans = a**(1/3)
                                a = ans          
                            return a,i                         
                        try:
                            j = len(k)
                            a,i = call(0)
                            def toki(a,i):
                                try:
                                    if i<j:
                                        i+=1
                                        d,i = ok(a,i)
                                        a,i = d,i
                                    return a,i
                                except:
                                    return a,i
                            while i<j:
                                a,i = toki(a,i)
                            ro=round(a,4)
                            if ro == 0.0 or ro == -0.0:
                                a = 0.0
                            b = str(a)                            
                            self.root.ids.inp.text=s
                            self.root.ids.ans.text=b                             
                            threading.Thread(target=self.sayans, args=(b,)).start()   
                            self.his(s,b)         
                        except:
                            b = "Math Error"
                            self.root.ids.inp.text=s
                            self.root.ids.ans.text=b
                    else:
                        t = s.split()
                        def num(n):
                            try:
                                p = float(n)
                                return True
                            except:
                                return False
                        def goat(n):
                            if "." in n:
                                return "float"
                            elif num(n) == True:
                                return "int"
                            elif num(n) == False:
                                return "other"
                        i = 0
                        s = ""
                        f = ""
                        for word in t:
                            if goat(word) == "int":  
                                x = t.index(word)   
                                try:
                                    x-=1
                                    chkword = t[x]
                                    if goat(chkword) == "int" or goat(chkword) == "float": 
                                        x+=1
                                        word = t[x]
                                        s = s.rstrip()
                                        f = f.rstrip()
                                        s = s+word+" "   
                                        f = f+word+" "
                                    else:
                                        s = s+" "+word+" "
                                        f = f+" "+word+" "
                                except:
                                    pass
                            elif word == "mod": 
                                s = s+" "+"%"+" "
                                f = f+" "+word+" "
                            elif word == "%": 
                                s = s+" "+"/ 100"+" "
                                f = f+" "+"%"+" "
                            else:
                                s = s+" "+word+" "
                                f = f+" "+word+" "
                        b = str(eval(s))
                        if "**" in s:
                            f=f.replace("**","^ ")
                        elif "*" in s:
                            f=f.replace("*","x")
                        self.root.ids.inp.text=f
                        self.root.ids.ans.text=b     
                        threading.Thread(target=self.sayans, args = (b,)).start()  
                        self.his(s,b)
                except:
                    if "**" in s:
                        s=s.replace("**","^ ")
                    elif "*" in s:
                        s=s.replace("*","x")    
                    self.root.ids.inp.text=s
                    self.root.ids.ans.text="Math Error" 
    @mainthread
    def check2(self,s,t):     
        # derivative and anti derivative calz   
        if "factorial" in s:
            s=s.replace("factorial","!")             
        if "secund" in s:
            s=s.replace("secund","sec ")             
        if "one" in s:
            s=s.replace("one","1 ")             
        if "zero" in s:
            s=s.replace("zero","0 ")             
        if "hero" in s:
            s=s.replace("hero","0 ")             
        if "two" in s:
            s=s.replace("two","2")             
        if "free" in s:
            s=s.replace("free","3")             
        if "nayan" in s:
            s=s.replace("nayan","9")             
        if "plus" in s:
            s=s.replace("plus","+")             
        if "does" in s:
            s=s.replace("does","+")   
        if "core" in s:
            s=s.replace("core","4")             
        if "by" in s:
            s=s.replace("by","/")             
        if "b" in s:
            s=s.replace("b","/")             
        if "bi" in s:
            s=s.replace("bi","/")                     
        if "du/ai" in s:
            s=s.replace("du/ai","2 /")                     
        if "10,000" in s:
            s=s.replace("10,000","10000")             
        if "tree" in s:
            s=s.replace("tree","3")             
        if "into" in s:
            s=s.replace("into","*")             
        if "to" in s:
            s=s.replace("to","2")             
        if "tu" in s:
            s=s.replace("tu","2")             
        if "bhai" in s:
            s=s.replace("bhai","/")
        if "why" in s:
            s=s.replace("why","y")             
        if "power" in s:
            s=s.replace("power","**")             
        if "four" in s:
            s=s.replace("four","4")             
        if "square root" in s:
            s=s.replace("square root","sqrt")                     
        if "cu/e root" in s:
            s=s.replace("cu/e root","cbrt")             
        if "cu/e" in s:
            s=s.replace("cu/e","** 3")             
        if "qu/e root" in s:
            s=s.replace("qu/e root","cbrt")             
        if "root" in s:
            s=s.replace("root","sqrt")             
        if "route" in s:
            s=s.replace("route","sqrt ")             
        if "square" in s:
            s=s.replace("square","** 2")             
        if "2 kyln" in s:
            s=s.replace("2 kyln","2 ** 3")             
        if "sign" in s:
            s=s.replace("sign","sin ")             
        if "science" in s:
            s=s.replace("science","sin ")             
        if "shine" in s:
            s=s.replace("shine","sin ")             
        if "ten" in s:
            s=s.replace("ten","10")             
        if "loan" in s:
            s=s.replace("loan","ln ")
        if "learn" in s:
            s=s.replace("learn","ln ")             
        if "cars" in s:
            s=s.replace("cars","cos ")             
        if "qrs" in s:
            s=s.replace("qrs","cos ")             
        if "cause" in s:
            s=s.replace("cause","cos")             
        if "you2/e" in s:
            s=s.replace("you2/e","e ** 3")             
        if "loggy" in s:
            s=s.replace("loggy","log e")             
        if "and 2" in s:
            s=s.replace("and 2","* 2")             
        if "land" in s:
            s=s.replace("land","ln")             
        if "lan" in s:
            s=s.replace("lan","ln")             
        if "lawn" in s:
            s=s.replace("lawn","ln")             
        if "loan" in s:
            s=s.replace("loan","ln")             
        if "lock" in s:
            s=s.replace("lock","log")             
        if "logi" in s:
            s=s.replace("logi","log e")             
        if "how" in s:
            s=s.replace("how","log")             
        if "ready for" in s:
            s=s.replace("ready for","34")             
        if "loni" in s:
            s=s.replace("loni","ln e")             
        if "long" in s:
            s=s.replace("long","ln ")             
        if "lon" in s:
            s=s.replace("lon","ln ")             
        if "dog" in s:
            s=s.replace("dog","log ")      
        if "lock" in s:
            s=s.replace("lock","log ")
        if "lan" in s:
            s=s.replace("lan","ln ")             
        if "fore" in s:
            s=s.replace("fore","4")             
        if "log10" in s:
            s=s.replace("log10","log 10")             
        if "shiny" in s:
            s=s.replace("shiny","sin e")              
        if "tany" in s:
            s=s.replace("tany","tan e")              
        if "tani" in s:
            s=s.replace("tani","tan e")              
        if "dani" in s:
            s=s.replace("dani","tan e")             
        if "kashi" in s:
            s=s.replace("kashi","cos e")              
        if "kasi" in s:
            s=s.replace("kasi","cos e")             
        if "cosy" in s:
            s=s.replace("cosy","cos e")             
        if "11 10" in s:
            s=s.replace("11 10","ln 10")             
        if "helen" in s:
            s=s.replace("helen","ln ")             
        if "ellen" in s:
            s=s.replace("ellen","ln ")             
        if "on" in s:
            s=s.replace("on","ln ")             
        if "minus" in s:
            s=s.replace("minus","-")             
        if "curse" in s:
            s=s.replace("curse","cos ")             
        if "cost" in s:
            s=s.replace("cost","cos ")                
        if "three" in s:
            s=s.replace("three","3")                
        if "launch" in s:
            s=s.replace("launch","ln ")                     
        if "caught" in s:
            s=s.replace("caught","cot ")
        if "hot" in s:
            s=s.replace("hot","cot ")             
        if "got" in s:
            s=s.replace("got","cot ")             
        if "ekant" in s:
            s=s.replace("ekant","sec ")            
        if "cottage" in s:
            s=s.replace("cottage","cot ")             
        if "kota agent" in s:
            s=s.replace("kota agent","cotangent ")             
        if "check" in s :
            s=s.replace("check","sec ")             
        if "point" in s:
            s=s.replace("point",".")             
        if "call" in s:
            s=s.replace("call","cos ")             
        if "sin0" in s:
            s=s.replace("sin0","sin 0")             
        if "2x" in s:
            s=s.replace("2x","2 * ")             
        if "and" in s:
            s=s.replace("and","")             
        if "kottayam" in s:
            s=s.replace("kottayam","cotangent ")              
        if "agent" in s:
            s=s.replace("agent"," ")             
        if "kaushik" in s:
            s=s.replace("kaushik","cosec ")              
        if "srikanth" in s:
            s=s.replace("srikanth","sec ")                 
        if "cosine" in s:
            s=s.replace("cosine","cos")             
        if "sine" in s:
            s=s.replace("sine","sin")             
        if "tangent" in s:
            s=s.replace("tangent","tan")             
        if "cosecant" in s:
            s=s.replace("cosecant","cosec")             
        if "secant" in s:
            s=s.replace("secant","sec")             
        if "cotangent" in s:
            s=s.replace("cotangent","cot")
        if "cotan" in s:
            s=s.replace("cotan","cot")             
        if "sin inverse" in s:
            s=s.replace("sin inverse","asin ")              
        if "cos inverse" in s:
            s=s.replace("cos inverse","acos ")              
        if "tan inverse" in s:
            s=s.replace("tan inverse","atan ")              
        if "cosec inverse" in s:
            s=s.replace("cosec inverse","acosec ")              
        if "sec inverse" in s:
            s=s.replace("sec inverse","asec ")              
        if "cot inverse" in s:
            s=s.replace("cot inverse","acot ")      
        else:               
            print(s)
            if "parenthesis" in s:
                s=s.replace("parenthesis","packet")
            if "differentiatiln" in s:
                s=s.replace("differentiatiln","packet")
            if "franchises" in s:
                s=s.replace("franchises","packet")
            if "differences" in s:
                s=s.replace("differences","packet")
            if "franchise" in s:
                s=s.replace("franchise","packet")
            if "/ranches" in s:
                s=s.replace("/ranches","packet") 
            if "characteristics" in s:
                s=s.replace("characteristics","packet") 
            if "/races" in s:
                s=s.replace("/races","packet")            
            if "francis" in s:
                s=s.replace("francis","packet")   
            if "parents is" in s:
                s=s.replace("parents is","packet")
            if "parents" in s:
                s=s.replace("parents","packet")
            if "rameses" in s:
                s=s.replace("rameses","packet")
            if "france" in s:
                s=s.replace("france","packet")    
            def num(n):
                try:
                    p = float(n)
                    return True
                except:
                    return False
            def goat(n):
                if "." in n:
                    return "float"
                elif num(n) == True:
                    return "int"
                elif num(n) == False:
                    return "other"       
            q = s.split()
            u = enumerate(q)
            s=""
            f=""
            i=0
            for value, word in u:
                if word == "sin":
                    s = s+" sin ("
                    f = f+" sin ("
                    i+=1                             
                elif goat(word) == "int":  
                    x = value   
                    try:
                        x-=1
                        chkword = q[x]
                        if goat(chkword) == "float": 
                            x+=1
                            word = q[x]
                            s = s.rstrip()
                            s = s+word+" "  
                            f = f.rstrip()
                            f = f+word+" "
                        else:
                            x+=1
                            word = q[x]
                            s = s+" "+word+" "
                            f = f+" "+word+" "
                    except:
                        pass           
                elif word == "cos":
                    s = s+" cos ("
                    f = f+" cos ("
                    i+=1
                elif word == "tan":
                    s = s+" tan ("
                    f = f+" tan ("
                    i+=1
                elif word == "cosec":
                    s = s+" cosec ("
                    f = f+" cosec ("
                    i+=1
                elif word == "sec":
                    s = s+" sec ("
                    f = f+" sec ("
                    i+=1
                elif word == "cot":
                    s = s+" cot ("
                    f = f+" cot ("
                    i+=1
                elif word == "log":
                    s = s+" log ("
                    f = f+" log ("
                    i+=1
                elif word == "ln":
                    s = s+" ln ("
                    f = f+" ln ("
                    i+=1
                elif word == "asin":
                    s = s+" asin ("
                    f = f+" asin ("
                    i+=1
                elif word == "acos":
                    s = s+" acos ("
                    f = f+" acos ("
                    i+=1
                elif word == "atan":
                    s = s+" atan ("
                    f = f+" atan ("
                    i+=1
                elif word == "acosec":
                    s = s+" acosec ("
                    f = f+" acosec ("
                    i+=1
                elif word == "asec":
                    s = s+" asec ("
                    f = f+" asec ("
                    i+=1
                elif word == "acot":
                    s = s+" acot ("
                    f = f+" acot ("
                    i+=1
                elif word == "sqrt":
                    s = s+" sqrt ("
                    f = f+" sqrt ("
                    i+=1
                elif word == "cbrt":
                    s = s+" cbrt ("
                    f = f+" cbrt ("
                    i+=1
                elif word == "packet":
                    g = ""
                    for z in range(0,i,1):
                        g = g+")"
                    s = s+g
                    f = f+g
                    i = 0             
                else:
                    if goat(word) == "other":
                        if word != "+" and  word != "-" and word != "/" and word != "**" and word != "*" and word != "^" and word != ".":                            
                            x = value
                            x-=1
                            if x>=0:
                                chkword = q[x]
                                if  chkword != "cbrt" and chkword != "sqrt" and chkword != "acot" and chkword != "asec" and chkword != "acosec" and chkword != "atan" and chkword != "acos" and chkword != "asin" and chkword != "cot" and chkword != "sec" and chkword != "cosec" and chkword != "tan" and chkword != "cos" and chkword != "sin" and chkword != "+" and chkword != "-" and chkword != "/" and chkword != "**" and chkword != "*"and chkword != "." and chkword != "sin" and chkword != "cos" and chkword != "tan" and chkword != "log" and chkword != "ln" and chkword != "sec" and chkword != "cosec" and chkword != "cot" and chkword != "e" and chkword != "^":
                                    s = s.rstrip()
                                    s = s+" * "+word+" "  
                                    f = f.rstrip()
                                    f = f+" * "+word+" "
                                else:
                                    s = s+" "+word+" "
                                    f = f+" "+word+" "
                            else:
                                s = s+" "+word+" "
                                f = f+" "+word+" "
                        else:
                            s = s+" "+word+" "
                            f = f+" "+word+" "
                    else:
                        s = s+" "+word+" "
                        f = f+" "+word+" "
            if "**" in s:
                v = s.split()
                if v[0] == "*":
                    s = s.lstrip("*")
                    f = f.lstrip("*")
                f=f.replace("**","^")
            if "*" in s:
                v = s.split()
                if v[0] == "*":
                    s = s.lstrip("*")
                    f = f.lstrip("*")
                f=f.replace("*",".")
            if t == "anti":
                try: 
                    x = symbols('x')
                    e = symbols('e')
                    y = symbols('y')
                    z = symbols('z')
                    s=str(s)
                    o=str(sp.integrate(s,x))
                    b = o
                    if "Integral" in o:
                        b="Sorry! Integral cannot be found for the given input!!!"
                    else:
                        b=b+" + C"
                    if "**" in b:
                        b=b.replace("**","^")
                    if "*" in b:
                        b=b.replace("*",".")
                    self.root.ids.inp3.text=f
                    self.root.ids.ans3.text=b
                    self.his(f,b)
                except:
                    self.root.ids.inp3.text=f
                    self.root.ids.ans3.text="Math Error"
            else:
                try: 
                    x = symbols('x')
                    e = symbols('e')
                    y = symbols('y')
                    z = symbols('z')
                    s=str(s)
                    o=str(Derivative(s,x).doit())
                    b = o
                    if "**" in b:
                        b=b.replace("**","^")
                    if "*" in b:
                        b=b.replace("*",".")
                    self.root.ids.inp2.text=f
                    self.root.ids.ans2.text=b
                    self.his(f,b)
                except:
                    self.root.ids.inp2.text=f
                    self.root.ids.ans2.text="Math Error"
    def sayans(self,b):
        Speak = Dispatch('SAPI.Spvoice')
        Speak.Voice = Speak.GetVoices().Item(2)
        Speak.Rate = 1
        Speak.Volume = 90
        Speak.speak(b)
    def his(self,a,b):        
        p=a+"\n= "+b+"\n" 
        today = str(date.today())
        with open("history.txt",'a+') as f:            
            f.write(f"# {p} ({today})\n\n")
        self.root.ids.his.text = open("history.txt").read()
if __name__=="__main__":
    LabelBase.register(name="bold", fn_regular="F:\\PYPRO\\rsp project\\font\\Kanit"
                                               "-bold.ttf")
    LabelBase.register(name="diff", fn_regular="F:\\PYPRO\\rsp project\\font\\Orbit"
                                               "-Regular.ttf")
    LabelBase.register(name="good", fn_regular="F:\\PYPRO\\rsp project\\font\\Oswald"
                                               "-Regular.ttf")
    LabelBase.register(name="s", fn_regular="F:\\PYPRO\\rsp project\\font\\RobotoSlab"
                                               "-Bold.ttf")
    LabelBase.register(name="f", fn_regular="F:\\PYPRO\\rsp project\\font\\Diphylleia"
                                               "-Regular.ttf")
    LabelBase.register(name="g", fn_regular="F:\\PYPRO\\rsp project\\font\\Kalam"
                                               "-Regular.ttf")
    LabelBase.register(name="o", fn_regular="F:\\PYPRO\\rsp project\\font\\Poppins"
                                               "-Medium.ttf")
    LabelBase.register(name="u", fn_regular="F:\\PYPRO\\rsp project\\font\\Itim"
                                               "-Regular.ttf")  
    LabelBase.register(name="p", fn_regular="F:\\PYPRO\\rsp project\\font\\Itim"
                                               "-Regular.ttf")                                          
    Damszt().run()