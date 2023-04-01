from PyPDF2 import PdfReader
#from gtts import gTTS
import pyttsx3

reader = PdfReader('testing.pdf')
finalText = ''

for page in reader.pages:
    finalText += page.extract_text(0)

#print(finalText)

engine = pyttsx3.init()
engine.setProperty('rate', 250)

#engine.say(finalText)
#engine.runAndWait()

engine.save_to_file(finalText, 'testing.mp3')
engine.runAndWait()
print('completed')