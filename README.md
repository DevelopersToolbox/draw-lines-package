<!-- markdownlint-disable -->
<p align="center">
    <a href="https://github.com/DevelopersToolbox/">
        <img src="https://cdn.wolfsoftware.com/assets/images/github/organisations/developerstoolbox/black-and-white-circle-256.png" alt="DevelopersToolbox logo" />
    </a>
    <br />
    <a href="https://github.com/DevelopersToolbox/draw-lines-package/actions/workflows/cicd.yml">
        <img src="https://img.shields.io/github/actions/workflow/status/DevelopersToolbox/draw-lines-package/cicd.yml?branch=master&label=build%20status&style=for-the-badge" alt="Github Build Status" />
    </a>
    <a href="https://github.com/DevelopersToolbox/draw-lines-package/blob/master/LICENSE.md">
        <img src="https://img.shields.io/github/license/DevelopersToolbox/draw-lines-package?color=blue&label=License&style=for-the-badge" alt="License">
    </a>
    <a href="https://github.com/DevelopersToolbox/draw-lines-package">
        <img src="https://img.shields.io/github/created-at/DevelopersToolbox/draw-lines-package?color=blue&label=Created&style=for-the-badge" alt="Created">
    </a>
    <br />
    <a href="https://github.com/DevelopersToolbox/draw-lines-package/releases/latest">
        <img src="https://img.shields.io/github/v/release/DevelopersToolbox/draw-lines-package?color=blue&label=Latest%20Release&style=for-the-badge" alt="Release">
    </a>
    <a href="https://github.com/DevelopersToolbox/draw-lines-package/releases/latest">
        <img src="https://img.shields.io/github/release-date/DevelopersToolbox/draw-lines-package?color=blue&label=Released&style=for-the-badge" alt="Released">
    </a>
    <a href="https://github.com/DevelopersToolbox/draw-lines-package/releases/latest">
        <img src="https://img.shields.io/github/commits-since/DevelopersToolbox/draw-lines-package/latest.svg?color=blue&style=for-the-badge" alt="Commits since release">
    </a>
    <br />
    <a href="https://github.com/DevelopersToolbox/draw-lines-package/blob/master/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/DevelopersToolbox/draw-lines-package/blob/master/.github/CONTRIBUTING.md">
        <img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/DevelopersToolbox/draw-lines-package/blob/master/.github/SECURITY.md">
        <img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/DevelopersToolbox/draw-lines-package/issues">
        <img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge" />
    </a>
</p>

## Overview

A Python module for drawing styled and colored lines in the terminal. This utility allows for the customization of line styles, colors, and text positioning, making it a versatile tool for enhancing the output of CLI applications.

## Features

- Customizable text positions: left, right, or center.
- Support for various text colors and styles including bold.
- Adjustable line width and padding.
- Uses `colorama` for color and style handling, ensuring compatibility across different operating systems.

## Installation

```shell
pip install wolfsoftware.drawlines
```

## Usage

The main functionality is provided by the `draw_line` function, which can be used to create lines in the terminal with or without text.

### Function Signature

```python
def draw_line(text='', position='center', fill_char='-', pad=2, width=-1, color=''):
    """
    Draw a line across the terminal with optional text.

    Args:
        text (str): Text to include in the line. Defaults to '' (no text).
        position (str): Position of the text ('left', 'right', 'center'). Defaults to 'center'.
        fill_char (str): Character used to fill the line. Defaults to '-'.
        pad (int): Padding characters around the text. Defaults to 2.
        width (int): Total width of the line; defaults to the terminal width if set to -1.
        color (str): Color and style of the text, e.g., 'red', 'blue+bold'. Defaults to no color.
    """
```

### Examples

#### 1. Simple line with default settings

```python
from your_module import draw_line

# Draw a simple dashed line
print(draw_line())
```

#### Output

```shell
------------------------------------------------------------------------------------------
```

#### 2. Line with centered text and custom color

```python
# Draw a line with centered text
print(draw_line(text="Hello, World!", position='center'))
```

#### Output

```shell
------------------------------------- Hello, World! --------------------------------------
```
> If you set the `fill_char=' '` you will simply get centered text with no line.

#### 3. Line with left-aligned text and custom fill character

```python
# Draw a line with left-aligned text and asterisk fill character
print(draw_line(text="Left aligned text", position='left', fill_char='*'))
```

#### Output

```shell
** Left aligned text *********************************************************************
```

## Customization

This section provides details on how you can customize the `draw_line` function parameters. Below is a table listing each parameter, its default value, purpose, and allowed values:

| Name      | Default Value | Purpose                                                                                        | Allowed Values                                                                                                                                                                                                    |
| :-------- | :-----------: | :--------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| text      | ''            | Any string you want to display within the line.                                                | Any string                                                                                                                                                                                                        |
| position  | 'center'      | Where to place the text.                                                                       | 'left', 'center', 'right'                                                                                                                                                                                         |
| fill_char | '-'           | The character to use when drawing the line. If more than one is given, only the first is used. | Any single character                                                                                                                                                                                              |
| left_pad  | 2             | How many fill_chars to use as a prefix when aligning the text left.                            | Any positive integer                                                                                                                                                                                              |
| right_pad | 2             | How many fill_chars to use as a postfix when aligning the text right.                          | Any positive integer                                                                                                                                                                                              |
| width     | -1            | How wide to draw the line. Defaults to the terminal's width minus one if not specified.        | Any integer; -1 for terminal width minus 1                                                                                                                                                                        |
| color     | ''            | What color to make the text.                                                                   | 'bold', 'black', 'blue', 'cyan', 'green', 'grey', 'magenta', 'red', 'white', 'yellow', 'black+bold', 'blue+bold', 'cyan+bold', 'green+bold', 'grey+bold', 'magenta+bold', 'red+bold', 'white+bold', 'yellow+bold' |
| bold      | False         | Should the text be bold. This can be used with or without a defined color.                     | True, False                                                                                                                                                                                                       |

> If you are adding bold to a color it **must** come after the color name. E.b. cyan+bold **NOT** bold+cyan as this will cause an exception to be thrown.

<br />
<p align="right"><a href="https://wolfsoftware.com/"><img src="https://img.shields.io/badge/Created%20by%20Wolf%20on%20behalf%20of%20Wolf%20Software-blue?style=for-the-badge" /></a></p>
