# fonts.py
import pkg_resources

def get_fonts():
   fonts = []
   for entry_point in pkg_resources.iter_entry_points('fonts_ttf'):
      font_path = entry_point.load()
      fonts.append(font_path)
   return fonts
if __name__ == "__main__":
  print(get_fonts())
