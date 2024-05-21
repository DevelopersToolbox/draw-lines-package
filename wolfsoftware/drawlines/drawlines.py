"""This is the summary line.

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""


import shutil

import colorama

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
    Extract and returns the first character of the given string.

    If the input string is empty or None, returns an empty string.

    Arguments:
        text (str): The input string from which the first character is to be extracted.

    Returns:
        str: The first character of the input string, or an empty string if the input is empty or None.
    """
    if text and len(text) > 0:
        return text[0]
    return ''


def draw_line(text: str = '',  # pylint: disable=too-many-arguments, too-many-locals
              position: str = 'center',
              fill_char: str = '-',
              left_pad: int = 2,
              right_pad: int = 2,
              width: int = -1,
              color: str = '',
              bold: bool = False) -> str:
    """
    Draw a line across the terminal with optional text in a specified position.

    Args:
        text (str): The text to include in the line.
        position (str): The position of the text ('left', 'right', or 'center').
        fill_char (str): Character used to fill the line and for padding prefixes and postfixes.
        left_pad_count (int): Number of padding characters to the left of the text.
        right_pad_count (int): Number of padding characters to the right of the text.
        color (str): The color code for the text.
    """
    display_text: str = ''

    # ANSI color codes
    colors: dict[str, str] = {
        'black': colorama.Fore.BLACK,
        'blue': colorama.Fore.BLUE,
        'cyan': colorama.Fore.CYAN,
        'green': colorama.Fore.GREEN,
        'grey': colorama.Fore.LIGHTBLACK_EX,
        'magenta': colorama.Fore.MAGENTA,
        'red': colorama.Fore.RED,
        'white': colorama.Fore.WHITE,
        'yellow': colorama.Fore.YELLOW,
        'bold': colorama.Style.BRIGHT,
        'reset': colorama.Style.RESET_ALL
    }

    if width == 0:
        print('')
        return ''

    # Get the width of the terminal
    if width == -1:
        terminal_width: int = shutil.get_terminal_size().columns - 1
    else:
        terminal_width = width

    # If text is empty, print a single unbroken line with no spaces
    if not text:
        print(fill_char * terminal_width)
        return fill_char * terminal_width

    fill_char = __get_first_character(fill_char)

    # Set color if specified
    color_code: str = colors.get(color, '') if color else ''
    reset_code: str = colors['reset'] if color or bold else ''

    if bold:
        color_code += colors['bold']

    # Adjust text with padding characters and space conditionally based on padding counts
    if position == 'left':
        display_text = f"{fill_char * left_pad}{' ' if left_pad > 0 else ''}{color_code}{text}{reset_code} "
    elif position == 'right':
        display_text = f" {color_code}{text}{reset_code}{' ' if right_pad > 0 else ''}{fill_char * right_pad}"
    else:
        display_text = f" {color_code}{text}{reset_code} "  # Center position always has space around text for visual balance

    text_len: int = len(display_text) - len(color_code) - len(reset_code)  # Adjust text length excluding color codes

    if text_len >= terminal_width:
        print(f"{color_code}{display_text}{reset_code}")  # If text is too long, just print the text
        return f"{color_code}{display_text}{reset_code}"  # If text is too long, just print the text

    if position == 'left':
        # Text flush left
        print(f"{display_text}{fill_char * (terminal_width - text_len)}")
        return f"{display_text}{fill_char * (terminal_width - text_len)}"
    if position == 'right':
        # Text flush right
        print(f"{fill_char * (terminal_width - text_len)}{display_text}")
        return f"{fill_char * (terminal_width - text_len)}{display_text}"
    # Center text
    left_padding: int = (terminal_width - text_len) // 2
    right_padding: int = terminal_width - text_len - left_padding
    print(f"{fill_char * left_padding}{display_text}{fill_char * right_padding}")
    return f"{fill_char * left_padding}{display_text}{fill_char * right_padding}"
