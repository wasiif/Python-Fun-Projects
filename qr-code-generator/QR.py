import qrcode

# Prompt user for data to encode in QR code
data = input("Enter the data you want to encode in the QR code: ").strip()

# Prompt user for filename
fileName = input("Enter a filename to save the QR code (e.g., 'qrcode.png'): ").strip()

# Generate QR code
img = qrcode.make(data)

# Save QR code as image file
img.save(fileName)

print(f"QR code is saved as {fileName}")
