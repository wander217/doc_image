from PIL import ImageFont


class FontLineSplitting:
    def __init__(self, font: ImageFont):
        self._font = font

    def text_2_line(self, line_width: int, text: str):
        words = text.split(" ")
        lines = []
        text_lines, length = [], 0
        for word in words:
            w, h = self._font.getsize(word)
            if w > line_width:
                if len(text_lines) > 0:
                    lines.append(" ".join(text_lines))
                    length = 0
                    text_lines.clear()
                character_text = []
                character_length = 0
                for character in word:
                    cw, ch = self._font.getsize(character)
                    if character_length + cw > line_width:
                        lines.append("".join(character_text))
                        character_length = 0
                        character_text.clear()
                    else:
                        character_text.append(character)
                        character_length += cw
            elif length + w > line_width:
                lines.append(" ".join(text_lines))
                length = 0
                text_lines.clear()
            else:
                text_lines.append(word)
                length += w
        if len(text_lines) > 0:
            lines.append(" ".join(text_lines))
        return lines


if __name__ == "__main__":
    font = ImageFont.truetype(r"D:\python_project\doc_image\font\time_new_roman.ttf", 18)
    alphabet = FontLineSplitting(font)
    print(alphabet.text_2_line(100, "abcd _"*10))

