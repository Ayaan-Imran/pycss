# Pycss
Pycss is a module that will help you to colorise your output in the terminal.
This module also allows you to do a variety of logic opertations on various color formats, such as RGB and Hex color codes.

## How does it work?
Pycss uses ANSI color codes.
Read about the [ANSI codes](https://en.wikipedia.org/wiki/ANSI_escape_code).

**Note**: This module may not work wih certain terminals as they may not support ANSI color codes.

## Installation
To install the `pycss` module, use the following command:
```commandline
pip install pycss
```
Import `pycss` with the following code snippet:
```python
# Not pycss
import css
```

## Documentation
Before the documentation starts, you should be familiar with css colors.
### Inbuilt foreground colors
You can access the css colors by refferring to the color variables `css.COLORNAME`.  

**Note:** The css colors are 3-bit and 4-bit colors. If your terminal does not support 3-bit and 4-bit colors, it will not be able to understand them.

| Variable  | Color          |
|-----------|----------------|
| GREY      | Grey           |
| RED       | Red            |
| GREEN     | Green          |
| YELLOW    | Yellow         |
| BLUE      | Blue           |
| MAGENTA   | Magenta        |
| CYAN      | Cyan           |
| WHITE     | White          |
| NOCOLOR   | Transparent    |
| C_BLACK   | Bright Black   |
| C_RED     | Bright Red     |
| C_YELLOW  | Bright Yellow  |
| C_GREEN   | Bright Green   |
| C_BLUE    | Bright Blue    |
| C_MAGENTA | Bright Magenta |
| C_CYAN    | Bright Cyan    |
| C_WHITE   | Bright White   |

### Inbuilt background colors
You can access the css background colors by refferring to the background color variables `css.BGCOLORNAME`.  

**Note:** The css background colors are 3-bit and 4-bit colors. If your terminal does not support 3-bit and 4-bit colors, it will not be able to understand them.
`css.BACKROUND_COLOR`

| Variable    | Color          |
|-------------|----------------|
| BGGREY      | Grey           |
| BGRED       | Red            |
| BGGREEN     | Green          |
| BGYELLOW    | Yellow         |
| BGBLUE      | Blue           |
| BGMAGENTA   | Magenta        |
| BGCYAN      | Cyan           |
| BGWHITE     | White          |
| C_BGBLACK   | Bright Black   |
| C_BGRED     | Bright Red     |
| C_BGYELLOW  | Bright Yellow  |
| C_BGGREEN   | Bright Green   |
| C_BGBLUE    | Bright Blue    |
| C_BGMAGENTA | Bright Magenta |
| C_BGCYAN    | Bright Cyan    |
| C_BGWHITE   | Bright White   |

### Using external foreground colors
If you want to use a specific foreground color with your text output, you can
use the `pycss` inbiult functions to convert hex or RGB color codes to 
usable ANSI color codes: `hex2color()` or `rgb2color()`.  

**Note:** The ANSI color code that will be returned by the above functions is 24-bit. If your terminal does not support 24-bit colors, it will not be able to understand them.

```python
import css

# Hex code
hex_code = "#FFF"
ansi_color_code = css.hex2color(hex_code)

# RGB color
red, green, blue = 255, 255, 255
ansi_color_code = css.rgb2color(red, green, blue)

# The ansi_color_code can also be used with the color() function. 
# Scroll down to learn more.
```

### Using external background colors
If you want to use a specific background color with your text output, you can
use the `pycss` inbiult functions to convert hex or RGB color codes to 
usable ANSI color codes: `hex2bgcolor()` or `rgb2bgcolor()`.  

**Note:** The ANSI color code that will be returned by the above functions is 24-bit. If your terminal does not support 24-bit colors, it will not be able to understand them.

```python
import css

# Hex code
hex_code = "#FFF"
ansi_color_code = css.hex2bgcolor(hex_code)

# RGB color
red, green, blue = 255, 255, 255
ansi_color_code = css.rgb2bgcolor(red, green, blue)

# The ansi_color_code can also be used with the bgcolor() function. 
# Scroll down to learn more.
```

### Coloring the text
To color text, you use the `color()` function.  
> Parameters
> 1. text - The text you want colored.
> 2. color - Pass in the color you desire. It can either be an inbuilt foreground color or an external foreground color. 

**Returns:**  
Returns a string with your colored text.

```python
import css

# Inbuilt color (3-bit and 4-bit color)
colored_text = css.color("Hello World!", css.RED)
print(colored_text)

# External color (24-bit true color)
hex_color = "#d62828"
ansi_color_code = css.hex2color(hex_color)
colored_text = css.color("Hello World!", ansi_color_code)
print(colored_text)
```

### Applying background
To apply background to text, you use the `bgcolor()` function.

> Parameters
> 1. text - The text you want to be colored
> 2. background_color - Pass in the background color you desire. It can either be an inbuilt background color or an external background color.  

**Note:** You don't use normal strings for background colors eg: "red".USE pycss's background color!

**Returns:**  
Returns a string with your background-applied text.

```python
import css

# Inbuilt color (3-bit and 4-bit color)
colored_text = css.bgcolor("Hello World!", css.BGRED)
print(colored_text)

# External color (24-bit true color)
hex_color = "#d62828"
ansi_color_code = css.hex2color(hex_color)
colored_text = css.bgcolor("Hello World!", ansi_color_code)
print(colored_text)
```

### Making text bold
To make text bold, you use the `bold()` function.

> Parameter
> 1. text - The text you want bold.

**Returns:**
It returns a string containing the bolded text.

```python
import css

bolded_text = css.bold("Hello World!")
print(bolded_text)
```

### Underlining text
To underline text, you use the `underline()` function.

> Parameter
> 1. text - The text you want to be underlined

**Returns:**
It returns a string containing the underlined text.

```python
import css

underlined_text = css.underline("Hello World!")
print(underlined_text)
```

### Converting color formats
`pycss` has functions that allows you to convert between Hex color codes and RGB color codes.

#### Hex to RGB
To convert hex color codes into RGB color codes, use the `hex2rgb()` function.

> Parameter
> 1. hex_code - The hex code you want converted.

**Returns:**
This function returns a tuple with the format (red, green, blue) to represent RGB.

```python
import css

# Convert hex code
hex_code = "#ffc300"
rgb = css.hex2rgb(hex_code)

# Extract red, green, and blue from rgb
red, green, blue = rgb[0], rgb[1], rgb[2]

# Print them out
print("Red:", red)
print("Green:", green)
print("Blue:", blue)
print("RGB color code:", rgb)
```
```
Red: 255
Green: 195
Blue: 0
RGB color code: (255, 195, 0)
```

#### RGB to hex
To convert RGB color codes into hex color codes, use the `rgb2hex()` function.

> Parameters
> 1. red - The red value in RGB.
> 2. green - The green value in RGB.
> 3. blue - The blue value in RGB.

**Returns:**
This function returns a string with the converted hex code.

```python
import css

# Convert RGB color code
red, green, blue = 255, 195, 0
hex_code = css.rgb2hex(red, green, blue)

# Print the converted hex_code out
print(hex_code)
```
```
#ffc300
```