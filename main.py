# Import the python text to speech library and the PDF REader library
import pyttsx3
import PyPDF2

# Read the PDF file binary mode
pdf_file = open('test.pdf', 'rb')
read_pdf = PyPDF2.PdfReader(pdf_file, strict=False)
# Find the number of pages in the PDF document
number_of_pages = len(read_pdf.pages)
# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()
for i in range(4, number_of_pages):
    # Read the PDF page
    page = read_pdf.pages[i]

    # Extract the text of the PDF page
    page_content = page.extract_text()

    # set the audio speed and volume
    newrate = 200
    engine.setProperty('rate', newrate)
    newvolume = 200
    engine.setProperty('volume', newvolume)

    # say method on the engine that passing input text to be spoken
    engine.say(page_content)

    # run and wait method to processes the voice commands.
    engine.runAndWait()