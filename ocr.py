import os
from PIL import Image


files = os.listdir('/home/wh/script')
png = []
for f in files:
    if f[-3:] == 'png':
        png.append(f)

# jpeg = []
# for i in png:
#     conv = Image.open(i).convert('L')
#     conv.save(i[:-4] + '.jpeg')
#     jpeg.append(i[:-4] + '.jpeg')

# for f in jpeg:
for f in png:
    print(f)
    os.popen('tesseract ' + str(f) + ' result')
    text = file('result.txt').read().strip()
    print(text)
