from docx import Document
import os

def write (content, filename):
    file = Document()
    file.add_paragraph(content)
    file.save("C:/Users/ADMIN/PycharmProjects/pythonProject6/"+filename+".docx")
    os.startfile("C:/Users/ADMIN/PycharmProjects/pythonProject6/"+filename+".docx")