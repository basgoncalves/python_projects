import qrcode
import os

def generate_qr_code(link, filename="qr_code.png"):
  """Generates a QR code with the given link and saves it as an image.

  Args:
    link: The URL or text to be encoded in the QR code.
    filename: The name of the output image file.
  """
  
  # Create a QR code instance
  qr = qrcode.QRCode(
      version=1,  # Adjust version as needed for larger QR codes
      error_correction=qrcode.constants.ERROR_CORRECT_L  # Adjust error correction level
  )

  # Add the link to the QR code
  qr.add_data(link)

  # Generate the QR code image
  qr.make(fit=True)

  # Create an image from the QR code data
  img = qr.make_image(fill_color="black", back_color="white")

  # Save the image
  img.save(filename)
  
  print(f"QR code saved as {filename}")
  # open file location explorer
  os.system(f"explorer /select,{filename}")

if __name__ == "__main__":
  link = "https://photos.app.goo.gl/HhRTjt4Y7YoSmhx68"
  current_dir = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(current_dir, "Us_cute.png")
  generate_qr_code(link, filename)