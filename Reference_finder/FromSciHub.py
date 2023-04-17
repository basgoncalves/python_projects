import requests
import os

os.chdir(r"C:\Users\Bas\AppData\Local\Mendeley Ltd\Mendeley Desktop\Downloaded")
def download_pdf(url, file_name, headers):

    # Send GET request
    response = requests.get(url, headers=headers)

    # Save the PDF
    if response.status_code == 200:
        with open(file_name, "wb") as f:
            f.write(response.content)
    else:
        print(response.status_code)


if __name__ == "__main__":

    # Define HTTP Headers
    headers = {
        "User-Agent": "Chrome/51.0.2704.103",
    }

    # Define URL of a PDF
    url = "https://sci-hub.hkvisa.net/10.1007/s11517-020-02239-0"

    # Define PDF file name
    file_name = "file1.pdf"

    # Download PDF
    download_pdf(url, file_name, headers)
