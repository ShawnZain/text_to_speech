import pyttsx3 #used for text-to-speach conversion
import PyPDF2 #used to handle pdf files
from tkinter.filedialog import * #for the askopenfilename() function


"""ask the user which file to convert to mp3
in this line the file that we want to convert to mp3
does not need to be in the same directory as the main.py file
"""
book = askopenfilename()

audio_file_name = input("Enter the file name to save the audio as: ")
audio_file_name += ".mp3"
#read the text stored in the pdf file
pdf_reader = PyPDF2.PdfReader(book)

#initialise the pyttsx3
pdf_sound = pyttsx3.init()

#to change the voice of the tts
voices = pdf_sound.getProperty('voices')
pdf_sound.setProperty('voice', voices[1].id)

#buffer that will store all the text read from the pdf file
pdf_text = ""

for num in range(0, len(pdf_reader.pages)):
    page = pdf_reader.pages[num] #get the page number of the pdf
    text = page.extract_text() #get the text from current page
    clean_text = text.strip().replace('\n', ' ') #remove the \n so that there is no long pause
    pdf_text += clean_text #append the read text to pdf_text

pdf_sound.save_to_file(pdf_text, audio_file_name) #save the mp3
pdf_sound.runAndWait()

pdf_sound.stop()
