from typing import List
from PIL import ImageFont
from functional.font_line_splitting import FontLineSplitting


class TableDrawer:
    def __int__(self,
                structure: List,
                width: int,
                font: ImageFont):
        self._structure: List = structure
        self._row = len(self._structure)
        self._column = len(self._structure[0])
        self._width: int = width
        self._column_width: float = self._width / self._column
        self._font: ImageFont = font
        self._font_splitting: FontLineSplitting = FontLineSplitting(self._font)

    def draw(self):
        for row in self._structure:
            for column in row:
                pass

