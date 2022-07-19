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

        self.img = None
        self.draw = None

        self.producer: str = ''
        self.location: str = ''
        self.extra_info: str = ''
        self.is_organic: bool = False
        self.is_local: bool = False

    def new_img(self):
        colors = self.get_colors()
        self.img = Image.new(mode='RGB', size=(self.width, self.height), color=colors['bg'])
        self.draw = ImageDraw.Draw(self.img)
    
    def make_sign(self):
        self.new_img()
        self.draw_accents()
        self.draw_description()

    def draw_description(self):
        # Center of image
        description_location = (round(self.width / 2), round(self.height / 2))
        description_fnt = ImageFont.truetype('/Library/Fonts/NewYork.ttf', self.font_sizes['description'])
        self.draw.text(description_location, self.description, fill=self.colors['font']['black'], anchor='ms', font=description_fnt)
    
    def draw_price(self):
        price_ftn = ImageFont.truetype('/Library/Fonts/NewYork.ttf', self.font_sizes['price'])
        pass

    def draw_accent_text(self):
        accent_fnt = ImageFont.truetype('/Library/Fonts/NewYork.ttf', self.font_sizes['accent'])
        # producer and location
        pass

    def draw_extra_info(self):
        extra_info_fnt = ImageFont.truetype('/Library/Fonts/NewYork.ttf', self.font_sizes['extra_info'])
        pass

    def display(self):
        self.img.show()

    def draw_accents(self):
        accent_color = self.get_colors()['accent']

        # Top accent
        top_accent_x = (0, 0)
        top_accent_y = (self.width + 1, round(self.height / 6))
        self.draw.rectangle([top_accent_x, top_accent_y], fill=accent_color)

        # Bottom accent
        bottom_accent_x = (0, self.height + 1)
        bottom_accent_y = (self.width + 1, round((self.height / 6) * 5))
        self.draw.rectangle([bottom_accent_x, bottom_accent_y], fill=accent_color)

    def draw_debug(self):
        # Vertical middle line
        self.draw.line([(round(self.width / 2), 0), (round(self.width / 2), self.height)], fill='Blue', width=1)

        # Horizontal middle line
        self.draw.line([(0, round(self.height / 2)), (self.width, round(self.height / 2))], fill='Blue', width=1)

    
    def get_colors(self) -> dict[str, tuple]:
        return {
            'bg': self.colors['main']['local'] if self.is_local else self.colors['main']['reg'],
            'accent': self.colors['accent']['org'] if self.is_organic else self.colors['accent']['conv'],
        }


def main():
    sign = SignMaker('Hot New Product', '$12.99', 'ea')
    sign.is_local = True
    sign.make_sign()
    sign.draw_debug()
    sign.display()

if __name__ == '__main__':
    main()