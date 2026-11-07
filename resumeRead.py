from pypdf import PdfReader 
from docx import Document
from pathlib import Path



def readResume():
    resumeData=[]
    currentDir=Path.cwd()
    if not currentDir:
        print("Current Directory does not exists")
    for file in currentDir.iterdir():
        if file.suffix.lower() in ['.pdf','.docx']:
            if file.suffix.lower()==".pdf":
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
            
    return resumeData


    


