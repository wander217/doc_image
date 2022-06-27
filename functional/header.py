from PIL import Image, ImageDraw


class Header:
    def __int__(self, slogan: str, department: str, ):
        self._slogan: str = slogan
        self._department: str = department
        self._image = Image.new('RGB', ())