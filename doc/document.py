from typing import Dict

from PIL import Image, ImageDraw, ImageFont


class Alignment:
    def __init__(self,
                 right: int,
                 left: int,
                 top: int,
                 bottom: int,
                 line_space: int):
        self.right: int = right
        self.left: int = left
        self.top: int = top
        self.bottom: int = bottom
        self.line_space: int = line_space

    def get_horizontal_border(self):
        return self.left + self.right

    def get_vertical_border(self):
        return self.top + self.bottom

    def get_padded_image(self, page:Page):
        width = width + self.left + self.right
        height = self.top + self.bottom + height
        return Image.new("RGB", (width, height), (255, 255, 255))


class Page:
    def __init__(self,
                 width: int,
                 height: int,
                 line_space: int,
                 structure: Dict,
                 font_path: str):
        self._width: int = width
        self._height: int = height
        self._line_space: int = line_space
        self._structure = structure
        self.LINE = "line"
        self.TABLE = "table"
        self._font_path = font_path
        self._pointer = (0, 0, 0, 0)

    def add_item(self, structure: Dict):
        self._structure = structure

    def draw_header(self, draw):
        draw.text((0, 0), self._structure['department'])

    def draw(self):
        image = Image.new("RGBA", (self._width, self._height), (255, 255, 255, 0))
        image_draw = ImageDraw.Draw(image)
        self.draw_header(image_draw)
        return image

    def size(self):
        return self._width, self._height


class Document:
    def __init__(self, alignment: Alignment):
        self._page: list = []
        self._width: int = 0
        self._height: int = 0
        self._background: tuple = (255, 255, 255)
        self._alignment: Alignment = alignment

    def add_page(self, page: Page):
        padded_image =
        self._page.append(page)
        pw, ph = page.size()
        self._height += ph

    def save(self, output: str):
        image = Image.new("RGB", (self._width, self._height), self._background)
        start = 0
        for item in self._page:
            new_image = item.draw()
            image.paste(new_image, (0, start), new_image)
            start += item.size()[1]
        image.save(output)


if __name__ == "__main__":
    alignment = Alignment(10, 10, 10, 10, 10)
    font_path = r''
    page: Page = Page(width=100,
                      height=100,
                      line_space=5,
                      structure={},
                      font_path=font_path)
    document = Document(alignment=alignment)
    document.add_page(page)
    document.add_page(page1)
    document.save(r"D:\python_project\doc_image\test\abc.jpg")
