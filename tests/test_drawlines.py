"""
Documentation to go here
"""
import shutil

from typing import Optional

import importlib.metadata

import colorama

from wolfsoftware.drawlines import draw_line  # pylint: disable=import-error


def test_version() -> None:
    """
    Test that a version is defined.

    Should return the version of the package.
    """
    version: Optional[str] = None

    try:
        version = importlib.metadata.version('wolfsoftware.drawlines')
    except importlib.metadata.PackageNotFoundError:
        version = None

    assert version is not None, "Version should be set"    # nosec: B101
    assert version != 'unknown', f"Expected version, but got {version}"    # nosec: B101


def test_draw_line_default() -> None:
    """
    Test the default behaviour of draw_line with no parameters.

    Should return a line of default fill character '-' spanning the terminal width.
    """
    result: str = draw_line()
    terminal_width: int = shutil.get_terminal_size().columns - 1

    assert result.strip() == '-' * terminal_width  # nosec: B101


def test_draw_line_with_text() -> None:
    """
    Test draw_line with centered text.

    The text "Hello" should appear in the center of the line with default fill characters.
    """
    result: str = draw_line(text="Hello", position="center", width=50)

    assert "Hello" in result  # nosec: B101
    assert result.strip().startswith("-") and result.strip().endswith("-")  # nosec: B101


def test_draw_line_left() -> None:
    """
    Test draw_line with text positioned to the left.

    The text "Hello" should appear at the left of the line with specified fill characters.
    """
    result: str = draw_line(text="Hello", position="left", width=50)

    assert result.startswith("-- Hello")  # nosec: B101


def test_draw_line_right() -> None:
    """
    Test draw_line with text positioned to the right.

    The text "Hello" should appear at the right of the line with specified fill characters.
    """
    result: str = draw_line(text="Hello", position="right", width=50)

    assert result.endswith("Hello --")  # nosec: B101


def test_draw_line_with_color() -> None:
    """
    Test draw_line with colored text.

    The text "Hello" should appear in red color within the line.
    """
    result: str = draw_line(text="Hello", position="center", width=50, color="red")

    assert '\033[' in result  # nosec: B101


def test_draw_line_with_bold() -> None:
    """
    Test draw_line with bold text.

    The text "Hello" should appear in bold style within the line.
    """
    result: str = draw_line(text="Hello", position="center", width=50, color="bold")

    assert '\033[' in result  # nosec: B101


def test_draw_line_with_color_and_bold() -> None:
    """
    Test draw_line with colored and bold text.

    The text "Hello" should appear in cyan color and bold within the line.
    """
    result: str = draw_line(text="Hello", position="center", width=50, color="cyan+bold")

    assert '\033[' in result  # nosec: B101
    assert colorama.Fore.CYAN in result  # nosec: B101
    assert colorama.Style.BRIGHT in result  # nosec: B101


def test_draw_line_width_zero() -> None:
    """
    Test draw_line with a width of 0.

    Should return an empty string.
    """
    result: str = draw_line(width=0)

    assert result == ""  # nosec: B101


def test_draw_line_width_large() -> None:
    """
    Test draw_line with a very large width.

    Should return a line with the specified width.
    """
    result: str = draw_line(width=200)

    assert len(result) == 200  # nosec: B101


def test_draw_line_fill_char() -> None:
    """
    Test draw_line with a different fill character.

    Should return a line filled with '*' characters.
    """
    result: str = draw_line(fill_char="*", width=50)

    assert result.strip() == '*' * 50  # nosec: B101


def test_draw_line_left_padding() -> None:
    """
    Test draw_line with text positioned to the left and left padding.

    The text "Hello" should appear at the left with specified padding.
    """
    result: str = draw_line(text="Hello", position="left", pad=5, width=50)

    assert result.startswith("----- Hello")  # nosec: B101


def test_draw_line_right_padding() -> None:
    """
    Test draw_line with text positioned to the right and right padding.

    The text "Hello" should appear at the right with specified padding.
    """
    result: str = draw_line(text="Hello", position="right", pad=5, width=50)

    assert result.endswith("Hello -----")  # nosec: B101


def test_draw_line_text_too_long() -> None:
    """
    Test draw_line with text that is too long for the specified width.

    Should handle the long text correctly within the line.
    """
    long_text: str = "This is a very long text that will not fit in the default terminal width" * 2
    result: str = draw_line(text=long_text, width=50)

    assert long_text in result  # nosec: B101


def test_draw_line_centered_text() -> None:
    """
    Test draw_line with centered text.

    The text "Hello" should appear in the center with balanced padding.
    """
    result: str = draw_line(text="Hello", position="center", width=51)
    left_padding: int = (51 - len(" Hello ")) // 2
    right_padding: int = 51 - len(" Hello ") - left_padding

    assert result == f"{'-' * left_padding} Hello {'-' * right_padding}"  # nosec: B101
