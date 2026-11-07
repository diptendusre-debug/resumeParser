from pypdf import PdfReader 
from docx import Document
from pathlib import Path
import os



def readResume():
    resumeData=[]
    currentDir = Path(__file__).resolve().parent
    print("Current Working Directory********",currentDir)
    if not currentDir:
        print("Current Directory does not exists")
    for file in currentDir.iterdir():
        if file.suffix.lower() in ['.pdf','.docx']:
            text=""
            if file.is_file() and file.suffix.lower()==".pdf":
                reader=PdfReader(file)
                for page in reader.pages:
                    text += page.extract_text()
            if file.suffix.lower()==".docx":
                doc=Document(file)
                for paragraph in doc.paragraphs:
                    text+=paragraph.text
            resumeData.append({
                "filename": file.name,
                "content": text
            })  
    if not resumeData:
            raise ValueError("No Resume Found")
    return resumeData




    


