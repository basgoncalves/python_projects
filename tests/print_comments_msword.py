from docx import Document
from lxml import etree
import zipfile

ooXMLns = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

def get_comments(docxFileName):
  docxZip = zipfile.ZipFile(docxFileName)
  commentsXML = docxZip.read('word/comments.xml')
  et = etree.XML(commentsXML)
  comments = et.xpath('//w:comment',namespaces=ooXMLns)
  for c in comments:
    # attributes:
    print(c.xpath('@w:author',namespaces=ooXMLns))
    print(c.xpath('@w:date',namespaces=ooXMLns))
    # string value of the comment:
    print(c.xpath('string(.)',namespaces=ooXMLns))


# Prompt the user to select a Word document
file_path = input("Enter the path of the Word document: ")
try:
    get_comments(file_path)
except Exception as e:  
    print(f"Error: {e}")
    exit(1)
    
# Load the document
document = Document(file_path)

# Iterate over all the comments in the document
for comment in document.comments:  
    try:
       # Print the comment text
       print(comment.text)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)