"""This module contains the color and formatting codes for the terminal."""
import enum


class ColorCodes(enum.IntEnum):
    """This class contains the color codes for the terminal."""

    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    PURPLE = 35
    CYAN = 36
    WHITE = 37

    def background(self) -> int:
        """Returns the background color code for the color."""
        return self.value + 10


class FormattingCodes(enum.IntEnum):
    """This class contains the formatting codes for the terminal."""

    BOLD = 1
    DIM = 2
    ITALIC = 3
    UNDERLINE = 4
    BLINK = 5
    STRIKETHROUGH = 9
