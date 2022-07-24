"""
A poster maker for gigs and events.

Grabs an image or two (or more), does some processing to make an interesting background
and overlays the following fields to create a poster:

- Event title
- Artist
- Venue
- Event date*
- Event time*
- Description
- Extra info
- Price
- Contact email
- Contact phone

*Provide options for multi day events
"""

from tkinter import *
from PIL import Image, ImageDraw, ImageFont

class PosterBuilder():
    colors = {
        'main': {
            'primary': (255, 255, 255),
            'secondary': (235, 227, 178),
        },
        'accent': {
            'primary': (54, 105, 24),
            'secondary': (122, 74, 10),
        },
        'font': {
            'black': (13, 13, 13),
            'white': (255, 255, 255),
        }
    }
    font_sizes = {
        'artist': 174,
        'venue': 140,
        'datetime': 90,
        'accent': 62

    }
    height = 1080
    width = 1920

    def __init__(self) -> None:
        self.img = None
        self.draw = None

        self.event_title: str = ''
        self.artist: str = ''
        self.venue: str = ''
        self.event_date: str = ''
        self.event_time: str = ''
        self.description: str = ''
        self.extra_info: str = ''
        self.admission_price: str = ''
        self.contact_email: str = ''
        self.contact_phone: str = ''

    def new_img(self):
        colors = self.get_colors()
        self.img = Image.new(mode='RGB', size=(self.width, self.height), color=colors['bg'])
        self.draw = ImageDraw.Draw(self.img)
    
    def make_poster(self):
        self.new_img()
        self.draw_venue()
        self.draw_artist()

    def draw_artist(self):
        # Center of image
        artist_location = (round(self.width / 2), round(self.height / 2))
        artist_fnt = ImageFont.truetype('/Library/Fonts/NewYork.ttf', self.font_sizes['artist'])
        self.draw.text(artist_location, self.artist, fill=self.colors['font']['black'], anchor='ms', font=artist_fnt)
    
    def draw_admission_price(self):
        price_ftn = ImageFont.truetype('/Library/Fonts/NewYork.ttf', self.font_sizes['venue'])
        pass

    def draw_accent_text(self):
        accent_fnt = ImageFont.truetype('/Library/Fonts/NewYork.ttf', self.font_sizes['accent'])
        # producer and location
        pass

    def draw_extra_info(self):
        extra_info_fnt = ImageFont.truetype('/Library/Fonts/NewYork.ttf', self.font_sizes['datetime'])
        pass

    def display(self):
        self.img.show()

    def draw_venue(self):
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
            'bg': self.colors['main']['primary'],
            'accent': self.colors['accent']['secondary'],
        }


def main():
    poster = PosterBuilder()
    poster.artist = 'Made by Robots'
    poster.venue = 'Radio Bean'
    poster.make_poster()
    poster.draw_debug()
    poster.display()

if __name__ == '__main__':
    main()