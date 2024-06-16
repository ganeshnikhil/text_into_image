
**Creating Text Images with Color and Font Customization**

This Python script provides a convenient way to generate text images with customizable colors, fonts, and formatting. It offers a user-friendly interface for creating visually appealing text-based graphics.

**Key Features:**

- **Color Selection:** Choose from a predefined set of colors using color names (e.g., 'blue', 'red', 'green') or use hex codes for more specific color control.
- **Font Customization:** Employ the `Roboto` font by default, or specify an alternative font path if desired.
- **Text Wrapping:** Automatically wrap long text lines to fit within a defined image width, ensuring proper text placement.
- **Image Creation:** Generates PNG images containing the formatted text.

**Installation:**

1. **Prerequisites:** Ensure you have Python 3 installed on your system. You can verify this by running `python3 --version` in your terminal. If not installed, download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. **Package Dependencies:** This script relies on the following external libraries:
   - Pillow (PIL Fork): Install it using `pip install Pillow` , `pip install textwrap` , `pip install fonts`.

**Usage:**

1. **Import Necessary Modules:**

   ```python
   from PIL import Image, ImageFont, ImageDraw
   from fonts.ttf import Roboto  # Assuming Roboto font is in the 'fonts' directory
   from Constants.Colors import RGB_TO_COLOR_NAMES
   import textwrap
   ```

   - Replace the `fonts.ttf` path with the actual location of your Roboto font file if using a different font.

2. **Color Mapping:**

   The script utilizes a dictionary (`COLOR_NAME_TO_RGB`) to map color names to their corresponding RGB values. This allows for color selection using intuitive names.

3. **`file_name` Function:**

   - Hashes the input text to generate a unique filename for the generated image.

4. **`text_balance` Function:**

   - Employs the `textwrap` module to break down long text into multiple lines that fit within a specified width (default: 40 characters). This ensures proper text wrapping and prevents lines from overflowing the image boundaries.

5. **`convert` Function:**

   - **Parameters:**
     - `text` (str): The text content to be displayed in the image.
     - `font_size` (int, optional): The size of the font (default: 29).
     - `color` (str, optional): The color of the text (default: 'blue'). You can use color names or hex codes.
     - `image_file` (str, optional): The desired filename for the generated image (default: a unique filename based on the text hash).
     - `font_name` (str, optional): The path to an alternative font file (default: 'Roboto').
   - **Functionality:**
     1. Selects the font based on the provided `font_name` (or uses the default `Roboto` font).
     2. Calculates the optimal image dimensions based on the font size and wrapped text lines.
     3. Creates an RGBA image with a transparent background.
     4. Draws the formatted text onto the image using the specified color and font.
     5. Saves the image as a PNG file using the provided `image_file` or a unique filename generated using the `file_name` function.

6. **Example Usage:**

   ```python
   if __name__ == "__main__":
       text = "Hello, world! How are you doing today?"
       convert(text, image_file='my_text_image.png', color='red', font_size=35)
   ```

   This code snippet creates a text image named "my_text_image.png" with the text "Hello, world! How are you doing today?" in red color using a font size of 35.

**Customization:**

- Modify the `COLOR_NAME_TO_RGB` dictionary to add or remove color options.
- Experiment with different font sizes and colors to achieve the desired visual effect.
- Consider using alternative font styles (if provided) to create unique text images.

**Additional Notes:**

- For more advanced text formatting options, explore the capabilities of the `textwrap` module.
- This script provides a basic foundation for creating text images. You can extend it to incorporate features like text alignment, background images, or text effects.
