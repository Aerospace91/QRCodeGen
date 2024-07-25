import qrcode

# Data to be encoded
data = "https://google.com"

# Create a QR Code instance
qr = qrcode.QRCode(
    version=1,  # version parameter controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
    box_size=10,  # controls how many pixels each “box” of the QR code is
    border=4,  # controls how many boxes thick the border should be
)

# Add data to the instance
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill="black", back_color="white")

# Save the image
img.save("qrcode_example.png")

print("QR code generated and saved as 'qrcode_example.png'")