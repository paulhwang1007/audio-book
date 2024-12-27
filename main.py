# Install the following 2 packages:
# pip install pyttsx3
# pip install pyPDF2

import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)

for num in range(0, pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()