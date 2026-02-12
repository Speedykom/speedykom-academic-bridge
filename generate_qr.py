#!/usr/bin/env python3
"""Generate QR code for presentation access"""

import qrcode
from PIL import Image

# URL to encode
url = "https://speedykom.github.io/speedykom-academic-bridge/"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data
qr.add_data(url)
qr.make(fit=True)

# Create image with SpeedyKom colors
img = qr.make_image(fill_color="#1e3a5f", back_color="white")

# Save the QR code
output_path = "images/qr_code.png"
img.save(output_path)

print(f"✅ QR code generated successfully!")
print(f"📍 Saved to: {output_path}")
print(f"🔗 URL: {url}")
