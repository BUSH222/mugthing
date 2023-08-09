from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from rembg import remove
from bs4 import BeautifulSoup


response = requests.get("https://thispersondoesnotexist.com/")
face = Image.open(BytesIO(response.content))


width, height = face.size
face = face.crop((0, 0, width, height))
face_data = remove(face)
face = face_data

new_width = new_height = 700
border_size = 162

newface = Image.new('RGBA', (new_width + border_size * 2, new_height + border_size * 2), (0, 0, 0, 0))
newface.paste(face.resize((new_width, new_height)), (border_size, border_size*2))

background = Image.open("mugshot_background.png")
background = background.resize((width, height))
background.paste(newface, (0, 0), newface)


response2 = requests.get("https://loremflickr.com/1024/1024/thing")

img2 = Image.open(BytesIO(response2.content))
#img2 = img2.resize((1024, 1024))

new_image = Image.new('RGBA', (2048, 1024))

new_image.paste(background, (0, 0))
new_image.paste(img2, (1024, 0))

#new_image.show()
new_image.save('final.png')