"""
wolfsoftware.drawlines.

A simple Python package to draw lines across the terminal with optional text in specified positions.

Modules:
--------
drawlines.py : Contains the primary function `draw_line` for drawing lines with optional text and formatting.

Functions:
----------
draw_line(text='', position='center', fill_char='-', left_pad=2, right_pad=2, width=-1, color='', bold=True):
    Draws a line across the terminal with optional text in a specified position and formatting options.

Example Usage:
--------------
>>> from wolfsoftware.drawlines import draw_line
>>> print(draw_line(text="Hello", position="center", fill_char="*", width=50, color="red", bold=True))
"""

from .drawlines import draw_line

__all__: list[str] = ['draw_line']
