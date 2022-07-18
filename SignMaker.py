from tkinter import *
from PIL import Image, ImageDraw, ImageFont

class SignMaker():
    colors = {
        'main': {
            'reg': (255, 255, 255),
            'local': (235, 227, 178),
        },
        'accent': {
            'org': (54, 105, 24),
            'conv': (122, 74, 10),
        },
        'font': {
            'black': (13, 13, 13),
            'white': (255, 255, 255),
        }
    }
    font_sizes = {
        'description': 174,
        'price': 140,
        'extra_info': 90,
        'accent': 62

    }
    height = 1080
    width = 1920

    def __init__(self, description: str, price: str, unit: str) -> None:
        self.description = description
        self.price = price
        self.unit = unit

        self.extra_info: str = ''
        self.is_organic: bool = False
        self.is_local: bool = False
    
    def make_sign(self):
        colors = self.get_colors()
        img = Image.new(mode='RGB', size=(self.width, self.height), color=colors['bg'])
        draw = ImageDraw.Draw(img)
        description_fnt = ImageFont.truetype('/Library/Fonts/NewYork.ttf', self.font_sizes['description'])
        price_ftn = ImageFont.truetype('/Library/Fonts/NewYork.ttf', self.font_sizes['price'])
        extra_info_fnt = ImageFont.truetype('/Library/Fonts/NewYork.ttf', self.font_sizes['extra_info'])
        accent_fnt = ImageFont.truetype('/Library/Fonts/NewYork.ttf', self.font_sizes['accent'])

        # TODO: get specific on centering text
        description_location = (round(self.height / 3), round(self.width / 4))

        draw.text(description_location, self.description, self.colors['font']['black'], description_fnt)
        draw = self.draw_accents(draw)
        img.show()

    def draw_accents(self, draw: ImageDraw):
        accent_color = self.get_colors()['accent']

        # Top accent
        top_accent_x = (0, 0)
        top_accent_y = (self.width + 1, round(self.height / 6))
        draw.rectangle([top_accent_x, top_accent_y], fill=accent_color)

        # Bottom accent
        bottom_accent_x = (0, self.height + 1)
        bottom_accent_y = (self.width + 1, round((self.height / 6) * 5))
        draw.rectangle([bottom_accent_x, bottom_accent_y], fill=accent_color)

        return draw

    
    def get_colors(self) -> dict[str, tuple]:
        return {
            'bg': self.colors['main']['local'] if self.is_local else self.colors['main']['reg'],
            'accent': self.colors['accent']['org'] if self.is_organic else self.colors['accent']['conv'],
        }


def main():
    sign = SignMaker('Hot New Product', '$12.99', 'ea')
    sign.is_local = True
    sign.make_sign()

if __name__ == '__main__':
    main()