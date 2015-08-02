__author__ = 'Amirhossein'

from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Ellipse, Color

class TrackBar(Widget):

    __num_markers = 10

    def __init__(self, **kwargs):
        super(TrackBar, self).__init__(**kwargs)

        with self.canvas:

            # some consts for rational draw
            center_x = self.width / 2
            height_factor = self.height / self.__num_markers

            Color(1, 0, 0)
            Rectangle(pos=self.pos, size=(self.width, self.height))

            # draw markers
            for marker_idx in range(self.__num_markers):

                # Add the marker
                Color(1, 1, 0)
                marker_diameter = (self.__num_markers- abs(marker_idx - self.__num_markers / 2)) * height_factor / 5 + 3
                Ellipse(pos=(self.x + center_x - marker_diameter / 2, self.y + marker_idx*height_factor),
                        size=(marker_diameter, marker_diameter)
                        )
                
