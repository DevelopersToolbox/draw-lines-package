"""
Documentation to go here
"""

import shutil

from wolfsoftware.drawlines import draw_line  # pylint: disable=import-error


def test_draw_line_default() -> None:
    """Test Line Length"""
    result: str = draw_line()
    assert result.strip() == '-' * (shutil.get_terminal_size().columns - 1)  # nosec: B101


def test_draw_line_with_text() -> None:
    """Test Line Length"""
    result: str = draw_line(text="Hello", position="center", width=50)
    assert "Hello" in result  # nosec: B101


def test_draw_line_left() -> None:
    """Test Line Length"""
    result: str = draw_line(text="Hello", position="left", width=50)
    assert result.startswith("-- Hello")  # nosec: B101


def test_draw_line_right() -> None:
    """Test Line Length"""
    result: str = draw_line(text="Hello", position="right", width=50)
    assert result.endswith("Hello --")  # nosec: B101


def test_draw_line_with_color() -> None:
    """Test Line Length"""
    result: str = draw_line(text="Hello", position="center", width=50, color="red")
    assert '\033[' in result  # nosec: B101


def test_draw_line_with_bold() -> None:
    """Test Line Length"""
    result: str = draw_line(text="Hello", position="center", width=50, bold=True)
    assert '\033[' in result  # nosec: B101
