import textract
import os

def get_text_from_doc(file_path):
    """
    Extracts text from a .doc file using textract.
    """
    try:
        text = textract.process(file_path).decode('utf-8')  # Decode bytes to string
        return text
    except textract.exceptions.ExtensionNotSupported as e:
        print(f"Error: .doc format not directly supported by textract.  You may need antiword installed.")
        print(e)
        return None
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def get_author_from_doc(file_path):
    """
    Attempts to extract author information from a .doc file.
    This is a simplified example and might need adjustments based on
    the specific structure of your .doc files.
    """
    text = get_text_from_doc(file_path)
    if text:
        # This is a very basic example.  You'll likely need to adapt this
        # to your specific document format.  Look for patterns in the text
        # that indicate the author.
        lines = text.splitlines()
        for line in lines:
            if "Author:" in line:
                return line.split("Author:")[1].strip()
            if "Authors:" in line:
                return line.split("Authors:")[1].strip()
        return "Author not found"
    else:
        return None

# Example usage:
path = r"Z:\iacss\IACSS_IJCSS\IJCSS\Volumes\Vol242025Ed1\1-Plain Papers\Final_Revised_Article.doc"
print(path)
author = get_author_from_doc(path)

if author:
    print(f"Author: {author}")
else:
    print("Could not retrieve author information.")