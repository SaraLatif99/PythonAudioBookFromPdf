import pyttsx3 #importing library pytorch speech to text3
import PyPDF2 #importing library for reading apdf file
book = open('pd.pdf', 'rb') #reading a pdf file
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()