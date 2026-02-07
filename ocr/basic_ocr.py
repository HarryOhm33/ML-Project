import cv2
import pytesseract
import re

# read image
img = cv2.imread("image.png")

# preprocess
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

# OCR
text = pytesseract.image_to_string(thresh)

print("----- RAW OCR TEXT -----")
print(text)


# -----------------------------
# EMAIL
# -----------------------------
email = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", text)


# -----------------------------
# PHONE
# Handles:
# +91-9876543210
# 9876543210
# numbers with X masking
# -----------------------------
phone = re.search(r"(\+?\d[\d\-\sX]{8,}\d)", text)


# -----------------------------
# NAME
# heuristic:
# first non-empty line
# uppercase & not too long
# -----------------------------
lines = [line.strip() for line in text.split("\n") if line.strip()]

name = None
for line in lines[:5]:  # check top few lines
    if (
        line.isupper()
        and "@" not in line
        and not any(char.isdigit() for char in line)
        and len(line.split()) <= 4
    ):
        name = line
        break


# -----------------------------
# final JSON
# -----------------------------
data = {
    "name": name,
    "email": email.group(0) if email else None,
    "phone": phone.group(0) if phone else None,
}

print("\n----- EXTRACTED JSON -----")
print(data)
