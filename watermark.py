import os
import sys

from PIL import Image

EXTS = ('.jpg', '.png','.jpeg')

logo = Image.open("logo.png")
logoWidth = logo.width
logoHeight = logo.height
pos = 'center'

for filename in os.listdir("./images"):
    if any([filename.lower().endswith(ext) for ext in EXTS]) and filename != "logo.png":
        image = Image.open('./images/' + filename)
        imageWidth = image.width
        imageHeight = image.height

        try:
            if pos == 'topleft':
                image.paste(logo, (0, 0))
            elif pos == 'topright':
                image.paste(logo, (imageWidth - logoWidth, 0),logo)
            elif pos == 'bottomleft':
                image.paste(logo, (0, imageHeight - logoHeight))
            elif pos == 'bottomright':
                image.paste(logo, (imageWidth - logoWidth, imageHeight - logoHeight))
            elif pos == 'center':
                image.paste(logo, (int((imageWidth - logoWidth)/2), int((imageHeight - logoHeight)/2)),logo)
            else:
                print('Error: ' + pos + ' is not a valid position')
                print('Usage: watermark.py \'image path\' \'logo path\' [topleft, topright, bottomleft, bottomright, center]')

            image.save('./images/watermarked/' + filename)
            print('Added watermark to ' + '/' + filename)

        except:
            image.paste(logo, ((imageWidth - logoWidth)/2, (imageHeight - logoHeight)/2), logo)
            image.save('./images/watermarked/' + filename)
            print('Added default watermark to ' + '/' + filename)
