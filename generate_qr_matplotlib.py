import qrcode
import matplotlib.pyplot as plt

# Define the URL
url = "https://speedykom.github.io/speedykom-academic-bridge/"

# Generate the QR Code
qr = qrcode.QRCode(version=1, box_size=10, border=2)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Display it as a plot
plt.figure(figsize=(6, 6))
plt.imshow(img, cmap="gray")
plt.axis("off")

# Save to file
plt.savefig("images/qr_code.png", bbox_inches="tight", pad_inches=0)
print("✅ QR Code generated using Matplotlib logic and saved to images/qr_code.png")
