"""
This module provides utilities for drawing colored lines in the terminal.

The `draw_line` function can be used to create lines with optional text
positioned to the left, center, or right, with customizable colors and styles.
"""

import shutil
import re

import colorama

# Define color constants using colorama
BLACK: str = colorama.Fore.BLACK
BLUE: str = colorama.Fore.BLUE
CYAN: str = colorama.Fore.CYAN
GREEN: str = colorama.Fore.GREEN
GREY: str = colorama.Fore.LIGHTBLACK_EX
MAGENTA: str = colorama.Fore.MAGENTA
RED: str = colorama.Fore.RED
WHITE: str = colorama.Fore.WHITE
YELLOW: str = colorama.Fore.YELLOW

BOLD: str = colorama.Style.BRIGHT
RESET: str = colorama.Style.RESET_ALL


def __get_first_character(text: str) -> str:
    """
    Extract and return the first character of the given string.

    If the input string is empty or None, returns an empty string.

    Args:
        text (str): The input string from which the first character is to be extracted.

    Returns:
        str: The first character of the input string, or an empty string if the input is empty or None.
    """
    if text:
        return text[0]
    return ''


def __validate_and_configure(text: str,  # pylint: disable=too-many-arguments
                             position: str,
                             fill_char: str,
                             pad: int,
                             width: int,
                             color: str) -> dict:
    """
    Validate input parameters and configure settings for line drawing.

    Args:
        text (str): The text to include in the line.
        position (str): The position of the text ('left', 'right', or 'center').
        fill_char (str): Character used to fill the line.
        pad (int): Number of padding characters to the left or right of the text.
        width (int): The width of the line.
        color (str): The color code for the text.

    Returns:
        dict: A dictionary with the validated and configured settings.
    """
    # Define ANSI color codes using a dictionary
    colors: dict[str, str] = {
        'black': BLACK,
        'blue': BLUE,
        'cyan': CYAN,
        'green': GREEN,
        'grey': GREY,
        'magenta': MAGENTA,
        'red': RED,
        'white': WHITE,
        'yellow': YELLOW,
        'bold': BOLD,
        'reset': RESET
    }

    if width == 0:
        return {'terminal_width': 0, 'display_text': ''}

    # Get the width of the terminal
    if width < 0:
        terminal_width: int = shutil.get_terminal_size().columns - 1
    else:
        terminal_width = width

    # If text is empty, return a single unbroken line with no spaces
    if not text:
        text = ''
        fill_char = __get_first_character(fill_char)
        return {
            'text': text,
            'position': position,
            'fill_char': fill_char,
            'pad': pad,
            'terminal_width': terminal_width,
            'color_code': '',
            'reset_code': '',
            'display_text': fill_char * terminal_width
        }

    # Get the first character of the fill_char
    fill_char = __get_first_character(fill_char)

    # Set color and style if specified
    color_code: str = ''
    if color:
        sanitized_color: str = re.sub(r'[^a-zA-Z+]', '', color).lower()  # Remove everything except alphabetic characters and '+', and convert to lowercase
        parts = sanitized_color.split('+')
        if len(parts) > 2 or (len(parts) == 2 and 'bold' not in parts):
            raise ValueError("Invalid color format. Use 'color', 'color+bold', or 'bold'.")

        color_code = ''
        for part in parts:
            if part in colors:
                color_code += colors[part]
            else:
                raise ValueError(f"Invalid color component '{part}'. Allowed values are: {', '.join(colors.keys())}")

    reset_code: str = colors['reset'] if color_code else ''

    return {
        'text': text,
        'position': position,
        'fill_char': fill_char,
        'pad': pad,
        'terminal_width': terminal_width,
        'color_code': color_code,
        'reset_code': reset_code
    }


def __draw_line(config: dict) -> str:
    """
    Draw the line based on the configuration settings.

    Args:
        config (dict): A dictionary with the validated and configured settings.

    Returns:
        str: The constructed line string.
    """
    text: str = config['text']
    position: str = config['position']
    fill_char: str = config['fill_char']
    pad: int = config['pad']
    terminal_width: int = config['terminal_width']
    color_code: str = config['color_code']
    reset_code: str = config['reset_code']
    display_text: str = ''

    # Adjust text with padding characters and space conditionally based on padding counts
    if position == 'left':
        display_text = f"{fill_char * pad}{' ' if pad > 0 else ''}{color_code}{text}{reset_code} "
    elif position == 'right':
        display_text = f" {color_code}{text}{reset_code}{' ' if pad > 0 else ''}{fill_char * pad}"
    else:
        display_text = f" {color_code}{text}{reset_code} "  # Center position always has space around text for visual balance

    text_len: int = len(display_text) - len(color_code) - len(reset_code)  # Adjust text length excluding color codes

    if text_len >= terminal_width:
        # If text is too long, just return the text
        return f"{color_code}{display_text}{reset_code}"

    if position == 'left':
        # Text flush left
        return f"{display_text}{fill_char * (terminal_width - text_len)}"
    if position == 'right':
        # Text flush right
        return f"{fill_char * (terminal_width - text_len)}{display_text}"

    # Center text
    left_padding: int = (terminal_width - text_len) // 2
    right_padding: int = terminal_width - text_len - left_padding
    return f"{fill_char * left_padding}{display_text}{fill_char * right_padding}"


def draw_line(text: str = '',  # pylint: disable=too-many-arguments
              position: str = 'center',
              fill_char: str = '-',
              pad: int = 2,
              width: int = -1,
              color: str = '') -> str:
    """
    Draw a line across the terminal with optional text in a specified position.

    Args:
        text (str): The text to include in the line. Defaults to ''.
        position (str): The position of the text ('left', 'right', or 'center'). Defaults to 'center'.
        fill_char (str): Character used to fill the line and for padding prefixes and postfixes. Defaults to '-'.
        pad (int): Number of padding characters to the left or right of the text. Defaults to 2.
        width (int): The width of the line. Defaults to terminal width if set to -1.
        color (str): The color code for the text. Supports combinations like 'cyan+bold'. Defaults to '' (no color).

    Returns:
        str: The constructed line string.
    """
    config: dict = __validate_and_configure(text, position, fill_char, pad, width, color)
    if 'display_text' in config:
        return config['display_text']
    return __draw_line(config)
