# Errors
class ColourNotFound(ValueError):
    pass

# Basic colors
GREY = "\u001b[30m"
RED = "\u001b[31m"
GREEN = "\u001b[32m"
YELLOW = "\u001b[33m"
BLUE = "\u001b[34m"
MAGENTA = "\u001b[35m"
CYAN = "\u001b[36m"
WHITE = "\u001b[37m"
NOCOLOR = "\u001b[0m"

# Bright colors
C_GREY = "\u001b[30;1m"
C_RED = "\u001b[31;1m"
C_GREEN = "\u001b[32;1m"
C_YELLOW = "\u001b[33;1m"
C_BLUE = "\u001b[34;1m"
C_MAGENTA = "\u001b[35;1m"
C_CYAN = "\u001b[36;1m"
C_WHITE = "\u001b[37;1m"

# Basic background colors
BGGREY = "\u001b[40m"
BGRED = "\u001b[41m"
BGGREEN = "\u001b[42m"
BGYELLOW = "\u001b[43m"
BGBLUE = "\u001b[44m"
MGMAGENTA = "\u001b[45m"
BGCYAN = "\u001b[46m"
BGWHITE = "\u001b[47m"

# Bright background colors
C_BGGREY = "\u001b[40;1m"
C_BGRED = "\u001b[41;1m"
C_BGGREEN = "\u001b[42;1m"
C_BGYELLOW = "\u001b[43;1m"
C_BGBLUE = "\u001b[44;1m"
C_MGMAGENTA = "\u001b[45;1m"
C_BGCYAN = "\u001b[46;1m"
C_BGWHITE = "\u001b[47;1m"

def color(text:str, color):
    """
    This function will make your text colorful
    :param text: String
    :param color: pycss color
    :return: Colored text
    """

    color_list = [GREY, RED, GREEN, YELLOW, CYAN, WHITE, BLUE, C_GREY, C_RED, C_GREEN, C_YELLOW, C_CYAN, C_WHITE, C_BLUE]
    if color not in color_list:
        raise ColourNotFound("The color you passed is not valid")
    else:
        return f"{color}{text}{NOCOLOR}"

def bgcolor(text:str, background_color):
    """
    This function will apply a background color on your text
    :param text: String
    :param background_color: pycss background color
    :return: Background color on the text
    """
    color_list = [BGGREY, BGRED, BGGREEN, BGYELLOW, BGCYAN, BGWHITE, BGBLUE, C_BGGREY, C_BGRED, C_BGGREEN, C_BGYELLOW, C_BGCYAN, C_BGWHITE, C_BGBLUE]

    if background_color not in color_list:
        raise ColourNotFound("The color you passed is not valid")
    else:
        return f"{background_color}{text}{NOCOLOR}"

def bold(text:str):
    """
    This function will make your text bold
    :param text: String
    :return: Bold text
    """

    return f"\u001b[1m{text}{NOCOLOR}"

def underline(text:str):
    """
    This function will make your text underlined
    :param text: String
    :return: Underlined text
    """

    return f"\u001b[4m{text}{NOCOLOR}"

def rgb2hex(red:int, green:int, blue:int):
    """
    This function convert RGB color codes to hex color codes
    :param red: The red value in RGB
    :param green: The green value in RGB
    :param blue: The blue valie in RGB
    :return: The converted hex color code
    """

    # Check if RGB value is valid
    if (red < 0) or (green < 0) or (blue < 0) or (red > 255) or (green > 255) or (blue > 255):
        print(underline(bold("Length error")))
        print()
        print(color("[!] Your RGB value(s) is not in range of 0-255.", RED))
        quit()

    # Local variables
    corresponding_letters = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }

    # Convert red, green, blue values to hex
    red = f"{corresponding_letters[int(red / 16)]}{corresponding_letters[red % 16]}"
    green = f"{corresponding_letters[int(green / 16)]}{corresponding_letters[green % 16]}"
    blue = f"{corresponding_letters[int(blue / 16)]}{corresponding_letters[blue % 16]}"

    # Compile them
    hex_code = f"#{red}{green}{blue}"

    return hex_code
