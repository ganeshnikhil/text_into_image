from PIL import Image, ImageFont, ImageDraw
from fonts.ttf import Roboto
from Constants.Colors import RGB_TO_COLOR_NAMES
import textwrap


COLOR_NAME_TO_RGB = dict(
   (name.lower(), rgb)
   for rgb, names in RGB_TO_COLOR_NAMES.items()
   for name in names)

def file_name(text):
   return str(abs(hash(text)))

def text_balance(text, width=40):
   wrapper = textwrap.TextWrapper(width=width)
   return wrapper.wrap(text=text)

def convert(text, font_size=29, color='blue', image_file=None, font_name=None):
   if font_name is None:
      font_name = Roboto

   font = ImageFont.truetype(font_name, font_size, encoding='utf-8')
   formatted_text = text_balance(text)
   
   max_width = max(font.getbbox(line)[2] for line in formatted_text)
   total_height = sum(font.getbbox(line)[3] for line in formatted_text)

   image = Image.new('RGBA', (max_width, total_height), (0, 0, 0, 0))
   draw = ImageDraw.Draw(image)
   
   if color not in COLOR_NAME_TO_RGB:
      color = 'black'

   y = 0
   for line in formatted_text:
      draw.text((0, y), line, fill=color, font=font)
      y += font.getbbox(line)[3]

   if image_file is None:
      filename = text.replace(' ', '')
      image_file = 'Image/{}.png'.format(file_name(text))

   image.save(image_file, 'PNG')

if __name__ == "__main__":
   text = "hellow world how are you doing really"
   convert(text, image_file='test.png')
