from PyPDF2 import PdfReader
#from gtts import gTTS
import pyttsx3
import os
from tqdm import tqdm

reader = PdfReader('book.pdf')
finalText = ''

dirname = 'my_folder'
filename = 'myfile'

#   os.makedirs(dirname)
parts = []
def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    print(f"{y}: {text}")
    if y < 600:
        parts.append(text)

counter = 0
engine = pyttsx3.init()
for i in tqdm(range(len(reader.pages))):
    text = reader.pages[i].extract_text(visitor_text=visitor_body)
    finalText += text
    #print(parts)
    if i > 14: 
        print("".join(parts))
        quit()

"""    if i % 30 == 0:
        file_path = os.path.join(dirname, f'{filename}-{counter}.mp3')
        engine.save_to_file(finalText, file_path)
        counter += 1
        engine.runAndWait()"""

#engine.setProperty('rate', 250)

#engine.say(finalText)
#engine.runAndWait()

print('completed')